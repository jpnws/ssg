from block.block_node import BlockNode
from block.split_blocks import (
    split_blocks_code,
    split_blocks_heading,
    split_blocks_ordered_list,
    split_blocks_quote,
    split_blocks_unordered_list,
)


def markdown_to_blocks(markdown: str) -> list[BlockNode]:
    """
    Given markdown text create a list of markdown blocks.

    Parameters:
        - markdown (str): The markdown text to parse for block extraction.

    Returns:
        - list[BlockNoe]: A list of all the blocks with markdown text.
    """
    node = BlockNode(markdown, "paragraph")
    nodes = split_blocks_code([node])
    nodes = split_blocks_unordered_list(nodes)
    nodes = split_blocks_quote(nodes)
    nodes = split_blocks_ordered_list(nodes)
    nodes = split_blocks_heading(nodes)
    return nodes
