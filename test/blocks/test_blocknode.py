import unittest

from markdown_blocks import BlockNode


class TestBlockNode(unittest.TestCase):
    def test_eq(self):
        node1 = BlockNode("# Heading1", "heading")
        node2 = BlockNode("# Heading1", "heading")
        self.assertEqual(node1, node2)
