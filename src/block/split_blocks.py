from util import block_type_newline, block_type_quote, block_type_paragraph

from block.block_node import BlockNode
from block.heading_block import HeadingBlock
from block.code_block import CodeBlock


def split_blocks_heading(blocks: list[BlockNode]) -> list[BlockNode]:
    nodes: list[BlockNode] = []
    for block in blocks:
        if isinstance(block, CodeBlock):
            nodes.append(block)
            continue
        for line in block.block_text.splitlines():
            line = line.strip()
            if not line:
                continue
            elif "#" not in line:
                nodes.append(BlockNode(line, "paragraph"))
                continue
            elif line.startswith("######"):
                block_text = line.split("######")[-1].strip()
                nodes.append(HeadingBlock(block_text, "heading", 6))
            elif line.startswith("#####"):
                block_text = line.split("#####")[-1].strip()
                nodes.append(HeadingBlock(block_text, "heading", 5))
            elif line.startswith("####"):
                block_text = line.split("####")[-1].strip()
                nodes.append(HeadingBlock(block_text, "heading", 4))
            elif line.startswith("###"):
                block_text = line.split("###")[-1].strip()
                nodes.append(HeadingBlock(block_text, "heading", 3))
            elif line.startswith("##"):
                block_text = line.split("##")[-1].strip()
                nodes.append(HeadingBlock(block_text, "heading", 2))
            elif line.startswith("#"):
                block_text = line.split("#")[-1].strip()
                nodes.append(HeadingBlock(block_text, "heading", 1))
    return nodes


def split_blocks_code(blocks: list[BlockNode]) -> list[BlockNode]:
    nodes: list[BlockNode] = []
    opening_found = False
    for block in blocks:
        language = ""
        code_segment = ""
        paragraph_segment = ""
        for line in block.block_text.splitlines():
            if not line:
                continue
            if "```" not in line and not opening_found:
                paragraph_segment += line
                continue
            if "```" in line and not opening_found:
                language = line.split("```")[-1]
                if paragraph_segment:
                    nodes.append(BlockNode(paragraph_segment.strip(), "paragraph"))
                opening_found = True
                paragraph_segment = ""
                continue
            if "```" in line and opening_found:
                opening_found = False
                nodes.append(CodeBlock(code_segment, "code", language))
                code_segment = ""
                language = ""
                continue
            code_segment += f"{line}\n"
        if paragraph_segment:
            nodes.append(BlockNode(paragraph_segment.strip(), "paragraph"))
    return nodes


def split_blocks_quote(blocks: list[BlockNode]) -> list[BlockNode]:
    nodes: list[BlockNode] = []
    for block in blocks:
        paragraph_segment = ""
        quote_segment = ""
        quote_started = False
        # Skip if we are not at a block with paragraph type. Let the block
        # through to the nodes list.
        if block.block_type != block_type_paragraph:
            nodes.append(block)
            continue
        split_block_text = block.block_text.splitlines()
        print(split_block_text)
        for line in split_block_text:
            line = line.strip()
            # Create a newline block separator for empty lines.
            if not line:
                nodes.append(BlockNode("", block_type_newline))
                continue
            # Handle a non-quote line where there was no quote block that was
            # parsed previously.
            if not line.startswith(">") and not quote_started:
                paragraph_segment += f"{line}\n"
                continue
            # Handle a non-quote line where there was a quote block being parsed
            # previously.
            if not line.startswith(">") and quote_started:
                nodes.append(BlockNode(f"{quote_segment}\n", block_type_quote))
                quote_segment = ""
                quote_started = False
                continue
            # Handle a quote line here as long as it is not started.
            if line.startswith(">"):
                quote_segment += f"{line}\n"
                if not quote_started:
                    if paragraph_segment:
                        nodes.append(
                            BlockNode(f"{paragraph_segment}\n", block_type_paragraph)
                        )
                    quote_started = True
                continue
    return nodes


def split_blocks_unordered_list(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError


def split_blocks_ordered_list(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError
