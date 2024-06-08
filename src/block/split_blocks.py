from block.block_node import BlockNode
from block.code_block import CodeBlock
from block.heading_block import HeadingBlock
from util import block_type_newline, block_type_paragraph, block_type_quote


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
    for block in blocks:
        # Skip if we are not at a block with paragraph type. Let the block
        # through to the nodes list.
        if block.block_type != block_type_paragraph:
            nodes.append(block)
            continue
        language = ""
        code_segment = ""
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
                if code_segment:
                    nodes.append(BlockNode(code_segment, block_type_quote))
                    code_segment = ""
                    opening_found = False
                nodes.append(BlockNode("", block_type_newline))
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
        # Skip if we are not at a block with paragraph type. Let the block
        # through to the nodes list.
        if block.block_type != block_type_paragraph:
            nodes.append(block)
            continue
        paragraph_segment = ""
        quote_segment = ""
        quote_started = False
        split_block_text = block.block_text.splitlines()
        for line in split_block_text:
            line = line.strip()
            if not line:
                # If the current line is an empty string, then that means that
                # we have a newline markdown block separator here. This could
                # have come after a paragraph or quote segment, if so, then
                # create the block nodes for them, and then continue to create
                # the newline separator block node.
                if paragraph_segment:
                    nodes.append(BlockNode(paragraph_segment, block_type_paragraph))
                    paragraph_segment = ""
                if quote_segment:
                    nodes.append(BlockNode(quote_segment, block_type_quote))
                    quote_segment = ""
                    quote_started = False
                nodes.append(BlockNode("", block_type_newline))
            if not line.startswith(">") and not quote_started:
                # Handle a non-quote line where there was no quote block that
                # was parsed previously.
                paragraph_segment += line
            if not line.startswith(">") and quote_started:
                # Handle a non-quote line where there was a quote block being
                # parsed previously.
                nodes.append(BlockNode(quote_segment, block_type_quote))
                quote_segment = ""
                quote_started = False
            if line.startswith(">"):
                if not quote_started:
                    # Suppose that the quote was not started yet. First, there
                    # could've been a paragraph segement previously, so check
                    # for that and handle it accordingly.
                    if paragraph_segment:
                        nodes.append(
                            BlockNode(f"{paragraph_segment}", block_type_paragraph)
                        )
                        paragraph_segment = ""
                    # Flag that the quote block has now started since it was not
                    # started previously.
                    quote_started = True
                # Suppose that the current line has a quote symbol, then
                # concatenate the line to the quote segment variable.
                quote_segment += f"{line.lstrip("> ")}\n"
        # Lastly, the text processing ends at the very last quote segment, but
        # there could've been paragraph segments following it; therefore, check
        # for it handle it accordingly.
        if paragraph_segment:
            nodes.append(BlockNode(f"{paragraph_segment}", block_type_paragraph))
    return nodes


def split_blocks_unordered_list(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError


def split_blocks_ordered_list(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError
