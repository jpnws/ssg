from block.block_node import BlockNode
from block.code_block import CodeBlock
from block.heading_block import HeadingBlock
from html_node import HTMLNode
from inline.text_node_to_leaf_node import text_node_to_leaf_node
from inline.text_to_text_nodes import text_to_text_nodes
from leaf_node import LeafNode
from parent_node import ParentNode
from util import (
    block_type_code,
    block_type_heading,
    block_type_ordered_list,
    block_type_paragraph,
    block_type_quote,
    block_type_unordered_list,
)


def block_nodes_to_html_nodes(block_nodes: list[BlockNode]) -> list[HTMLNode]:
    raise NotImplementedError


def heading_block_to_html_node(heading_block: HeadingBlock) -> HTMLNode:
    if heading_block.block_type != block_type_heading:
        raise ValueError("Invalid block type: must be a heading block.")
    html_tag = f"h{heading_block.block_level}"
    text_nodes = text_to_text_nodes(heading_block.block_text)
    leaf_nodes: list[HTMLNode] = []
    for text_node in text_nodes:
        leaf_node = text_node_to_leaf_node(text_node)
        leaf_nodes.append(leaf_node)
    return ParentNode(html_tag, leaf_nodes)


def code_block_to_html_node(code_block: CodeBlock) -> HTMLNode:
    if code_block.block_type != block_type_code:
        raise ValueError("Invalid block type: must be a code block.")
    return ParentNode("pre", [LeafNode("code", code_block.block_text)])


def quote_block_to_html_node(block_node: BlockNode) -> HTMLNode:
    if block_node.block_type != block_type_quote:
        raise ValueError("Invalid block type: must be a quote block.")
    text_nodes = text_to_text_nodes(block_node.block_text)
    leaf_nodes: list[HTMLNode] = []
    for text_node in text_nodes:
        leaf_node = text_node_to_leaf_node(text_node)
        leaf_nodes.append(leaf_node)
    return ParentNode("blockquote", leaf_nodes)


def unordered_list_block_to_html_node(block_node: BlockNode) -> HTMLNode:
    if block_node.block_type != block_type_unordered_list:
        raise ValueError("Invalid block type: must be an unordered list block.")
    parent_nodes: list[HTMLNode] = []
    for line in block_node.block_text.splitlines():
        text_nodes = text_to_text_nodes(line)
        leaf_nodes: list[HTMLNode] = []
        for text_node in text_nodes:
            leaf_node = text_node_to_leaf_node(text_node)
            leaf_nodes.append(leaf_node)
        parent_nodes.append(ParentNode("li", leaf_nodes))
    return ParentNode("ul", parent_nodes)


def ordered_list_block_to_html_node(block_node: BlockNode) -> HTMLNode:
    if block_node.block_type != block_type_ordered_list:
        raise ValueError("Invalid block type: must be an ordered list block.")
    parent_nodes: list[HTMLNode] = []
    for line in block_node.block_text.splitlines():
        text_nodes = text_to_text_nodes(line)
        leaf_nodes: list[HTMLNode] = []
        for text_node in text_nodes:
            leaf_node = text_node_to_leaf_node(text_node)
            leaf_nodes.append(leaf_node)
        parent_nodes.append(ParentNode("li", leaf_nodes))
    return ParentNode("ol", parent_nodes)


def paragraph_block_to_html_node(block_node: BlockNode) -> HTMLNode:
    if block_node.block_type != block_type_paragraph:
        raise ValueError("Invalid block type: must be a paragraph block.")
    text_nodes = text_to_text_nodes(block_node.block_text)
    leaf_nodes: list[HTMLNode] = []
    for text_node in text_nodes:
        leaf_node = text_node_to_leaf_node(text_node)
        leaf_nodes.append(leaf_node)
    return ParentNode("p", leaf_nodes)
