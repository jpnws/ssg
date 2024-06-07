import unittest

from leaf_node import LeafNode


class TestLeafNode(unittest.TestCase):
    def setUp(self) -> None:
        self.p_tag: str = "p"
        self.p_value: str = "This is a paragraph."
        self.p_props: dict[str, str | None] = {"id": "para", "class": "para-class"}
        self.a_tag: str = "a"
        self.a_value: str = "Click me!"
        self.a_props: dict[str, str | None] = {"href": "https://www.google.com"}

    def test_to_html_vars(self):
        """
        Make sure that the LeafNode instance variables are correctly set.
        """
        # Arrange / Act
        leafnode = LeafNode(self.p_tag, self.p_value, self.p_props)
        # Assert
        self.assertEqual(leafnode.tag, self.p_tag)
        self.assertEqual(leafnode.value, self.p_value)
        self.assertIsNone(leafnode.children)
        self.assertEqual(leafnode.props, self.p_props)

    def test_to_html_output(self):
        """
        Verify that the to_html method returns the correct HTML string.
        """
        # Arrange
        leafnode1 = LeafNode(self.p_tag, self.p_value, self.p_props)
        leafnode2 = LeafNode(self.a_tag, self.a_value, self.a_props)
        # Act
        html1 = leafnode1.to_html()
        html2 = leafnode2.to_html()
        # Assert
        self.assertEqual(
            html1,
            f'<{self.p_tag} id="{self.p_props["id"]}" class="{self.p_props["class"]}">{self.p_value}</{self.p_tag}>',
        )
        self.assertEqual(
            html2,
            f'<{self.a_tag} href="{self.a_props["href"]}">{self.a_value}</{self.a_tag}>',
        )

    def test_to_html_value_error(self):
        """
        Check that to_html raises a ValueError when value is None.
        """
        # Arrange / Act
        leafnode = LeafNode(self.p_tag, None, self.p_props)
        # Assert
        with self.assertRaises(ValueError):
            leafnode.to_html()

    def test_to_html_plain_text_output(self):
        """
        Be sure that to_html returns plain text when the tag is None or empty.
        """
        # Arrange
        leafnode = LeafNode(None, self.p_value, self.p_props)
        # Act
        res = leafnode.to_html()
        # Assert
        self.assertEqual(res, self.p_value)


if __name__ == "__main__":
    unittest.main()
