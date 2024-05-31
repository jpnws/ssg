import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def setUp(self) -> None:
        self.p_tag = "p"
        self.p_value = "This is a paragraph."
        self.p_props = {"id": "para"}

    def test_to_html_vars(self):
        """
        Test for the instance variables.
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
        Test for the full HTML string returned by to_html.
        """
        # Arrange
        leafnode = LeafNode(self.p_tag, self.p_value, self.p_props)
        # Act
        html = leafnode.to_html()
        # Assert
        self.assertEqual(
            html,
            f'<{self.p_tag} id="{self.p_props["id"]}">{self.p_value}</{self.p_tag}>',
        )

    def test_to_html_value_error(self):
        """
        Test for the ValueError exception when value is None.
        """
        # Arrange / Act
        leafnode = LeafNode(self.p_tag, None, self.p_props)
        # Assert
        with self.assertRaises(ValueError):
            leafnode.to_html()

    def test_to_html_plain_text_output(self):
        """
        Test for the plain text value when tag is empty or None.
        """
        # Arrange
        leafnode = LeafNode(None, self.p_value, self.p_props)
        # Act
        res = leafnode.to_html()
        # Assert
        self.assertEqual(res, self.p_value)
