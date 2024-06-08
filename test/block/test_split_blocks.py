import unittest

from block.block_node import BlockNode
from block.heading_block import HeadingBlock
from block.code_block import CodeBlock

from block.split_blocks import split_blocks_heading
from block.split_blocks import split_blocks_code
from block.split_blocks import split_blocks_quote


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
            HeadingBlock("Heading 1", "heading", 1),
            BlockNode("ABC", "paragraph"),
            HeadingBlock("Heading 2", "heading", 2),
            BlockNode("ABC", "paragraph"),
            HeadingBlock("Heading 3", "heading", 3),
            BlockNode("ABC", "paragraph"),
            HeadingBlock("Heading 4", "heading", 4),
            BlockNode("ABC", "paragraph"),
            HeadingBlock("Heading 5", "heading", 5),
            BlockNode("ABC", "paragraph"),
            HeadingBlock("Heading 6", "heading", 6),
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
            CodeBlock("# comment\ndef func():\n    pass\n", "code", "python"),
            BlockNode("ABC", "paragraph"),
        ]
        # Assert
        self.assertListEqual(actual, expected)

    def test_split_blocks_quote(self):
        # Arrange
        node = BlockNode(
            """
ABC

> Lorem ipsum dolor sit amet, consectetur adipiscing elit.
> Morbi quis interdum nunc. Aenean rutrum pretium eros, non placerat est rhoncus ultricies.
> In sagittis consectetur tristique. Sed porttitor mi magna.

> Vivamus nec auctor quam. In mauris mauris, sagittis quis dignissim.
> Etiam tempus tellus nec elementum sagittis. Phasellus ullamcorper risus elit, eget blandit diam cursus ut.
> Suspendisse eu sem risus.

ABC
""",
            "paragraph",
        )
        # Act
        actual = split_blocks_quote([node])
        expected = [
            BlockNode("", "newline"),
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
