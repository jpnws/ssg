from block.block_node import BlockNode
from block.heading_node import HeadingNode
from block.code_node import CodeNode


def split_blocks_heading(blocks: list[BlockNode]) -> list[BlockNode]:
    nodes: list[BlockNode] = []
    for block in blocks:
        if isinstance(block, CodeNode):
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
                nodes.append(HeadingNode(block_text, "heading", 6))
            elif line.startswith("#####"):
                block_text = line.split("#####")[-1].strip()
                nodes.append(HeadingNode(block_text, "heading", 5))
            elif line.startswith("####"):
                block_text = line.split("####")[-1].strip()
                nodes.append(HeadingNode(block_text, "heading", 4))
            elif line.startswith("###"):
                block_text = line.split("###")[-1].strip()
                nodes.append(HeadingNode(block_text, "heading", 3))
            elif line.startswith("##"):
                block_text = line.split("##")[-1].strip()
                nodes.append(HeadingNode(block_text, "heading", 2))
            elif line.startswith("#"):
                block_text = line.split("#")[-1].strip()
                nodes.append(HeadingNode(block_text, "heading", 1))
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
                nodes.append(CodeNode(code_segment, "code", language))
                code_segment = ""
                language = ""
                continue
            code_segment += f"{line}\n"
        if paragraph_segment:
            nodes.append(BlockNode(paragraph_segment.strip(), "paragraph"))
    return nodes


def split_blocks_quote(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError


def split_blocks_unordered_list(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError


def split_blocks_ordered_list(blocks: list[BlockNode]) -> list[BlockNode]:
    raise NotImplementedError
