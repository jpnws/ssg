import unittest

from block.markdown_to_blocks import markdown_to_blocks


class TestMarkdownBlocks(unittest.TestCase):
    #     def test_markdown_to_blocks(self):
    #         # Arrange
    #         text = """

    # This is **bolded** paragraph

    # This is another paragraph with *italic* text and `code` here
    # This is the same paragraph on a new line

    # * This is a list
    # * with items

    # """
    #         expected = [
    #             "This is **bolded** paragraph",
    #             "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
    #             "* This is a list\n* with items",
    #         ]
    #         # Act
    #         actual = markdown_to_blocks(text)
    #         # Assert
    #         self.assertListEqual(actual, expected)

    def test_markdown_code_block(self):
        # Arrange
        text = """

This is **bolded** paragraph

```python


def func1(arg):
    pass
```

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items

```python


def func2(arg):
    pass

def func3(arg):
    pass
```

> This is a quote
> with greater than symbol.

## This is a heading

An ordered list:
1. One
2. Two
3. Three


        """
        expected = [
            "```python\ndef func(arg):\n    pass\n```",
        ]
        # Act
        actual = markdown_to_blocks(text)
        print(actual)
        # Assert
        self.assertListEqual(actual, expected)
