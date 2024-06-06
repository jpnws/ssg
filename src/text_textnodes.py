from textnode import TextNode

from split_delimiter import split_nodes_delimiter
from split_images_links import split_nodes_image
from split_images_links import split_nodes_link


def text_to_textnodes(text: str) -> list[TextNode]:
    res = [TextNode(text, "text")]
    res = split_nodes_image(res)
    res = split_nodes_link(res)
    res = split_nodes_delimiter(res, "**", "bold")
    res = split_nodes_delimiter(res, "`", "code")
    res = split_nodes_delimiter(res, "*", "italic")
    return res
