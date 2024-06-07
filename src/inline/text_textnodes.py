from inline.text_node import TextNode

from split_delimiter import split_nodes_delimiter
from split_images_links import split_nodes_image
from split_images_links import split_nodes_link

from util import (
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


def text_to_textnodes(text: str) -> list[TextNode]:
    res = [TextNode(text, text_type_text)]
    res = split_nodes_image(res)
    res = split_nodes_link(res)
    res = split_nodes_delimiter(res, "**", text_type_bold)
    res = split_nodes_delimiter(res, "`", text_type_code)
    res = split_nodes_delimiter(res, "*", text_type_italic)
    return res
