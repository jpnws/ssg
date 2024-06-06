from typing import Callable

from textnode import TextNode

from extract_links import extract_markdown_images
from extract_links import extract_markdown_links


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    return node_splitter(old_nodes, extract_markdown_images, "image")


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    return node_splitter(old_nodes, extract_markdown_links, "link")


def node_splitter(
    old_nodes: list[TextNode],
    extractor: Callable[[str], list[tuple[str, str]]],
    text_type: str,
) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for old_node in old_nodes:
        target_tuples = extractor(old_node.text)
        if not target_tuples:
            new_nodes.append(old_node)
            continue
        new_nodes.extend(splitter(old_node.text, target_tuples, text_type))
    return new_nodes


def splitter(
    text: str, delim_tuples: list[tuple[str, str]], text_type: str
) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    normal_segment = ""
    i = 0
    for delim_tuple in delim_tuples:
        delim = ""
        if text_type == "image":
            delim = f"![{delim_tuple[0]}]({delim_tuple[1]})"
        elif text_type == "link":
            delim = f"[{delim_tuple[0]}]({delim_tuple[1]})"
        while i < len(text):
            if text[i : i + len(delim)] == delim:
                if normal_segment:
                    new_nodes.append(TextNode(normal_segment, "text"))
                new_nodes.append(TextNode(delim_tuple[0], text_type, delim_tuple[1]))
                normal_segment = ""
                i += len(delim)
                break
            else:
                normal_segment += text[i]
            i += 1
    if i < len(text):
        while i < len(text):
            normal_segment += text[i]
            i += 1
        new_nodes.append(TextNode(normal_segment, "text"))
    return new_nodes
