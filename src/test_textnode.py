import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):

    def test_init(self):
        text = "This is a text node"
        text_type = "bold"
        url = "https://www.github.com"
        node1 = TextNode(text, text_type, url)
        self.assertEqual(node1.text, text)
        self.assertEqual(node1.text_type, text_type)
        self.assertEqual(node1.url, url)

    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)

    def test_neq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node.", "italic")
        self.assertNotEqual(node1, node2)

    def test_none_url(self):
        node1 = TextNode("This is a text node", "bold")
        self.assertIsNone(node1.url)


if __name__ == "__main__":
    unittest.main()
