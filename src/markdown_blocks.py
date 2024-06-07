from util import (
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)


class BlockNode:
    def __init__(self, block_text: str, block_type: str):
        self.block_text = block_text
        self.block_type = block_type

    def __eq__(self, other: object) -> bool:
        """
        Compare two BlockNode objects for equality.

        Args:
            other (BlockNode): The BlockNode object to compare with.

        Returns:
            bool: True if the two BlockNode object attributes are equal. False
            otherwise.
        """
        if not isinstance(other, BlockNode):
            return False
        return (
            self.block_text == other.block_text and self.block_type == other.block_type
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of the BlockNode object.

        The returned string includes the block_text and block_type.

        Returns:
            str: A string representation of the BlockNode object.
        """
        return f"BlockNode({self.block_text}, {self.block_type})"


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


# block_type_paragraph = "paragraph"
# block_type_heading = "heading"
# block_type_code = "code"
# block_type_quote = "quote"
# block_type_unordered_list = "unordered_list"
# block_type_ordered_list = "ordered_list"


def split_blocks_heading(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError


def split_blocks_code(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError


def split_blocks_quote(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError


def split_blocks_unordered_list(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError


def split_blocks_ordered_list(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError
