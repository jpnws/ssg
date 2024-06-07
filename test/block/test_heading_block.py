import unittest

from blocks.heading_block import HeadingBlock


class TestHeadingBlock(unittest.TestCase):
    def test_eq(self):
        # Arrange / Act
        heading1 = HeadingBlock("Here is a heading", "heading", 1)
        heading2 = HeadingBlock("Here is a heading", "heading", 1)
        # Assert
        self.assertEqual(heading1, heading2)

    def test_repr(self):
        # Assert
        heading = HeadingBlock("Here is a heading", "heading", 1)
        expected = "HeadingBlock(Here is a heading, heading, 1)"
        # Act
        actual = repr(heading)
        # Assert
        self.assertEqual(actual, expected)
