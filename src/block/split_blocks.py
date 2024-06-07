from block.block_node import BlockNode
from block.heading_block import HeadingBlock
from block.code_block import CodeBlock


def split_blocks_heading(blocks: list[HeadingBlock]) -> list[HeadingBlock]:
    raise NotImplementedError


def split_blocks_code(blocks: list[CodeBlock]) -> list[CodeBlock]:
    raise NotImplementedError


def split_blocks_quote(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError


def split_blocks_unordered_list(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError


def split_blocks_ordered_list(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError
