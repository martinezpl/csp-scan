import re

# add nonces, hashes,
class Directive:
    def __init__(self, name: str):
        self.name = name
        
        self.search_instructions = set()
        self.urls_found = set()
        self.files_found = set()
        
        self.unsecure_conns = set()
    
    def __rgx(self, tag: str, att: str, format: str = "") -> re.Pattern:
        # Regex expression to find X in <tag ... att="X"> or <tag ... att='X'>
        exp = f"<{tag}.+?{att}="
        
        if format:
            exp += f".([^'\"]+\{format})"
        else:
            exp += ".([^'\"]+)"
        
        return re.compile(exp)

    def add_search_instruction(
        self, 
        tag: str, 
        attribute: str, 
        format: str = "", 
        condition: tuple = None
    ):
        instruction = ( self.__rgx(tag, attribute, format), condition )
        self.search_instructions.add(instruction)

    def scan_html(self, html: str, file_name: str = ""):
        for instruction in self.search_instructions:
            regex_expression = instruction[0]
            condition = instruction[1]
            
            for match in re.finditer(regex_expression, html):
                if condition: 
                    if not re.search(f"{condition[0]}=.{condition[1]}.", match.string):
                        continue
                url = match.group(1)
                if "http" in url:
                    self.urls_found.add(url)
                    if not "https" in url:
                        self.unsecure_conns.add((match.group(1), file_name))
                        url = url.replace('http', '\033[1;35mhttp\033[0m')

                        print("\033[1;31mWARNING: \033[0m\033[0;37mUnencrypted connection\033[0m\n", url, "in", file_name, "\n\n")
                else:
                    self.files_found.add(match.group(1))

    def get_csp_string(self, literal_src: bool = False):
        csp = f"{self.name} 'none'"
        if self.files_found:
            csp = csp.replace("none", "self")
        
        if self.urls_found:
            csp = csp.replace(" 'none'", "")
            if literal_src:
                sources = self.urls_found
            else:
                sources = set()
                for url in self.urls_found:
                    protocol = url.split("//")[0]
                    domain = url.split("//")[1].split("/")[0]
                    sources.add(f"{protocol}//{domain}")
            
            csp += " " + " ".join(sources)
        
        return csp
