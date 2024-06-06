import unittest

from textnode import TextNode

from split_images_links import split_nodes_image
from split_images_links import split_nodes_link


class TestSplitImagesLinks(unittest.TestCase):
    def test_split_nodes_image(self):
        """
        Test that TextNodes are split by images in markdown text.
        """
        # Arrange
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) and another normal text!",
            "text",
        )
        # Act
        actual = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", "text"),
            TextNode(
                "image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and another ", "text"),
            TextNode(
                "second image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
            ),
            TextNode(" and another normal text!", "text"),
        ]
        # Assert
        self.assertListEqual(actual, expected)

    def test_split_nodes_link(self):
        """
        Test that TextNodes are split by links in markdown text.
        """
        # Arrange
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            "text",
        )
        # Act
        actual = split_nodes_link([node])
        expected = [
            TextNode("This is text with a ", "text"),
            TextNode("link", "link", "https://www.example.com"),
            TextNode(" and ", "text"),
            TextNode("another", "link", "https://www.example.com/another"),
        ]
        # Assert
        self.assertListEqual(actual, expected)

    def test_split_nodes_image_combo(self):
        """
        Test that TextNodes are split by images in markdown text with varying
        form of strings.
        """
        # Arrange
        node1 = TextNode(
            ".![img](image-link) a ![img](image-link)b![img](image-link)![img](image-link).",
            "text",
        )
        node2 = TextNode(
            "![img](image-link)![img](image-link)![img(image-link)",
            "text",
        )
        # Act
        actual = split_nodes_image([node1, node2])
        expected = [
            TextNode(".", "text"),
            TextNode("img", "image", "image-link"),
            TextNode(" a ", "text"),
            TextNode("img", "image", "image-link"),
            TextNode("b", "text"),
            TextNode("img", "image", "image-link"),
            TextNode("img", "image", "image-link"),
            TextNode(".", "text"),
            TextNode("img", "image", "image-link"),
            TextNode("img", "image", "image-link"),
            TextNode("![img(image-link)", "text"),
        ]
        # Assert
        self.assertListEqual(actual, expected)

    def test_split_nodes_link_combo(self):
        """
        Test that TextNodes are split by links in markdown text with varying
        form of strings.
        """
        # Arrange
        node1 = TextNode(
            ".[link](link-link) a [link](link-link)b[link](link-link)[link](link-link).",
            "text",
        )
        node2 = TextNode(
            "[link](link-link)[link](link-link)[link(link-link)",
            "text",
        )
        # Act
        actual = split_nodes_link([node1, node2])
        expected = [
            TextNode(".", "text"),
            TextNode("link", "link", "link-link"),
            TextNode(" a ", "text"),
            TextNode("link", "link", "link-link"),
            TextNode("b", "text"),
            TextNode("link", "link", "link-link"),
            TextNode("link", "link", "link-link"),
            TextNode(".", "text"),
            TextNode("link", "link", "link-link"),
            TextNode("link", "link", "link-link"),
            TextNode("[link(link-link)", "text"),
        ]
        # Assert
        self.assertListEqual(actual, expected)
