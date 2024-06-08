import re

from block.block_node import BlockNode
from block.code_block import CodeBlock
from block.heading_block import HeadingBlock
from util import (
    block_type_code,
    block_type_heading,
    block_type_newline,
    block_type_ordered_list,
    block_type_paragraph,
    block_type_quote,
    block_type_unordered_list,
)


def split_blocks_heading(blocks: list[BlockNode]) -> list[BlockNode]:
    nodes: list[BlockNode] = []
    for block in blocks:
        # Skip if we are not at a block with paragraph type. Let the block
        # through to the nodes list.
        if block.block_type != block_type_paragraph:
            nodes.append(block)
            continue
        for line in block.block_text.splitlines():
            line = line.strip()
            if not line:
                nodes.append(BlockNode("", block_type_newline))
            elif "#" not in line:
                nodes.append(BlockNode(line, "paragraph"))
            elif line.startswith("###### "):
                block_text = line.split("###### ")[-1].strip()
                nodes.append(HeadingBlock(block_text, block_type_heading, 6))
            elif line.startswith("##### "):
                block_text = line.split("##### ")[-1].strip()
                nodes.append(HeadingBlock(block_text, block_type_heading, 5))
            elif line.startswith("#### "):
                block_text = line.split("#### ")[-1].strip()
                nodes.append(HeadingBlock(block_text, block_type_heading, 4))
            elif line.startswith("### "):
                block_text = line.split("### ")[-1].strip()
                nodes.append(HeadingBlock(block_text, block_type_heading, 3))
            elif line.startswith("## "):
                block_text = line.split("## ")[-1].strip()
                nodes.append(HeadingBlock(block_text, block_type_heading, 2))
            elif line.startswith("# "):
                block_text = line.split("# ")[-1].strip()
                nodes.append(HeadingBlock(block_text, block_type_heading, 1))
    return nodes


def split_blocks_code(blocks: list[BlockNode]) -> list[BlockNode]:
    nodes: list[BlockNode] = []
    for block in blocks:
        # Skip if we are not at a block with paragraph type. Let the block
        # through to the nodes list.
        if block.block_type != block_type_paragraph:
            nodes.append(block)
            continue
        language = ""
        block_segment = ""
        paragraph_segment = ""
        opening_found = False
        for line in block.block_text.splitlines():
            if not line:
                # If the current line is an empty string, then that means that
                # we have a newline markdown block separator here. This could
                # have come after a paragraph or quote segment, if so, then
                # create the block nodes for them, and then continue to create
                # the newline separator block node.
                if paragraph_segment:
                    nodes.append(BlockNode(paragraph_segment, block_type_paragraph))
                    paragraph_segment = ""
                if block_segment:
                    nodes.append(BlockNode(block_segment, block_type_quote))
                    block_segment = ""
                    opening_found = False
                nodes.append(BlockNode("", block_type_newline))
                continue
            if "```" not in line and not opening_found:
                paragraph_segment += f"{line}\n"
                continue
            if "```" in line and not opening_found:
                language = line.split("```")[-1]
                if paragraph_segment:
                    nodes.append(BlockNode(paragraph_segment, block_type_paragraph))
                opening_found = True
                paragraph_segment = ""
                continue
            if "```" in line and opening_found:
                opening_found = False
                nodes.append(CodeBlock(block_segment, block_type_code, language))
                block_segment = ""
                language = ""
                continue
            block_segment += f"{line}\n"
        if paragraph_segment:
            nodes.append(BlockNode(paragraph_segment, block_type_paragraph))
    return nodes


def split_blocks_quote(blocks: list[BlockNode]) -> list[BlockNode]:
    nodes: list[BlockNode] = []
    for block in blocks:
        if block.block_type != block_type_paragraph:
            nodes.append(block)
            continue
        paragraph_segment = ""
        block_segment = ""
        block_started = False
        for line in block.block_text.splitlines():
            print(repr(line))
            line = line.strip()
            if not line:
                if paragraph_segment:
                    nodes.append(BlockNode(paragraph_segment, block_type_paragraph))
                    paragraph_segment = ""
                if block_segment:
                    nodes.append(BlockNode(block_segment, block_type_quote))
                    block_segment = ""
                    block_started = False
                nodes.append(BlockNode("", block_type_newline))
            if not line.startswith("> ") and not block_started:
                paragraph_segment += line
            if not line.startswith("> ") and block_started:
                nodes.append(BlockNode(block_segment, block_type_quote))
                block_segment = ""
                block_started = False
            if line.startswith("> "):
                if not block_started:
                    if paragraph_segment:
                        nodes.append(BlockNode(paragraph_segment, block_type_paragraph))
                        paragraph_segment = ""
                    block_started = True
                block_segment += f"{line.lstrip("> ")}\n"
        if paragraph_segment:
            nodes.append(BlockNode(paragraph_segment, block_type_paragraph))
    return nodes


def split_blocks_unordered_list(blocks: list[BlockNode]) -> list[BlockNode]:
    nodes: list[BlockNode] = []
    for block in blocks:
        if block.block_type != block_type_paragraph:
            nodes.append(block)
            continue
        paragraph_segment = ""
        block_segment = ""
        block_started = False
        for line in block.block_text.splitlines():
            line = line.strip()
            if not line:
                if paragraph_segment:
                    nodes.append(BlockNode(paragraph_segment, block_type_paragraph))
                    paragraph_segment = ""
                if block_segment:
                    nodes.append(BlockNode(block_segment, block_type_unordered_list))
                    block_segment = ""
                    block_started = False
                nodes.append(BlockNode("", block_type_newline))
            if not line.startswith("* ") and not block_started:
                paragraph_segment += line
            if not line.startswith("* ") and block_started:
                nodes.append(BlockNode(block_segment, block_type_unordered_list))
                block_segment = ""
                block_started = False
            if line.startswith("* "):
                if not block_started:
                    if paragraph_segment:
                        nodes.append(BlockNode(paragraph_segment, block_type_paragraph))
                        paragraph_segment = ""
                    block_started = True
                block_segment += f"{line.lstrip("* ")}\n"
        if paragraph_segment:
            nodes.append(BlockNode(paragraph_segment, block_type_paragraph))
    return nodes


def split_blocks_ordered_list(blocks: list[BlockNode]) -> list[BlockNode]:
    nodes: list[BlockNode] = []
    for block in blocks:
        if block.block_type != block_type_paragraph:
            nodes.append(block)
            continue
        paragraph_segment = ""
        block_segment = ""
        block_started = False
        for line in block.block_text.splitlines():
            line = line.strip()
            if not line:
                if paragraph_segment:
                    nodes.append(BlockNode(paragraph_segment, block_type_paragraph))
                    paragraph_segment = ""
                if block_segment:
                    nodes.append(BlockNode(block_segment, block_type_ordered_list))
                    block_segment = ""
                    block_started = False
                nodes.append(BlockNode("", block_type_newline))
            if not re.match(r"^\d+\.\s", line) and not block_started:
                paragraph_segment += line
            if not re.match(r"^\d+\.\s", line) and block_started:
                nodes.append(BlockNode(block_segment, block_type_ordered_list))
                block_segment = ""
                block_started = False
            if re.match(r"^\d+\.\s", line):
                if not block_started:
                    if paragraph_segment:
                        nodes.append(BlockNode(paragraph_segment, block_type_paragraph))
                        paragraph_segment = ""
                    block_started = True
                block_segment += f"{re.sub(r"^\d+\.\s", "", line)}\n"
        if paragraph_segment:
            nodes.append(BlockNode(paragraph_segment, block_type_paragraph))
    return nodes
