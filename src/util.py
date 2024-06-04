# type: ignore

import re

from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    """
    Convert TextNode to HTMLNode/LeafNode.
    """
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError("Invalid text type.")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    """
    Helper function that extracts the alt text and the url from the markdown
    syntax for images.

    Args:
        text (str): The markdown text from which to extract alt text and url of
        images.

    Returns:
        list[tuple[str, str]]: A list of tuples where the tuple has two elements
        - the first one being the alt text and the second one the url.
    """
    r = r"!\[(.*?)\]\((.*?)\)"
    ret = re.findall(r, text)
    return ret


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    """
    Helper function that extracts the link text and its url from the markdown
    syntax for links.

    Args:
        text (str): The markdown text from which to extract link text and url.

    Returns:
        list[tuple[str, str]]: A list of tuples where the tuple has two elements
        - the first one is the link text and the second is the url.
    """
    r = r"\[(.*?)\]\((.*?)\)"
    ret = re.findall(r, text)
    return ret


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    pass


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    pass
