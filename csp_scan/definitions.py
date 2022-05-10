from csp_scan.directive import Directive

# BASE URI; 
base_uri = Directive("base-uri")
base_uri.add_search_instruction(
    tag = "base",
    attribute = "href"
)

# CHILD & FRAME ANCESTORS; 
child_src = Directive("child-src")
child_src.add_search_instruction(
    tag = "iframe",
    attribute = "src"
)
child_src.add_search_instruction(
    tag = "frame",
    attribute = "src"
)

frame_src = Directive("frame-src")
frame_src.search_instructions = child_src.search_instructions

frame_ancestors = Directive("frame-ancestors")
frame_ancestors.search_instructions = frame_src.search_instructions

# SCRIPTS; 
script_src = Directive("script-src")
script_src.add_search_instruction(
    tag = "script",
    attribute = "src"
)
script_src_elem = Directive("script-src-elem")
script_src_elem.search_instructions = script_src.search_instructions
script_src_attr = Directive("script-src-attr")
script_src_attr.search_instructions = script_src.search_instructions

# FONTS + STYLES; 
# TODO: inline css?
style_src = Directive("style-src")
style_src.add_search_instruction(
    tag = "style",
    attribute = "src"
)
style_src.add_search_instruction(
    tag = "link",
    attribute = "href",
    format = ".css"
)
style_src.add_search_instruction(
    tag = "div",
    attribute = "style"
)
style_src.add_search_instruction(
    tag = "link",
    attribute = "href",
    condition = ("rel", "stylesheet")
)

font_src = Directive("font-src")
font_src.search_instructions = style_src.search_instructions

# OBJECTS; 
objects_src = Directive("object-src")
objects_src.add_search_instruction(
    tag = "object",
    attribute = "data"
)
objects_src.add_search_instruction(
    tag = "embed",
    attribute = "src"
)
objects_src.add_search_instruction(
    tag = "applet",
    attribute = "archive"
)

# IMAGES; 
img_src = Directive("img-src")
img_src.add_search_instruction(
    tag = "img",
    attribute = "src"
)

# MEDIA; 
media_src = Directive("media-src")
media_src.add_search_instruction(
    tag = "audio",
    attribute = "src"
)
media_src.add_search_instruction(
    tag = "video",
    attribute = "src"
)
media_src.add_search_instruction(
    tag = "source",
    attribute = "src"
)

# MANIFEST; 
manifest_src = Directive("manifest-src")
manifest_src.add_search_instruction(
    tag = "link",
    attribute = "href",
    condition = ("rel", "manifest")
)

# NAVIGATE-TO; 
navigate_to = Directive("navigate-to")
navigate_to.add_search_instruction(
    tag = "a",
    attribute = "href"
)
navigate_to.add_search_instruction(
    tag = "area",
    attribute = "href"
)

# FORM-ACTION; 
form_action = Directive("form-action")
form_action.add_search_instruction(
    tag = "form",
    attribute = "action"
)

# PREFETCH; 
prefetch = Directive("prefetch")
prefetch.add_search_instruction(
    tag = "link",
    attribute = "href",
    condition = ("rel", "prefetch")
)
prefetch.add_search_instruction(
    tag = "link",
    attribute = "href",
    condition = ("rel", "prerender")
)

DIRECTIVES = [
    base_uri,
    child_src,
    frame_src,
    frame_ancestors,
    script_src,
    script_src_elem,
    script_src_attr,
    style_src,
    font_src,
    objects_src,
    img_src,
    media_src,
    manifest_src,
    navigate_to,
    form_action,
    prefetch
]

# CONNECT-SRC
# TODO: inline scripts, all