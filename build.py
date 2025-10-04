from jinja2 import Template
from http import HTTPStatus
import os

status_codes = [400, 401, 403, 404, 405, 408, 429, 500, 502, 503, 504]

with open("template.html") as f:
    template_str = f.read()

template = Template(template_str)

output_dir = "error_pages"
os.makedirs(output_dir, exist_ok=True)

for code in status_codes:
    code_info = HTTPStatus(code)

    html_content = template.render(code=code_info)
    file_path = os.path.join(output_dir, f"{code}.html")
    with open(file_path, "w") as f:
        f.write(html_content)

print(f"Generated {len(status_codes)} error pages in '{output_dir}' directory.")
