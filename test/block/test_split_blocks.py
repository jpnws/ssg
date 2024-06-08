import unittest

from block.block_node import BlockNode
from block.heading_node import HeadingNode
from block.code_node import CodeNode

from block.split_blocks import split_blocks_heading
from block.split_blocks import split_blocks_code


class TestSplitBlocks(unittest.TestCase):
    def test_split_blocks_heading(self):
        # Arrange
        node = BlockNode(
            """
        ABC

        # Heading 1

        ABC

        ## Heading 2

        ABC

        ### Heading 3

        ABC

        #### Heading 4

        ABC

        ##### Heading 5

        ABC

        ###### Heading 6

        ABC
        """,
            "paragraph",
        )
        # Act
        actual = split_blocks_heading([node])
        expected: list[BlockNode] = [
            BlockNode("ABC", "paragraph"),
            HeadingNode("Heading 1", "heading", 1),
            BlockNode("ABC", "paragraph"),
            HeadingNode("Heading 2", "heading", 2),
            BlockNode("ABC", "paragraph"),
            HeadingNode("Heading 3", "heading", 3),
            BlockNode("ABC", "paragraph"),
            HeadingNode("Heading 4", "heading", 4),
            BlockNode("ABC", "paragraph"),
            HeadingNode("Heading 5", "heading", 5),
            BlockNode("ABC", "paragraph"),
            HeadingNode("Heading 6", "heading", 6),
            BlockNode("ABC", "paragraph"),
        ]
        # Assert
        self.assertListEqual(actual, expected)

    def test_split_blocks_code(self):
        # Arrange
        node = BlockNode(
            """
        ABC
```python
# comment
def func():
    pass
```
        ABC
        """,
            "paragraph",
        )
        # Act
        actual = split_blocks_code([node])
        expected = [
            BlockNode("ABC", "paragraph"),
            CodeNode("# comment\ndef func():\n    pass\n", "code", "python"),
            BlockNode("ABC", "paragraph"),
        ]
        # Assert
        self.assertListEqual(actual, expected)
