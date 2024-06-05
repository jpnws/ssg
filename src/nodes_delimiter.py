from textnode import TextNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: str
) -> list[TextNode]:
    """
    Splits TextNode objects in a list by a given delimiter and converts them
    into multiple TextNodes of the specified type.

    Args:
        - old_nodes (list[TextNode]): List of TextNode objects to be processed.
        - delimiter (str): The delimiter string used to split the text.
        - text_type (str): The type of TextNode to create for the text between
          delimiters.

    Returns:
        - list[TextNode]: A new list of TextNode objects, split based on the
          given
        delimiter.

    Raises:
        - ValueError: If a matching closing delimiter is not found in the text.

    Example:
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        # new_nodes will be:
        # [
        #     TextNode("This is text with a ", "text"),
        #     TextNode("code block", "code"),
        #     TextNode(" word", "text"),
        # ]
    """
    ret: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != "text":
            # Append the TextNode as-is if its type is not text.
            ret.append(node)
        else:
            # Otherwise process the TextNode and extend the main TextNodes list
            # with the processed TextNodes list.
            ret.extend(splitter(node.text, delimiter, text_type))
    return ret


def splitter(text: str, delim: str, text_type: str) -> list[TextNode]:
    """
    Helper function to split a text string by a given delimiter and convert
    segments into TextNode objects.

    Args:
        - text (str): The text to be split.
        - delim (str): The delimiter string used to split the text.
        - text_type (str): The type of TextNode to create for the text between
          delimiters.

    Returns:
        - list[TextNode]: A list of TextNode objects created from the split
          text.

    Raises:
        - ValueError: If a matching closing delimiter is not found in the text.

    Example:
        text = "This is text with a `code block` word"
        nodes = splitter(text, "`", "code")
        # nodes will be:
        # [
        #     TextNode("This is text with a ", "text"),
        #     TextNode("code block", "code"),
        #     TextNode(" word", "text"),
        # ]
    """
    # All the TextNode segments are stored here for later return.
    segments: list[TextNode] = []
    # Used for identifying opening and ending of delimited text.
    delim_start_found = False
    # Used for accumulating normal text. This will be reset to empty string when
    # an opening delimiter is found.
    normal_segment = ""
    # Used for accumulating delimited text, the text within `**` from `**bold**`
    # for example. This will be reset to empty string after finding the closing
    # delimiter.
    delim_segment = ""
    # Keep track of whether there was a previous repeated non-delim sequence.
    was_repeated = True
    # Keep track of the non-delim repeat sequence count.
    prev_repeat_count = 0
    # Keep track of the index position in the target text string.
    index = 0
    # If the total occurrences of the delimiter is not even that means there was
    # no proper closing of the delimiter. Raise ValueError.
    if count_delim(text, delim) % 2 != 0:
        raise ValueError("Invalid markdown syntax.")
    # In the following `while` block, the program will loop until `index`
    # hits the length of the target text string.
    while index < len(text):
        # Check if the current position in the text is the start of a delimiter
        # and that we are not already inside a delimited segment.
        if text[index : index + len(delim)] == delim and not delim_start_found:
            if was_repeated and prev_repeat_count > 1:
                # If there was a previous repeat sequence and count is greater
                # than one then just consider the next sequence to be matching
                # non-delim repeats and consider them normal text.
                normal_segment += text[index : index + len(delim) * prev_repeat_count]
                # And then advance the index accordingly and reset vars.
                index += len(delim) * prev_repeat_count
                prev_repeat_count = 0
                was_repeated = False
            # Determine how many times the delimiter is consecutively repeated
            # starting fom the current index position.
            delim_repeat_count = get_delim_repeat_count(text, delim, index)
            if delim_repeat_count > 1:
                # If the delimiter is repeated more than once, consider it as
                # part of the normal text. Add the repeated delimiter sequence
                # to the normal text segment.
                normal_segment += text[index : index + len(delim) * delim_repeat_count]
                # Advance the index by the length of the repeated delimiter
                # sequence.
                was_repeated = True
                prev_repeat_count = delim_repeat_count
                index += len(delim) * delim_repeat_count
        if text[index : index + len(delim)] == delim:
            # If the program enters this block of code, it means that it is
            # currently at a certain position in the target text string where
            # the delimiter exists.
            if delim_start_found:
                # This block of code runs at a closing delimiter.If the program
                # hits this block of code, it means that a closing delimiter was
                # found. Therefore, we now set the delim_start_found back to
                # False.
                delim_start_found = False
                # And create and append the new TextNode containing the
                # delimited segment, for instance if we had the target
                # TextNode("This is text with a `code block` word", "text") and
                # we were delimiting the backtick, then this block of code would
                # append TextNode("code block", "code") to the segments array.
                if delim_segment:
                    segments.append(TextNode(delim_segment, text_type))
                # Once we've created TextNode for the delimited text, we reset
                # the delim_segment string to get ready for any other delimited
                # text segments in the other parts of the target string.
                delim_segment = ""
            else:
                # This block of code runs at an opening delimiter. Therefore, we
                # set delim_start_found to True.
                delim_start_found = True
                # If a normal text exists prior to a delimited text (e.g.
                # TextNode("This is a text with a `code block` word", "text"),
                # where "This is a text with a " is the normal text), we need to
                # create a separate normal text node for it.
                if normal_segment:
                    # Ensure that `normal_segment` is not empty, emptied
                    # normal_segment can happen if there is a delimited text at
                    # the beginning of the target text for example:
                    # TextNode("**bold** text is at the start", "text").
                    segments.append(TextNode(normal_segment, "text"))
                    # Once we've created TextNode for the normal text, we reset
                    # the normal_segment string to get ready for any other
                    # normal text segments in the other parts of the target
                    # string.
                    normal_segment = ""
        else:
            # The program enters this block of code if the current substring
            # within the target text string is not the delimiter.
            if delim_start_found:
                # Even if the current substring within the target text string is
                # not a delimiter, it can be a delimited string like "This is a
                # `**bold**` text", where we could current be at for instance
                # character `l` in the word "bold" which is part of a delimited
                # text. Therefore, we concatenate the substring to
                # `delim_segment`. But we only do this if we know that we've
                # previously found the opening delimiter.
                delim_segment += text[index]
            else:
                # However, if the current substring that we're looking at is not
                # a part of the delimited string, then it is considered as a
                # normal string; therefore, we concatenate the current substring
                # to the `normal_segment`.
                if index < len(text):
                    normal_segment += text[index]
        # Suppose that we reached the end of the target text string there was no
        # more delimiter found, then if there's anything in `normal_segment` it
        # means that the remaining text was a normal text, then create TextNode
        # and append it to `segments`.
        if index == len(text) - 1 and not delim_start_found and normal_segment:
            segments.append(TextNode(normal_segment, "text"))
        # This is where we increment the `index` value, but the size of the
        # increment will vary by two different situations.
        if text[index : index + len(delim)] == delim:
            # One situation is when we find a delimiter, we need to advance the
            # index by the length of the delimiter because in the next loop, we
            # want to just see the delimited text string instead of another
            # character of delimiter itself if the delimiter string is more than
            # one cahracter long such as `**` for bold.
            index += len(delim)
        else:
            # Otherwise, if the current substring is not a delimiter, just
            # advanced index by one.
            index += 1
    # If `delim_start_found` is not False at this point, it means that we did
    # not find any ending delimiter; therefore, the markdown syntax is invalid.
    # For example, if the text "**bold string" is provided, we will have to
    # raise the ValueError because `**` does not close.
    # if delim_start_found:
    #     raise ValueError("Invalid markdown syntax.")
    return segments


def get_delim_repeat_count(text: str, delim: str, index: int) -> int:
    """
    Determine the number of consecutive repetitions of a delimiter starting from
    a given index in the text.

    Args:
        - text (str): The text to be analyzed for repeated delimiters.
        - delim (str): The delimiter string to count repetitions of.
        - index (int): The starting index in the text to begin counting from.

    Returns:
        - int: The count of consecutive delimiter repetitions.

    Example:
        count = get_delim_repeat_count("**bold** text", "*", 0)

        # count will be 2 because there are two consecutive instances of the
        delimiter "*" immediately following the index before breaking out of the
        loop.
    """
    repeated_count = 0
    while index < len(text):
        if text[index : index + len(delim)] == delim:
            repeated_count += 1
        else:
            break
        index += len(delim)
    return repeated_count


def count_delim(text: str, delim: str) -> int:
    """
    Count the total occurrences of the delimiter in the text.

    Args:
        - text (str): The text to be analyzed for counting occurrences of delim.
        - delim (str): The delimiter string count.

    Returns:
        - int: total occurrences of the delimiter.
    """
    index = 0
    count = 0
    while index < len(text):
        if text[index : index + len(delim)] == delim:
            count += 1
            index += len(delim)
        else:
            index += 1
    return count
