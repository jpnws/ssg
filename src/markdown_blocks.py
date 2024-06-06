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
    # First, split the entire text by blocks.
    markdown_blocks: list[str] = markdown.split("\n\n")
    # Second, strip whitespaces around each block.
    stripped_blocks: list[str] = []
    for line in markdown_blocks:
        if line:
            stripped_blocks.append(line.strip())
    # Third, strip whitespace from every line from every block.
    line_stripped_blocks: list[str] = []
    for block in stripped_blocks:
        if block:
            line_stripped: list[str] = []
            for block_line in block.split("\n"):
                line_stripped.append(block_line.strip())
            line_stripped_blocks.append("\n".join(line_stripped))
    return line_stripped_blocks
    # Most likely a complicated approach.
    # return [
    #     "\n".join([block_line.strip() for block_line in block.split("\n")])
    #     for block in [line.strip() for line in markdown.split("\n\n") if line]
    #     if block
    # ]
