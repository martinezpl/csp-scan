import os
from optparse import OptionParser

from csp_scan.definitions import DIRECTIVES

parser = OptionParser()
parser.add_option('-d', '--default-src', type='string', default="'self'", help="Value for default src directive. Default: 'self'")
parser.add_option('-r', '--report-uri', type='string', help='Report URI to post violations to.')
parser.add_option('-l', '--literal-src', action='store_true', default=False, help='Include whole src path in the CSP.')
(options, args) = parser.parse_args()

def main():
    report_uri = options.report_uri
    literal_src = options.literal_src
    default_src = options.default_src

    # Find all the html files in the current directory
    html_files = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(".")
        for file in files
        if file.endswith(".html")
    ]
    if not html_files:
        print("\033[31;1;4mNo HTML files found in the current directory.\033[0m")
        return
    elif html_files:
        print("\033[1;32mFound", len(html_files), "HTML files. Press enter to continue.\033[0m")
        input()

    for file in html_files:
        with open(file, 'r') as f:
            html = f.read()
            for directive in DIRECTIVES:
                directive.scan_html(html, file)
    
    csp = f"default-src '{default_src}'"
    for directive in DIRECTIVES:
        csp += f"; {directive.get_csp_string(literal_src)}"
    if report_uri:
        csp += f"; report-uri {report_uri}"

    print(f"\033[1;32m ----- CONTENT-SECURITY-POLICY ----- \033[0m")
    return csp

if __name__ == "__main__":
    main()
