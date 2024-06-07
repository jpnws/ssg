import unittest

from inline.text_node import TextNode
from html_node import HTMLNode

from inline.text_node_to_leaf_node import text_node_to_leaf_node


class TestTextToHTML(unittest.TestCase):
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
        res1 = text_node_to_leaf_node(node1)
        res2 = text_node_to_leaf_node(node2)
        res3 = text_node_to_leaf_node(node3)
        res4 = text_node_to_leaf_node(node4)
        res5 = text_node_to_leaf_node(node5)
        res6 = text_node_to_leaf_node(node6)
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
            text_node_to_leaf_node(node7)
