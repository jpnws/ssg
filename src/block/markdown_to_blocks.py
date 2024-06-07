def markdown_to_blocks(markdown: str) -> list[str]:
    """
    Given markdown text create a list of markdown blocks based on the fact that
    each markdown block is separated by an empty line "\n\n". Also, ensure that
    all the whitespaces are stripped from the start and end of the blocks and
    all the lines within the blocks as well.

    Parameters:
        - markdown (str): The markdown text to parse for block extraction.

    Returns:
        - list[str]: A list of all the blocks with markdown text.
    """
    raise NotImplementedError
