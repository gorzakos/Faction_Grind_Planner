import os
import shutil

def path_guardrails(path):
    project_root = os.path.join(os.path.dirname(__file__), "..")
    allowed_path = os.path.abspath(project_root)
    target_path = os.path.abspath(path)
    common_path = os.path.commonpath([target_path, allowed_path])
    if common_path != allowed_path:
        error_message = f"Path supplied ({target_path}) is out of bounds from the project directory: {allowed_path}"
        raise ValueError(error_message)

def copy_static_content():
    shutil.copytree("static", "public", dirs_exist_ok=True)

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

def create_start_page():
    title = "Factions List"
    content = get_factions_list_html()
    write_page("public/index.html", title, content)

def get_factions_list_html():
    #Todo grab list from DB, feed it into a function that makes HTML from it
    html = "<p>The Dead</p><p>Neriak Guard Inner</p>"
    return html
