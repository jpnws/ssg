from block.block_node import BlockNode
from html_node import HTMLNode


def block_nodes_to_html_nodes(block_nodes: list[BlockNode]) -> list[HTMLNode]:
    raise NotImplementedError


def heading_block_to_html_node(block_node: BlockNode) -> HTMLNode:
    raise NotImplementedError


def code_block_to_html_node(block_node: BlockNode) -> HTMLNode:
    raise NotImplementedError


def quote_block_to_html_node(block_node: BlockNode) -> HTMLNode:
    raise NotImplementedError


def unordered_list_block_to_html_node(block_node: BlockNode) -> HTMLNode:
    raise NotImplementedError


def ordered_list_block_to_html_node(block_node: BlockNode) -> HTMLNode:
    raise NotImplementedError
