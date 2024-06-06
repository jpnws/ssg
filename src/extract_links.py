import re


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
