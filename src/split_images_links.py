from typing import Callable

from textnode import TextNode

from extract_links import extract_markdown_images
from extract_links import extract_markdown_links


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    """
    Split the text nodes into normal text nodes and markdown image text nodes.

    Args:
        - old_nodes: list[TextNode]: Target nodes to be splitted.

    Returns:
        - list[TextNode]: list of text nodes that have been split.
    """
    return node_splitter(old_nodes, extract_markdown_images, "image")


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    """
    Split the text nodes into normal text nodes and markdown link text nodes.

    Args:
        - old_nodes: list[TextNode]: Target nodes to be splitted.

    Returns:
        - list[TextNode]: list of text nodes that have been split.
    """
    return node_splitter(old_nodes, extract_markdown_links, "link")


def node_splitter(
    old_nodes: list[TextNode],
    extractor: Callable[[str], list[tuple[str, str]]],
    text_type: str,
) -> list[TextNode]:
    """ """
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
        for target_tuple in target_tuples:
            delim = ""
            if text_type == "image":
                delim = f"![{target_tuple[0]}]({target_tuple[1]})"
            elif text_type == "link":
                delim = f"[{target_tuple[0]}]({target_tuple[1]})"
            # Use split method to separate normal text from markdown target.
            split_text = text.split(f"{delim}", 1)
            # If the very first item in the split string is non-empty string
            # then it must be a normal text segment; therefore, create a normal
            # text node for it.
            if split_text[0]:
                new_nodes.append(TextNode(split_text[0], "text"))
            # Also, create a markdown target text node after that because we've
            # found the delimiter, so we can just use the existing target_tuple
            # values to create the markdown target text node.
            new_nodes.append(TextNode(target_tuple[0], text_type, target_tuple[1]))
            # Now, whatever the last item is in the split_text is the remaining
            # text to analyze; therefore, we overwrite the text variable with
            # the last item in the split text list. It is the string that should
            # containg either some normal text or a combination of normal and
            # markdown target.
            text = split_text[-1]
        # Suppose that we've went through all the extracted target tuples, this
        # means that we have completely serialized the markdown syntax, but to
        # make sure to consider normal text that follows the last markdown
        # syntax, we create TextNode out of the remain text (if non-empty).
        if text:
            new_nodes.append(TextNode(text, "text"))
    return new_nodes


# def node_splitter(
#     old_nodes: list[TextNode],
#     extractor: Callable[[str], list[tuple[str, str]]],
#     text_type: str,
# ) -> list[TextNode]:
#     """
#     Intermediary function for processing `TextNode`s to split them by markdown
#     image/link syntax in a target text string.

#     Args:
#         - old_nodes list[TextNode]: Target nodes to be splitted.
#         - extractor Callable[[str], list[tuple[str, str]]]: Extractor function
#           that takes a string argument and returns a list of tuples with two
#           items per tuple.
#         - text_type str: The type of text to target (e.g. image/link)

#     Returns:
#         - list[TextNode]: A list of text nodes containing normal and markdown
#           image/link segments.
#     """
#     # A list to store all the final `TextNode`s.
#     new_nodes: list[TextNode] = []
#     for old_node in old_nodes:
#         # The extractor is a function that takes in a string, extracts target
#         # segments within the string and returns a list of tuple[str, str].
#         target_tuples = extractor(old_node.text)
#         # If there are tuples, if it's empty then that means no target segments
#         # were found, so we consider this as just normal text TextNode, so we
#         # just put it into the new_nodes list straight.
#         if not target_tuples:
#             new_nodes.append(old_node)
#             continue
#         # Now, we know that the target text string (markdown) contains the
#         # target segments (the delimiters) because of the check above, so what
#         # we want to do is to separate the normal texts from the target segment
#         # (the delimiters), create `TextNode`s out of them.
#         split_nodes = splitter(old_node.text, target_tuples, text_type)
#         # We then take the resulting list of `TextNode`s (combination of normal
#         # texts and delimited texts (image/link) from the markdown text).
#         new_nodes.extend(split_nodes)
#     return new_nodes


# def splitter(
#     text: str, delim_tuples: list[tuple[str, str]], text_type: str
# ) -> list[TextNode]:
#     """
#     Args:
#         - text (str): The string to be analyzed.
#         - delim_tuples (list[tuple[str, str]]): The list of tuples contain a
#           tuple of the form (delim-text, delim-url).
#         - text_type (str): The text type of the delimiter.

#     Returns:
#         - list[TextNode]: A list of `TextNode`s containing the image and link
#           from markdown to the intermediary object TextNode with normal text
#           TextNode.
#     """
#     # Store the resulting `TextNode`s. This will contain both normal text
#     # `TextNode`s and either image or link `TextNode`s.
#     new_nodes: list[TextNode] = []
#     # This is used for concatenating any normal text as we advance through the
#     # target text string. This will be reset to an empty string whenever we find
#     # the delimiter.
#     normal_segment = ""
#     # Keep track of the position in the target text string.
#     i = 0
#     for delim_tuple in delim_tuples:
#         # Set the delimiter depending on the text type: either image or link.
#         delim = ""
#         if text_type == "image":
#             delim = f"![{delim_tuple[0]}]({delim_tuple[1]})"
#         elif text_type == "link":
#             delim = f"[{delim_tuple[0]}]({delim_tuple[1]})"
#         # Step through the target text string.
#         while i < len(text):
#             # Check if a certain segment of `len(delim)` from the current index
#             # is the delimiter within the target text string.
#             if text[i : i + len(delim)] == delim:
#                 # Now, suppose that we've found the delimiter, then we first
#                 # check if there were non-delimiter normal text segment prior to
#                 # it. So, if there's anything in the `normal_segment` then
#                 # append it to new_nodes as a normal TextNode.
#                 if normal_segment:
#                     new_nodes.append(TextNode(normal_segment, "text"))
#                 # And, since we've found the delimiter within the text, let's
#                 # use the tuple items to create the TextNode, it would be either
#                 # image or link text type.
#                 new_nodes.append(TextNode(delim_tuple[0], text_type, delim_tuple[1]))
#                 # Okay, and since we've stored a TextNode of the normal text
#                 # preceding the delimit text, we can now reset normal_segment
#                 # string here.
#                 normal_segment = ""
#                 # Advance the index by the length of the delimiter and
#                 i += len(delim)
#                 # Break out of this loop now because we've taken care of
#                 # identifying and creating the `TextNode`s for the delimiter and
#                 # other normal text segment prior to it if they existed.
#                 break
#             else:
#                 # Suppose we have not found the delimiter yet, then just
#                 # concatenate the current character in the target text string
#                 # into the normal_segment variable.
#                 normal_segment += text[i]
#             # If the program reaches this point, then it means that we have not
#             # hit a delimiter yet, because if we did, then this entire while
#             # loop would have just been broken out as specified above under the
#             # if-block.
#             i += 1
#     # Now, suppose that we've identified all the normal text `TextNode`s and the
#     # image/link `TextNode`s up to the very last image/link `TextNode` within
#     # the target text string. However, one thing that's missing is, what if
#     # there was more normal text following the last image/link `TextNode`? In
#     # that case, we first check if the `i` index have not already reached the
#     # end of the target text string position.
#     if i < len(text):
#         # If the index is still less than the total length of the target text
#         # string, then let's concatenate all the remaining text.
#         while i < len(text):
#             normal_segment += text[i]
#             i += 1
#         # And then, finally, we append that remaining text's `TextNode` to
#         # new_nodes.
#         new_nodes.append(TextNode(normal_segment, "text"))
#     return new_nodes
