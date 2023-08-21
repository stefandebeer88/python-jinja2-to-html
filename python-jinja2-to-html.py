from jinja2 import Template

template_string = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>{{ content }}</p>
</body>
</html>
"""

data = {
    'title': 'Jinja HTML Compiler Title',
    'heading': 'Jinja2 HTML Compiler Heading',
    'content': 'Example of using Jinja2 to build an HTML document.',
}

template = Template(template_string)
rendered_html = template.render(data)

with open('output.html', 'w') as f:
    f.write(rendered_html)

