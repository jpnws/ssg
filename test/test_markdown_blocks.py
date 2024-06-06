import unittest

from markdown_blocks import markdown_to_blocks


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        # Arrange
        text = """


This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items


"""
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
        ]
        # Act
        actual = markdown_to_blocks(text)
        # Assert
        self.assertListEqual(actual, expected)

    def test_markdown_code_block(self):
        # Arrange
        text = """
```python


def func(arg):
    pass
```
        """
        expected = [
            "```python\ndef func(arg):\n    pass\n```",
        ]
        # Act
        actual = markdown_to_blocks(text)
        print(actual)
        # Assert
        self.assertListEqual(actual, expected)
