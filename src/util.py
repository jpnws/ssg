# type: ignore

import re

from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


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
