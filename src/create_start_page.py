import os

def path_guardrails(path):
    project_root = os.path.join(os.path.dirname(__file__), "..")
    allowed_path = os.path.abspath(project_root)
    target_path = os.path.abspath(path)
    common_path = os.path.commonpath([target_path, allowed_path])
    if common_path != allowed_path:
        error_message = f"Path supplied ({target_path}) is out of bounds from the project directory: {allowed_path}"
        raise ValueError(error_message)

def write_page(dest_path, title, content):
    path_guardrails(dest_path)
    template_path = "template.html"
    template_file = open(template_path)
    template = template_file.read()
    template_file.close()
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    directories, file_name = os.path.split(dest_path)
    os.makedirs(directories, exist_ok=True)
    html_file = open(dest_path, "w")
    html_file.write(page)
    html_file.close()
