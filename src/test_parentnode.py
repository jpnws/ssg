import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    def test_to_html_one_level(self):
        """
        Ensure that the nested children tags show up properly.
        """
        # Arrange
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        # Act
        res = node.to_html()
        # Assert
        self.assertEqual(
            res, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_multiple_levels(self):
        """
        Ensure that the html tags show up correctly for nested nodes.
        """
        # Arrange
        node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
            ],
        )
        node2 = ParentNode(
            "div",
            [
                node1,
                LeafNode(None, "Normal text"),
            ],
        )
        node3 = ParentNode(
            "div",
            [
                node2,
                LeafNode("i", "italic text"),
            ],
        )
        # Act
        res = node3.to_html()
        # Assert
        self.assertEqual(
            res,
            "<div><div><p><b>Bold text</b></p>Normal text</div><i>italic text</i></div>",
        )
