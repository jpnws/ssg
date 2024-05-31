import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "This is a text node"
        self.text_type1 = "bold"
        self.text_type2 = "italic"
        self.url = "https://www.github.com"

    def test_init(self):
        """
        Test that the TextNode instance variables are correctly set.
        """
        # Arrange / Act
        node1 = TextNode(self.text, self.text_type1, self.url)
        # Assert
        self.assertEqual(node1.text, self.text)
        self.assertEqual(node1.text_type, self.text_type1)
        self.assertEqual(node1.url, self.url)

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
        node1 = TextNode(self.text, self.text_type1)
        # Assert
        self.assertIsNone(node1.url)


if __name__ == "__main__":
    unittest.main()
