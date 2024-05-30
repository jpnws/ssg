import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_init(self):
        html_node = HTMLNode("div", "Hello, World!", [], {"class": "container"})
        self.assertEqual(html_node.tag, "div")
        self.assertEqual(html_node.value, "Hello, World!")
        self.assertEqual(html_node.children, [])
        self.assertEqual(html_node.props, {"class": "container"})

    def test_props_to_html(self):
        html_node = HTMLNode(None, None, [], {"class": "container"})
        self.assertEqual(html_node.props_to_html(), 'class="container"')
        html_node = HTMLNode(None, None, [], {"class": "container", "id": "main"})
        self.assertEqual(html_node.props_to_html(), 'class="container" id="main"')
