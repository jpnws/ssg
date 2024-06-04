import unittest

from util import text_node_to_html_node
from util import split_nodes_delimiter
from util import extract_markdown_images
from util import extract_markdown_links
from util import split_nodes_image
from util import split_nodes_link

from textnode import TextNode

from htmlnode import HTMLNode


class TestUtil(unittest.TestCase):

    def test_text_to_html(self):
        """
        Test the TextNode to HTMLNode/LeafNode conversion.
        """
        # Arrange
        node1 = TextNode("text string", "text")
        node2 = TextNode("bold text", "bold")
        node3 = TextNode("italic text", "italic")
        node4 = TextNode("code text", "code")
        node5 = TextNode("link text", "link", "https://www.google.com")
        node6 = TextNode("alt text", "image", "https://www.google.com")
        node7 = TextNode("invalid type", "invalid")
        # Act
        res1 = text_node_to_html_node(node1)
        res2 = text_node_to_html_node(node2)
        res3 = text_node_to_html_node(node3)
        res4 = text_node_to_html_node(node4)
        res5 = text_node_to_html_node(node5)
        res6 = text_node_to_html_node(node6)
        # Assert
        self.assertIsInstance(res1, HTMLNode)
        self.assertIsInstance(res2, HTMLNode)
        self.assertIsInstance(res3, HTMLNode)
        self.assertIsInstance(res4, HTMLNode)
        self.assertIsInstance(res5, HTMLNode)
        self.assertIsInstance(res6, HTMLNode)
        self.assertEqual(res1.tag, None)
        self.assertEqual(res1.value, "text string")
        self.assertEqual(res2.tag, "b")
        self.assertEqual(res2.value, "bold text")
        self.assertEqual(res3.tag, "i")
        self.assertEqual(res3.value, "italic text")
        self.assertEqual(res4.tag, "code")
        self.assertEqual(res4.value, "code text")
        self.assertEqual(res5.tag, "a")
        self.assertEqual(res5.value, "link text")
        self.assertEqual(res5.props, {"href": "https://www.google.com"})
        self.assertEqual(res6.tag, "img")
        self.assertEqual(res6.value, "")
        self.assertEqual(
            res6.props,
            {"src": "https://www.google.com", "alt": "alt text"},
        )
        with self.assertRaises(ValueError):
            text_node_to_html_node(node7)

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

    def test_extract_markdown_images(self):
        """
        Test extracting markdown images.
        """
        # Arrange
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        # Act
        actual, expected = extract_markdown_images(text), [
            (
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            (
                "another",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png",
            ),
        ]
        # Assert
        self.assertListEqual(actual, expected)

    def test_extract_markdown_links(self):
        """
        Test extracting markdown links.
        """
        # Arrange
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        # Act
        actual, expected = extract_markdown_links(text), [
            ("link", "https://www.example.com"),
            ("another", "https://www.example.com/another"),
        ]
        # Assert
        self.assertListEqual(actual, expected)

    def test_split_nodes_image(self):
        """
        Test that TextNodes are split by images in markdown text.
        """
        # Arrange
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            "text",
        )
        # Act
        actual = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", "text"),
            TextNode(
                "image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and another ", "text"),
            TextNode(
                "second image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
            ),
        ]
        # Assert
        self.assertListEqual(actual, expected)

    def test_split_nodes_link(self):
        """
        Test that TextNodes are split by links in markdown text.
        """
        # Arrange
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            "text",
        )
        # Act
        actual = split_nodes_link([node])
        expected = [
            TextNode("This is text with a ", "text"),
            TextNode("link", "link", "https://www.example.com"),
            TextNode(" and ", "text"),
            TextNode("another", "link", "https://www.example.com/another"),
        ]
        # Assert
        self.assertListEqual(actual, expected)
