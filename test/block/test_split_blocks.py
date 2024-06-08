import pprint
import unittest

from block.block_node import BlockNode
from block.code_block import CodeBlock
from block.heading_block import HeadingBlock
from block.split_blocks import (
    split_blocks_code,
    split_blocks_heading,
    split_blocks_ordered_list,
    split_blocks_quote,
    split_blocks_unordered_list,
)


class TestSplitBlocks(unittest.TestCase):
    def test_split_blocks_heading(self):
        """
        Test that the split_blocks_heading function correctly serializes the
        heading blocks from a markdown string.
        """
        # Arrange
        node = BlockNode(
            "ABC\n\n# Heading 1\n\nABC\n\n## Heading 2\n\nABC\n\n### Heading 3\n\nABC\n\n#### Heading 4\n\nABC\n\n##### Heading 5\n\nABC\n\n###### Heading 6\n\nABC",
            "paragraph",
        )
        # Act
        actual = split_blocks_heading([node])
        expected: list[BlockNode] = [
            BlockNode("ABC", "paragraph"),
            BlockNode("", "newline"),
            HeadingBlock("Heading 1", "heading", 1),
            BlockNode("", "newline"),
            BlockNode("ABC", "paragraph"),
            BlockNode("", "newline"),
            HeadingBlock("Heading 2", "heading", 2),
            BlockNode("", "newline"),
            BlockNode("ABC", "paragraph"),
            BlockNode("", "newline"),
            HeadingBlock("Heading 3", "heading", 3),
            BlockNode("", "newline"),
            BlockNode("ABC", "paragraph"),
            BlockNode("", "newline"),
            HeadingBlock("Heading 4", "heading", 4),
            BlockNode("", "newline"),
            BlockNode("ABC", "paragraph"),
            BlockNode("", "newline"),
            HeadingBlock("Heading 5", "heading", 5),
            BlockNode("", "newline"),
            BlockNode("ABC", "paragraph"),
            BlockNode("", "newline"),
            HeadingBlock("Heading 6", "heading", 6),
            BlockNode("", "newline"),
            BlockNode("ABC", "paragraph"),
        ]
        # Assert
        self.assertListEqual(actual, expected)

    def test_split_blocks_code(self):
        """
        Test that the split_blocks_code function correctly serializes the code
        blocks from a markdown string.
        """
        # Arrange
        node = BlockNode(
            "ABC\n\n```python\n# comment\ndef func():\n    pass\n```\nABC",
            "paragraph",
        )
        # Act
        actual = split_blocks_code([node])
        expected = [
            BlockNode("ABC", "paragraph"),
            BlockNode("", "newline"),
            CodeBlock("# comment\ndef func():\n    pass\n", "code", "python"),
            BlockNode("ABC", "paragraph"),
        ]
        # Assert
        self.assertListEqual(actual, expected)

    def test_split_blocks_quote(self):
        """
        Test that the split_blocks_quote function correctly serializes the quote
        blocks from a markdown string.
        """
        # Arrange
        node = BlockNode(
            "ABC\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n> Morbi quis interdum nunc. Aenean rutrum pretium eros, non placerat est rhoncus ultricies.\n> In sagittis consectetur tristique. Sed porttitor mi magna.\n\n> Vivamus nec auctor quam. In mauris mauris, sagittis quis dignissim.\n> Etiam tempus tellus nec elementum sagittis. Phasellus ullamcorper risus elit, eget blandit diam cursus ut.\n> Suspendisse eu sem risus.\n\nABC",
            "paragraph",
        )
        # Act
        actual = split_blocks_quote([node])
        expected = [
            BlockNode("ABC", "paragraph"),
            BlockNode("", "newline"),
            BlockNode(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nMorbi quis interdum nunc. Aenean rutrum pretium eros, non placerat est rhoncus ultricies.\nIn sagittis consectetur tristique. Sed porttitor mi magna.\n",
                "quote",
            ),
            BlockNode("", "newline"),
            BlockNode(
                "Vivamus nec auctor quam. In mauris mauris, sagittis quis dignissim.\nEtiam tempus tellus nec elementum sagittis. Phasellus ullamcorper risus elit, eget blandit diam cursus ut.\nSuspendisse eu sem risus.\n",
                "quote",
            ),
            BlockNode("", "newline"),
            BlockNode("ABC", "paragraph"),
        ]
        # Assert
        self.assertListEqual(actual, expected)

    def test_split_blocks_unordered_list(self):
        """
        Test that the split_blocks_unordered_list function correctly serializes
        the unordered list blocks from a markdown string.
        """
        # Arrange
        node = BlockNode(
            "ABC\n\n* List item 1 (block1)\n* List item 2 (block1)\n\n* List item 1 (block2)\n* List item 2 (block2)\n\nABC",
            "paragraph",
        )
        # Act
        actual = split_blocks_unordered_list([node])
        expected = [
            BlockNode("ABC", "paragraph"),
            BlockNode("", "newline"),
            BlockNode("List item 1 (block1)\nList item 2 (block1)\n", "unordered_list"),
            BlockNode("", "newline"),
            BlockNode("List item 1 (block2)\nList item 2 (block2)\n", "unordered_list"),
            BlockNode("", "newline"),
            BlockNode("ABC", "paragraph"),
        ]
        # Assert
        self.assertListEqual(actual, expected)

    def test_split_blocks_ordered_list(self):
        """
        Test that the split_blocks_ordered_list function correctly serializes
        the ordered list blocks from a markdown string.
        """
        # Arrange
        node = BlockNode(
            "ABC\n\n1. List item 1 (block1)\n2. List item 2 (block1)\n\n1. List item 1 (block2)\n2. List item 2 (block2)\n\nABC",
            "paragraph",
        )
        # Act
        actual = split_blocks_ordered_list([node])
        expected = [
            BlockNode("ABC", "paragraph"),
            BlockNode("", "newline"),
            BlockNode("List item 1 (block1)\nList item 2 (block1)\n", "ordered_list"),
            BlockNode("", "newline"),
            BlockNode("List item 1 (block2)\nList item 2 (block2)\n", "ordered_list"),
            BlockNode("", "newline"),
            BlockNode("ABC", "paragraph"),
        ]
        # Assert
        self.assertListEqual(actual, expected)

    def test_split_blocks_combo(self):
        """
        Test that the split bocks functions all work together to correctly parse
        heading, code, quote, unordered list, and ordered list blocks.
        """
        # Arrange
        node = BlockNode(
            "ABC\n\n# Heading 1\n\nABC\n\n```python\n# comment\ndef func():\n    pass\n```\n\nABC\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n> Morbi quis interdum nunc. Aenean rutrum pretium eros, non placerat est rhoncus ultricies.\n> In sagittis consectetur tristique. Sed porttitor mi magna.",
            "paragraph",
        )
        # Act
        actual = split_blocks_code([node])
        actual = split_blocks_heading(actual)
        pprint.pp(actual)
        actual = split_blocks_quote(actual)
        # actual = split_blocks_unordered_list(actual)
        # actual = split_blocks_ordered_list(actual)

        expected = [
            BlockNode("ABC", "paragraph"),
            BlockNode("", "newline"),
            HeadingBlock("Heading 1", "heading", 1),
            BlockNode("", "newline"),
            BlockNode("ABC", "paragraph"),
            BlockNode("", "newline"),
            CodeBlock("# comment\ndef func():\n    pass\n", "code", "python"),
            BlockNode("", "newline"),
            BlockNode("ABC", "paragraph"),
            BlockNode("", "newline"),
            BlockNode(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nMorbi quis interdum nunc. Aenean rutrum pretium eros, non placerat est rhoncus ultricies.\nIn sagittis consectetur tristique. Sed porttitor mi magna.\n",
                "quote",
            ),
        ]
        # Assert
        self.assertListEqual(actual, expected)
