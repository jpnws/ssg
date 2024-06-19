import os
import shutil

from block.block_nodes_to_html_nodes import block_nodes_to_html_nodes
from block.markdown_to_block_nodes import markdown_to_block_nodes


def copy_static_assets():
    """
    Copy the static assets from the `static` directory to the `public` directory.
    """
    cur_file_path = os.path.realpath(__file__)
    cur_folder_path = os.path.dirname(cur_file_path)
    root_folder_path = os.path.dirname(cur_folder_path)
    static_dir_rel = os.path.join(root_folder_path, "static")
    static_dir_abs = os.path.abspath(static_dir_rel)
    if not os.path.exists(static_dir_abs):
        raise FileNotFoundError(
            f"static directory (`{static_dir_abs}`) must exist in the project root."
        )
    public_dir_path = os.path.join(root_folder_path, "public")
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)
    src_paths = [
        os.path.join(static_dir_abs, item) for item in os.listdir(static_dir_abs)
    ]
    copy_func(src_paths, public_dir_path)


def copy_func(src_paths: list[str], dest_path: str):
    for src_path in src_paths:
        if os.path.isdir(src_path):
            # If current path is a directory get the items within it and recurse
            # the function by passing the list of items and pass the destination
            # path as well.
            next_src_paths = [
                os.path.join(src_path, item) for item in os.listdir(src_path)
            ]
            copy_func(next_src_paths, dest_path)
        if os.path.isfile(src_path):
            # If current path is a file, get the directory path relative the the
            # source directory. (e.g. if src_path is `static/images/sample.png`,
            # then the directory path relative to the source directory would be
            # `images`).
            src_dir_path = os.path.dirname(src_path).split("/static")[-1].strip("/")
            # Since we need to have the same directory tree structure in the
            # destination folder, we first create the path to the `src_dir_path`
            # relative to the destination folder. (e.g. if `src_dir_path` is
            # `images`, then the destination directory path would be
            # `public/images`).
            dest_dir_path = os.path.join(dest_path, src_dir_path)
            # Create the destination directory path recursively.
            os.makedirs(dest_dir_path, 0o777, True)
            # Then we get the source file name and create the destination file
            # path by joining the `dest_dir_path` and `src_file_name`. (e.g. if
            # `src_path` is `static/images/sample.png`, then the `src_file_name`
            # would be `sample.png` and the `dest_file_path` would be
            # `public/images/sample.png`).
            src_file_name = os.path.basename(src_path)
            dest_file_path = os.path.join(dest_dir_path, src_file_name)
            shutil.copyfile(src_path, dest_file_path)


def extract_title(markdown: str) -> str:
    """
    Extract the title for the page.
    """
    for line in markdown.splitlines():
        if "# " in line:
            return line.replace("# ", "")
    raise ValueError("no h1 header found: must have a markdown `#` h1 header.")


def generate_page(from_path: str, template_path: str, dest_path: str):
    """
    Generate page.
    """
    # print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_contents = ""
    from_path = os.path.abspath(from_path)
    with open(from_path) as f:
        markdown_contents = f.read()
    template_contents = ""
    with open(template_path) as f:
        template_contents = f.read()
    block_nodes = markdown_to_block_nodes(markdown_contents)
    html_nodes = block_nodes_to_html_nodes(block_nodes)
    page_html = html_nodes.to_html()
    page_title = extract_title(markdown_contents)
    template_contents = template_contents.replace("{{ Title }}", page_title)
    template_contents = template_contents.replace("{{ Content }}", page_html)
    html_file_name = os.path.basename(from_path).split(".")[0]
    html_file = f"{html_file_name}.html"
    html_path = os.path.join(dest_path, html_file)
    with open(html_path, "w+") as f:
        f.write(template_contents)


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str
):
    """
    Recursively generate all pages.

    Args:
        - dir_path_content (str): The path to the `content` directory that
          should be recursed.
        - template_path (str): The path to the HTML template file.
        - dest_dir_path (str): The destination folder path to which the
          generated HTML file should be stored.
    """
    # print(
    # f"Generating pages from {dir_path_content} to {dest_dir_path} using {template_path}"
    # )
    if not os.path.exists(dir_path_content):
        raise FileNotFoundError(
            f"directory (`{dir_path_content}`) must exist in the project root."
        )
    src_paths = [
        os.path.abspath(os.path.join(dir_path_content, item))
        for item in os.listdir(dir_path_content)
    ]
    generate_pages_func(src_paths, template_path, dest_dir_path)


def generate_pages_func(src_paths: list[str], template_path: str, dest_path: str):
    for src_path in src_paths:
        if os.path.isdir(src_path):
            next_src_paths = [
                os.path.join(src_path, item) for item in os.listdir(src_path)
            ]
            generate_pages_func(next_src_paths, template_path, dest_path)
        if os.path.isfile(src_path):
            src_dir_path = os.path.dirname(src_path).split("/content")[-1].strip("/")
            dest_dir_path = os.path.join(dest_path, src_dir_path)
            os.makedirs(dest_dir_path, 0o777, True)
            generate_page(src_path, template_path, dest_dir_path)


if __name__ == "__main__":
    copy_static_assets()
    generate_pages_recursive("content", "template.html", "public")
