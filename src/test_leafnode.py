import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        leafnode1 = LeafNode("p", "This is a paragraph.", {"id": "para"})

        self.assertEqual(leafnode1.tag, "p")
        self.assertEqual(leafnode1.value, "This is a paragraph.")
        self.assertIsNone(leafnode1.children)
        self.assertEqual(leafnode1.props, {"id": "para"})

        html = leafnode1.to_html()
        self.assertEqual(html, '<p id="para">This is a paragraph.</p>')
