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


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: str
) -> list[TextNode]:
    ret: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != "text":
            ret.append(node)
        else:
            ret.extend(splitter(node.text, delimiter, text_type))
    return ret


def splitter(text: str, delim: str, text_type: str) -> list[TextNode]:
    start_found = False
    segments: list[TextNode] = []
    normal_segment: str = ""
    delim_segment: str = ""
    index = 0
    while index < len(text):
        if text[index : index + len(delim)] == delim:
            if start_found:
                start_found = False
                segments.append(TextNode(delim_segment, text_type))
                delim_segment = ""
            else:
                start_found = True
                segments.append(TextNode(normal_segment, "text"))
                normal_segment = ""
        else:
            if start_found:
                delim_segment += text[index]
            else:
                normal_segment += text[index]
        if index == len(text) - 1 and not start_found and normal_segment:
            segments.append(TextNode(normal_segment, "text"))
        if text[index : index + len(delim)] == delim:
            index += len(delim)
        else:
            index += 1
    return segments
