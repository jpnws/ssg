import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def setUp(self) -> None:
        self.div_tag: str = "div"
        self.div_value: str = "Hello, World!"
        self.div_props1: dict[str, str | None] = {"class": "container"}
        self.div_props2: dict[str, str | None] = {"class": "container", "id": "main"}

    def test_init(self):
        """
        Test that the HTMLNode instance variables are correctly set.
        """
        # Arrange / Act
        node = HTMLNode(self.div_tag, self.div_value, [], self.div_props1)
        # Assert
        self.assertEqual(node.tag, self.div_tag)
        self.assertEqual(node.value, self.div_value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, self.div_props1)

    def test_not_implemented_error(self):
        """
        Test that the to_html method raises NotImplementedError.
        """
        # Arrange
        node = HTMLNode(None, None, None, None)
        # Act / Assert
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        """
        Test that the props_to_html method returns the correct string.
        """
        # Arrange / Act
        node1 = HTMLNode(None, None, [], self.div_props1)
        node2 = HTMLNode(None, None, [], self.div_props2)
        # Assert
        self.assertEqual(node1.props_to_html(), f'class="{self.div_props1["class"]}"')
        self.assertEqual(
            node2.props_to_html(),
            f'class="{self.div_props2["class"]}" id="{self.div_props2["id"]}"',
        )

    def test_repr(self):
        """
        Test that the repr returns the correct string.
        """
        # Arrange
        sub_node = [HTMLNode("p", "This is a paragraph.", None, None)]
        # Act
        node = HTMLNode(self.div_tag, self.div_value, sub_node, self.div_props2)
        res = repr(node)
        # Assert
        self.assertEqual(
            res,
            f"""
        HTMLNode(
            tag={self.div_tag},
            value={self.div_value},
            children={sub_node}
            props={self.div_props2}
        )
        """,
        )


if __name__ == "__main__":
    unittest.main()
