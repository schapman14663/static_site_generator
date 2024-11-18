import os
import shutil
import time

from gencontent import generate_page, generate_pages_recursive
from textnode import TextNode, TextType


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    home_dir = "/Users/simonchapman/"
    project_dir = os.path.join(
        home_dir, "Documents/other_coding_study/boot_dev_work/static_website/"
    )
    public_dir = os.path.join(project_dir, "public")
    static_dir = os.path.join(project_dir, "static")
    content_dir = os.path.join(project_dir, "content")

    template_path = os.path.join(project_dir, "template.html")

    refresh_directory(public_dir)
    copy_static(static_dir, public_dir)

    print("Generating Page...")
    generate_pages_recursive(content_dir, template_path, public_dir)


def copy_static(from_dir, to_dir):

    contents_static_dir = os.listdir(from_dir)
    print(contents_static_dir)

    for node in contents_static_dir:
        node_path = os.path.join(from_dir, node)
        print(node_path)
        if os.path.isfile(node_path):
            shutil.copy(node_path, to_dir)
            print(f"copied {node} to the public directory")
            time.sleep(1)
        if os.path.isdir(node_path):
            new_from_dir = os.path.join(from_dir, node)
            new_to_dir = os.path.join(to_dir, node)
            os.mkdir(new_to_dir)
            print(f"created new directory {new_to_dir}")
            time.sleep(5)
            print(f"running copy algorithm from {new_from_dir} to {new_to_dir}")
            time.sleep(5)
            copy_static(new_from_dir, new_to_dir)


def refresh_directory(directory):

    if os.path.exists(directory):
        shutil.rmtree(directory)
        print("deleting existing public directory...")
        time.sleep(2)
        os.mkdir(directory)
        print("creating blank public directory")


main()
