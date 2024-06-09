import unittest

from block.block_node import BlockNode
from block.code_block import CodeBlock
from block.heading_block import HeadingBlock
from block.markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        # Arrange / Act
        actual = markdown_to_blocks(
            "ABC\n\n# Heading 1\n\nABC\n\n```python\n# comment\ndef func():\n    pass\n```\n\nABC\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n> Morbi quis interdum nunc. Aenean rutrum pretium eros, non placerat est rhoncus ultricies.\n> In sagittis consectetur tristique. Sed porttitor mi magna.\n\nABC\n\n* List item 1 (block1)\n- List item 2 (block1)\n\n- List item 1 (block2)\n* List item 2 (block2)\n\nABC\n\nABC\n\n1. List item 1 (block1)\n2. List item 2 (block1)\n\n1. List item 1 (block2)\n2. List item 2 (block2)\n\nABC"
        )
        # Act
        expected = [
            BlockNode("ABC\n", "paragraph"),
            BlockNode("", "newline"),
            HeadingBlock("Heading 1\n", "heading", 1),
            BlockNode("", "newline"),
            BlockNode("ABC\n", "paragraph"),
            BlockNode("", "newline"),
            CodeBlock("# comment\ndef func():\n    pass\n", "code", "python"),
            BlockNode("", "newline"),
            BlockNode("ABC\n", "paragraph"),
            BlockNode("", "newline"),
            BlockNode(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nMorbi quis interdum nunc. Aenean rutrum pretium eros, non placerat est rhoncus ultricies.\nIn sagittis consectetur tristique. Sed porttitor mi magna.\n",
                "quote",
            ),
            BlockNode("", "newline"),
            BlockNode("ABC\n", "paragraph"),
            BlockNode("", "newline"),
            BlockNode("List item 1 (block1)\nList item 2 (block1)\n", "unordered_list"),
            BlockNode("", "newline"),
            BlockNode("List item 1 (block2)\nList item 2 (block2)\n", "unordered_list"),
            BlockNode("", "newline"),
            BlockNode("ABC\n", "paragraph"),
            BlockNode("", "newline"),
            BlockNode("ABC\n", "paragraph"),
            BlockNode("", "newline"),
            BlockNode("List item 1 (block1)\nList item 2 (block1)\n", "ordered_list"),
            BlockNode("", "newline"),
            BlockNode("List item 1 (block2)\nList item 2 (block2)\n", "ordered_list"),
            BlockNode("", "newline"),
            BlockNode("ABC\n", "paragraph"),
        ]
        # Assert
        self.assertListEqual(actual, expected)
