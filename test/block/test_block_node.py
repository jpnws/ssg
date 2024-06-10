import unittest

from block.block_node import BlockNode


class TestBlockNode(unittest.TestCase):
    def test_eq(self):
        # Arrange / Act
        node1 = BlockNode("# Heading1", "heading")
        node2 = BlockNode("# Heading1", "heading")
        # Assert
        self.assertEqual(node1, node2)

    def test_neq(self):
        # Arrange / Act
        node1 = BlockNode("# Heading1", "heading")
        node2 = BlockNode("# Heading2", "heading")
        # Assert
        self.assertNotEqual(node1, node2)

    # def test_repr(self):
    #     # Arrange
    #     node = BlockNode("# Heading1", "heading")
    #     expected = "BlockNode('# Heading1', 'heading')"
    #     # Act
    #     actual = repr(node)
    #     # Arrange
    #     self.assertEqual(actual, expected)
