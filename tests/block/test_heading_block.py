import unittest

from src.block.heading_block import HeadingBlock


class TestHeadingBlock(unittest.TestCase):
    def test_eq(self):
        # Arrange / Act
        heading1 = HeadingBlock("Here is a heading", "heading", 1)
        heading2 = HeadingBlock("Here is a heading", "heading", 1)
        # Assert
        self.assertEqual(heading1, heading2)
