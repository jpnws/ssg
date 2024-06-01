import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):

    def setUp(self) -> None:
        self.text: str = "This is a text node"
        self.text_type1: str = "bold"
        self.text_type2: str = "italic"
        self.url: str = "https://www.github.com"

    def test_init(self):
        """
        Test that the TextNode instance variables are correctly set.
        """
        # Arrange / Act
        node = TextNode(self.text, self.text_type1, self.url)
        # Assert
        self.assertEqual(node.text, self.text)
        self.assertEqual(node.text_type, self.text_type1)
        self.assertEqual(node.url, self.url)

    def test_eq(self):
        """
        Test that two TextNode instances are equal.
        """
        # Arrange / Act
        node1 = TextNode(self.text, self.text_type1)
        node2 = TextNode(self.text, self.text_type1)
        # Assert
        self.assertEqual(node1, node2)

    def test_neq(self):
        """
        Test that two TextNode instances are not equal.
        """
        # Arrange / Act
        node1 = TextNode(self.text, self.text_type1)
        node2 = TextNode(self.text, self.text_type2)
        # Assert
        self.assertNotEqual(node1, node2)

    def test_none_url(self):
        """
        Test that the url attribute is None when not provided.
        """
        # Arrange / Act
        node = TextNode(self.text, self.text_type1)
        # Assert
        self.assertIsNone(node.url)

    def test_repr(self):
        """
        Test the __repr__ method to ensure it returns the correct string.
        """
        # Arrange
        node = TextNode(self.text, self.text_type1, self.url)
        expected_repr = f"TextNode({self.text}, {self.text_type1}, {self.url})"
        # Act
        actual_repr = repr(node)
        # Assert
        self.assertEqual(actual_repr, expected_repr)


if __name__ == "__main__":
    unittest.main()
