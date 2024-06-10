import pprint
import unittest

from block.block_nodes_to_html_nodes import heading_block_to_html_node
from block.heading_block import HeadingBlock
from leaf_node import LeafNode
from parent_node import ParentNode


class TestBlockNodesToHTMLNodes(unittest.TestCase):
    def test_heading_block_to_html_node(self):
        # Arrange
        heading = HeadingBlock("ABC Heading", "heading", 1)
        # Act
        actual = heading_block_to_html_node(heading)
        pprint.pp(actual)
        expected = ParentNode("h1", [LeafNode(None, "ABC Heading")])
        pprint.pp(expected)
        # Assert
        self.assertEqual(actual, expected)
