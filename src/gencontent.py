import os

from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)

    for node in contents:
        node_path = os.path.join(dir_path_content, node)
        if os.path.isfile(node_path):
            node_strip = node.strip(".md")
            node_html = f"{node_strip}.html"
            dest_path = os.path.join(dest_dir_path, node_html)
            generate_page(node_path, template_path, dest_path)
        if os.path.isdir(node_path):
            new_from_dir = os.path.join(dir_path_content, node)
            new_to_dir = os.path.join(dest_dir_path, node)
            os.mkdir(new_to_dir)
            generate_pages_recursive(new_from_dir, template_path, new_to_dir)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")
