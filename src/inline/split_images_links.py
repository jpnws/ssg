from typing import Callable

from ..util import (
    text_type_image,
    text_type_link,
    text_type_text,
)
from .extract_images_links import extract_markdown_images, extract_markdown_links
from .text_node import TextNode


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    """
    Split the text nodes into normal text nodes and markdown image text nodes.

    Args:
        - old_nodes: list[TextNode]: Target nodes to be splitted.

    Returns:
        - list[TextNode]: list of text nodes that have been split.
    """
    return node_splitter(old_nodes, extract_markdown_images, text_type_image)


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    """
    Split the text nodes into normal text nodes and markdown link text nodes.

    Args:
        - old_nodes: list[TextNode]: Target nodes to be splitted.

    Returns:
        - list[TextNode]: list of text nodes that have been split.
    """
    return node_splitter(old_nodes, extract_markdown_links, text_type_link)


def node_splitter(
    old_nodes: list[TextNode],
    extractor: Callable[[str], list[tuple[str, str]]],
    text_type: str,
) -> list[TextNode]:
    """
    Extract markdown image or link texts from the TextNode and serialize them
    into their own TextNodes.

    Args:
        - old_nodes (list[TextNode]): The text nodes that contain non-serialized
          version of the markdown image or link syntax.
        - extractor (Callable): The function that uses regex to extract out the
          texts within the markdown image or link syntax.
        - text_type (str): The text type would be either "image" or "link".

    Returns:
        - list[TextNode]: a list of text nodes that have the serialized version
          of either markdown image or link.
    """
    # Store the new nodes for later return.
    new_nodes: list[TextNode] = []
    for old_node in old_nodes:
        # Copy the text of the current node to analyze.
        text = old_node.text
        # Make use of the extraction function we wrote.
        target_tuples = extractor(old_node.text)
        # If there are no markdown targets, let it through without splitting.
        if not target_tuples:
            new_nodes.append(old_node)
            continue
        for target_tuple in target_tuples:
            delim = ""
            if text_type == text_type_image:
                delim = f"![{target_tuple[0]}]({target_tuple[1]})"
            elif text_type == text_type_link:
                delim = f"[{target_tuple[0]}]({target_tuple[1]})"
            # Use split method to separate normal text from markdown target.
            split_text = text.split(f"{delim}", 1)
            # If the very first item in the split string is non-empty string
            # then it must be a normal text segment; therefore, create a normal
            # text node for it.
            if split_text[0]:
                new_nodes.append(TextNode(split_text[0], text_type_text))
            # Also, create a markdown target text node after that because we've
            # found the delimiter, so we can just use the existing target_tuple
            # values to create the markdown target text node.
            new_nodes.append(TextNode(target_tuple[0], text_type, target_tuple[1]))
            # Now, whatever the last item is in the split_text is the remaining
            # text to analyze; therefore, we overwrite the text variable with
            # the last item in the split text list. It is the string that should
            # containing either some normal text or a combination of normal and
            # markdown target.
            text = split_text[-1]
        # Suppose that we've went through all the extracted target tuples, this
        # means that we have completely serialized the markdown syntax, but to
        # make sure to consider normal text that follows the last markdown
        # syntax, we create TextNode out of the remain text (if non-empty).
        if text:
            new_nodes.append(TextNode(text, text_type_text))
    return new_nodes
