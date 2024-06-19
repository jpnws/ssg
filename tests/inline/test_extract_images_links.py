import unittest

from src.inline.extract_images_links import (
    extract_markdown_images,
    extract_markdown_links,
)


class TestExtractLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        """
        Test extracting markdown images.
        """
        # Arrange
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        # Act
        actual, expected = (
            extract_markdown_images(text),
            [
                (
                    "image",
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                (
                    "another",
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png",
                ),
            ],
        )
        # Assert
        self.assertListEqual(actual, expected)

    def test_extract_markdown_links(self):
        """
        Test extracting markdown links.
        """
        # Arrange
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        # Act
        actual, expected = (
            extract_markdown_links(text),
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another"),
            ],
        )
        # Assert
        self.assertListEqual(actual, expected)
