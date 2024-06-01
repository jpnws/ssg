import unittest

from util import text_node_to_html_node

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
        # Act
        # Assert
