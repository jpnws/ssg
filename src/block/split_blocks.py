from block.block_node import BlockNode


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
