from ..util import (
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_text,
)
from .split_delimiters import split_nodes_delimiter
from .split_images_links import split_nodes_image, split_nodes_link
from .text_node import TextNode


def text_to_text_nodes(text: str) -> list[TextNode]:
    res = [TextNode(text, text_type_text)]
    res = split_nodes_image(res)
    res = split_nodes_link(res)
    res = split_nodes_delimiter(res, "**", text_type_bold)
    res = split_nodes_delimiter(res, "`", text_type_code)
    res = split_nodes_delimiter(res, "*", text_type_italic)
    res = split_nodes_delimiter(res, "_", text_type_italic)
    return res
