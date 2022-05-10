# Description

`csp-scan` is a Python script for constructing strict `content-security-policy` headers based on content of HTML files in a source directory. It looks for used sources and hrefs in HTML elements for most CSP directives and outputs the header content.

Includes a warning system for unencrypted HTTP connections.



# Installation

`pip3 install csp-scan`

# Usage

`cd my-frontend-src`

`csp-scan`

## Options

  `-d`, `--default-src`
                        
    Value for default src directive. Default: self
  
  `-r`, `--report-uri`
    
    Report URI to post violations to.
  
  `-l`, `--literal-src`     
    
    Include whole src paths in the CSP.

# Contribution / forking

Contributions welcome!

### Context

`Directive` class is initiated with a name of the directive (e.g. `script-src`, `style-src`...). Uses regex to locate specific attribute in a HTML element, given an optional pre-condition or file format. 

File `definitions.py` creates directive objects and defines their conditions through `add_search_instruction` method. If you want to add a directive or modify a search condition, do it there. 

```python
style_src.add_search_instruction(
    tag = "link",
    attribute = "href",
    format = ".css"
)
```

This instruction will find and classify this source as style-src:

```html    
<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.0/css/font-awesome.min.css"/>
```

But not this:

```html    
<link href="https://somecdn/js/somejsfile.js"/>
```

```python
style_src.add_search_instruction(
    tag = "link",
    attribute = "href",
    condition = ("rel", "stylesheet")
)
```

This instruction will find and classify this source as style-src:

```html    
<link
    href="https://fonts.googleapis.com/css2?family=Montserrat:wght@100;400;500;600;700&display=swap"
    rel="stylesheet"
/>
```

But not this:

```html    
<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.0/css/font-awesome.min.css"/>
```

```python
style_src.add_search_instruction(
    tag = "link",
    attribute = "href"
)
```

This instruction would find and classify all of the above examples.