import unittest

from nodes_delimiter import split_nodes_delimiter

from textnode import TextNode


class TestUtil(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        """
        Test splitting a TextNode into multiple TextNodes by code delimiter.
        """
        # Arrange
        node = TextNode("This is text with a `code block` word", "text")
        # Act
        actual_nodes = split_nodes_delimiter([node], "`", "code")
        expected_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text"),
        ]
        # Assert
        self.assertListEqual(actual_nodes, expected_nodes)

    def test_split_nodes_delimiter_italic(self):
        """
        Test splitting a TextNode into multiple TextNodes by italic delimiter.
        """
        # Arrange
        node = TextNode("This is a text with a *italic* word", "text")
        # Act
        actual_nodes = split_nodes_delimiter([node], "*", "italic")
        expected_nodes = [
            TextNode("This is a text with a ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word", "text"),
        ]
        # Assert
        self.assertListEqual(actual_nodes, expected_nodes)

    def test_split_nodes_delimiter_bold(self):
        """
        Test splitting a TextNode into multiple TextNodes by bold delimiter.
        """
        # Arrange
        node = TextNode("This is a text with a **bold** word", "text")
        # Act
        actual_nodes = split_nodes_delimiter([node], "**", "bold")
        expected_nodes = [
            TextNode("This is a text with a ", "text"),
            TextNode("bold", "bold"),
            TextNode(" word", "text"),
        ]
        # Assert
        self.assertListEqual(actual_nodes, expected_nodes)

    def test_split_nodes_delimiter_at_end_of_text_string(self):
        """
        Test splitting a TextNode into multiple TextNodes by a delimiter,
        where the delimiter text segment is at the end of the text string.
        """
        # Arrange
        node = TextNode("This text is **bold**", "text")
        # Act
        actual_nodes = split_nodes_delimiter([node], "**", "bold")
        expected_nodes = [
            TextNode("This text is ", "text"),
            TextNode("bold", "bold"),
        ]
        # Assert
        self.assertListEqual(actual_nodes, expected_nodes)

    def test_split_nodes_delimiter_at_start_of_text_string(self):
        """
        Test splitting a TextNode into multiple TextNodes by a delimiter,
        where the delimiter text segment is at the start of the text string.
        """
        # Arrange
        node = TextNode("**bold** string", "text")
        # Act
        actual_nodes = split_nodes_delimiter([node], "**", "bold")
        expected_nodes = [
            TextNode("bold", "bold"),
            TextNode(" string", "text"),
        ]
        # Assert
        self.assertListEqual(actual_nodes, expected_nodes)

    def test_split_nodes_delimiter_adjacent_delim_text(self):
        """
        Test splitting a TextNode into multiple TextNodes by a delimiter,
        where there are two adjacent delimited text segements.
        """
        # Arrange
        node = TextNode("**bold1****bold2**`code`", "text")
        # Act
        actual_nodes = split_nodes_delimiter([node], "**", "bold")
        expected_nodes = [
            TextNode("bold1", "bold"),
            TextNode("bold2", "bold"),
            TextNode("`code`", "text"),
        ]
        # Assert
        self.assertListEqual(actual_nodes, expected_nodes)

    def test_split_nodes_delimiter_without_end_delimiter(self):
        """
        Test splitting a TextNode, but the target TextNode has an invalid
        markdown syntax where delimiter has not been ended properly.
        """
        # Arrange
        node = TextNode("**bold** `code` **bold", "text")
        # Act / Assert
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", "bold")

    def test_split_nodes_delimiter_with_non_text_type(self):
        """
        Test splitting a TextNode with non-text type.
        """
        # Arrange
        nodes: list[TextNode] = [
            TextNode("italic text", "italic"),
            TextNode("bold text", "bold"),
            TextNode("Text with a `code block`", "text"),
        ]
        # Act
        actual_nodes = split_nodes_delimiter(nodes, "`", "code")
        expected_nodes = [
            TextNode("italic text", "italic"),
            TextNode("bold text", "bold"),
            TextNode("Text with a ", "text"),
            TextNode("code block", "code"),
        ]
        # Assert
        self.assertListEqual(actual_nodes, expected_nodes)

    def test_split_nodes_delimiter_italic_on_bold_included(self):
        """
        Test splitting a TextNode with both bold and italic markdown syntax.
        """
        # Arrange
        nodes = [
            TextNode("**bold** and *italic*", "text"),
        ]
        # Act
        actual_nodes = split_nodes_delimiter(nodes, "*", "italic")
        expected_nodes = [
            TextNode("**bold** and ", "text"),
            TextNode("italic", "italic"),
        ]
        # Assert
        self.assertEqual(actual_nodes, expected_nodes)

    def test_split_nodes_delimiter_with_combos1(self):
        """
        Test splitting TextNode with multiple markdown syntax.
        """
        # Arrange
        nodes = [
            TextNode(
                "***not bold***italic*`code`'abc'cool what_dkfj_ **bold** and **bold***more italic*",
                "text",
            ),
        ]
        # Act / Assert
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "*", "italic")

    def test_split_nodes_delimiter_with_combos2(self):
        """
        Test splitting TextNode with multiple markdown syntax.
        """
        # Arrange
        nodes = [
            TextNode(
                "***not bold****italic*`code`'abc'cool what_dkfj_ **bold** and **bold***more italic*",
                "text",
            ),
        ]
        # Act
        actual_nodes = split_nodes_delimiter(nodes, "*", "italic")
        expected_nodes = [
            TextNode("***not bold***", "text"),
            TextNode("italic", "italic"),
            TextNode("`code`'abc'cool what_dkfj_ **bold** and **bold**", "text"),
            TextNode("more italic", "italic"),
        ]
        # Assert
        self.assertListEqual(actual_nodes, expected_nodes)
