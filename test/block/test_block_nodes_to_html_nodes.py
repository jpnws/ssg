# import pprint
import unittest

from block.block_node import BlockNode
from block.block_nodes_to_html_nodes import (
    block_nodes_to_html_nodes,
    code_block_to_html_node,
    heading_block_to_html_node,
    ordered_list_block_to_html_node,
    paragraph_block_to_html_node,
    quote_block_to_html_node,
    unordered_list_block_to_html_node,
)
from block.code_block import CodeBlock
from block.heading_block import HeadingBlock
from leaf_node import LeafNode
from parent_node import ParentNode


class TestBlockNodesToHTMLNodes(unittest.TestCase):
    def test_block_nodes_to_html_nodes(self):
        # Arrange
        heading = HeadingBlock("Heading", "heading", 1)
        code = CodeBlock("# comment\ndef func():\n    pass\n", "code", "python")
        quote = BlockNode(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nMorbi quis interdum nunc. Aenean rutrum pretium eros, non placerat est rhoncus ultricies.\nIn sagittis consectetur tristique. Sed porttitor mi magna.\n",
            "quote",
        )
        unordered_list = BlockNode(
            "Unordered **list item** 1\nUnordered *list item* 2\n", "unordered_list"
        )
        ordered_list = BlockNode(
            "Ordered **list item** 1\nOrdered *list item* 2\n", "ordered_list"
        )
        paragraph = BlockNode(
            "This is a **paragraph** with *italic* and `code`.\n", "paragraph"
        )
        block_nodes = [heading, code, quote, unordered_list, ordered_list, paragraph]
        # Act
        actual = block_nodes_to_html_nodes(block_nodes)
        expected = ParentNode(
            "div",
            [
                ParentNode("h1", [LeafNode(None, "Heading")]),
                ParentNode(
                    "pre", [LeafNode("code", "# comment\ndef func():\n    pass\n")]
                ),
                ParentNode(
                    "blockquote",
                    [
                        LeafNode(
                            None,
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nMorbi quis interdum nunc. Aenean rutrum pretium eros, non placerat est rhoncus ultricies.\nIn sagittis consectetur tristique. Sed porttitor mi magna.\n",
                        )
                    ],
                ),
                ParentNode(
                    "ul",
                    [
                        ParentNode(
                            "li",
                            [
                                LeafNode(None, "Unordered "),
                                LeafNode("b", "list item"),
                                LeafNode(None, " 1"),
                            ],
                        ),
                        ParentNode(
                            "li",
                            [
                                LeafNode(None, "Unordered "),
                                LeafNode("i", "list item"),
                                LeafNode(None, " 2"),
                            ],
                        ),
                    ],
                ),
                ParentNode(
                    "ol",
                    [
                        ParentNode(
                            "li",
                            [
                                LeafNode(None, "Ordered "),
                                LeafNode("b", "list item"),
                                LeafNode(None, " 1"),
                            ],
                        ),
                        ParentNode(
                            "li",
                            [
                                LeafNode(None, "Ordered "),
                                LeafNode("i", "list item"),
                                LeafNode(None, " 2"),
                            ],
                        ),
                    ],
                ),
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "This is a "),
                        LeafNode("b", "paragraph"),
                        LeafNode(None, " with "),
                        LeafNode("i", "italic"),
                        LeafNode(None, " and "),
                        LeafNode("code", "code"),
                        LeafNode(None, ".\n"),
                    ],
                ),
            ],
        )
        # Assert
        self.assertEqual(actual, expected)

    def test_heading_block_to_html_node_basic(self):
        # Arrange
        heading = HeadingBlock("ABC Heading", "heading", 1)
        # Act
        actual = heading_block_to_html_node(heading)
        expected = ParentNode("h1", [LeafNode(None, "ABC Heading")])
        # Assert
        self.assertEqual(actual, expected)

    def test_heading_block_to_html_node_mixed(self):
        # Arrange
        heading1 = HeadingBlock("Heading 1", "heading", 1)
        heading2 = HeadingBlock("Heading 2", "heading", 2)
        heading3 = HeadingBlock("Heading 3", "heading", 3)
        heading4 = HeadingBlock("Heading 4", "heading", 4)
        heading5 = HeadingBlock("Heading 5", "heading", 5)
        heading6 = HeadingBlock("Heading 6", "heading", 6)
        # Act
        actual1 = heading_block_to_html_node(heading1)
        actual2 = heading_block_to_html_node(heading2)
        actual3 = heading_block_to_html_node(heading3)
        actual4 = heading_block_to_html_node(heading4)
        actual5 = heading_block_to_html_node(heading5)
        actual6 = heading_block_to_html_node(heading6)
        # Assert
        self.assertEqual(actual1, ParentNode("h1", [LeafNode(None, "Heading 1")]))
        self.assertEqual(actual2, ParentNode("h2", [LeafNode(None, "Heading 2")]))
        self.assertEqual(actual3, ParentNode("h3", [LeafNode(None, "Heading 3")]))
        self.assertEqual(actual4, ParentNode("h4", [LeafNode(None, "Heading 4")]))
        self.assertEqual(actual5, ParentNode("h5", [LeafNode(None, "Heading 5")]))
        self.assertEqual(actual6, ParentNode("h6", [LeafNode(None, "Heading 6")]))

    def test_heading_block_to_html_node_mixed_inline_styles(self):
        # Arrange
        heading_with_bold = HeadingBlock("**Heading 1**", "heading", 1)
        heading_with_italic = HeadingBlock("*Heading 2*", "heading", 2)
        heading_with_code = HeadingBlock("`Heading 3`", "heading", 3)
        heading_with_link = HeadingBlock(
            "[Heading 4](https://example.com)", "heading", 4
        )
        heading_with_image = HeadingBlock(
            "![Heading 5](https://example.com/image.jpg)", "heading", 5
        )
        # Act
        actual_with_bold = heading_block_to_html_node(heading_with_bold)
        actual_with_italic = heading_block_to_html_node(heading_with_italic)
        actual_with_code = heading_block_to_html_node(heading_with_code)
        actual_with_link = heading_block_to_html_node(heading_with_link)
        actual_with_image = heading_block_to_html_node(heading_with_image)
        # Assert
        self.assertEqual(
            actual_with_bold, ParentNode("h1", [LeafNode("b", "Heading 1")])
        )
        self.assertEqual(
            actual_with_italic, ParentNode("h2", [LeafNode("i", "Heading 2")])
        )
        self.assertEqual(
            actual_with_code, ParentNode("h3", [LeafNode("code", "Heading 3")])
        )
        self.assertEqual(
            actual_with_link,
            ParentNode(
                "h4", [LeafNode("a", "Heading 4", {"href": "https://example.com"})]
            ),
        )
        self.assertEqual(
            actual_with_image,
            ParentNode(
                "h5",
                [
                    LeafNode(
                        "img",
                        "",
                        {"src": "https://example.com/image.jpg", "alt": "Heading 5"},
                    )
                ],
            ),
        )

    def test_heading_block_to_html_node_invalid_block_type(self):
        # Arrange
        heading = HeadingBlock("Heading", "invalid", 1)
        # Act / Assert
        with self.assertRaises(ValueError):
            heading_block_to_html_node(heading)

    def test_code_block_to_html_node_basic(self):
        # Arrange
        code_block = CodeBlock("# comment\ndef func():\n    pass\n", "code", "python")
        # Act
        actual = code_block_to_html_node(code_block)
        expected = ParentNode(
            "pre", [LeafNode("code", "# comment\ndef func():\n    pass\n")]
        )
        # Assert
        self.assertEqual(actual, expected)

    def test_quote_block_to_html_node_basic(self):
        # Arrange
        quote_block = BlockNode(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nMorbi quis interdum nunc. Aenean rutrum pretium eros, non placerat est rhoncus ultricies.\nIn sagittis consectetur tristique. Sed porttitor mi magna.\n",
            "quote",
        )
        # Act
        actual = quote_block_to_html_node(quote_block)
        expected = ParentNode(
            "blockquote",
            [
                LeafNode(
                    None,
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nMorbi quis interdum nunc. Aenean rutrum pretium eros, non placerat est rhoncus ultricies.\nIn sagittis consectetur tristique. Sed porttitor mi magna.\n",
                )
            ],
        )
        # Arrange
        self.assertEqual(actual, expected)

    def test_unordered_list_block_to_html_node_basic(self):
        # Arrange
        unordered_list_block = BlockNode(
            "Unordered **list item** 1\nUnordered *list item* 2\n", "unordered_list"
        )
        # Act
        actual = unordered_list_block_to_html_node(unordered_list_block)
        expect = ParentNode(
            "ul",
            [
                ParentNode(
                    "li",
                    [
                        LeafNode(None, "Unordered "),
                        LeafNode("b", "list item"),
                        LeafNode(None, " 1"),
                    ],
                ),
                ParentNode(
                    "li",
                    [
                        LeafNode(None, "Unordered "),
                        LeafNode("i", "list item"),
                        LeafNode(None, " 2"),
                    ],
                ),
            ],
        )
        # Assert
        self.assertEqual(actual, expect)

    def test_ordered_list_block_to_html_node_basic(self):
        # Arrange
        ordered_list_block = BlockNode(
            "Ordered **list item** 1\nOrdered *list item* 2\n", "ordered_list"
        )
        # Act
        actual = ordered_list_block_to_html_node(ordered_list_block)
        expect = ParentNode(
            "ol",
            [
                ParentNode(
                    "li",
                    [
                        LeafNode(None, "Ordered "),
                        LeafNode("b", "list item"),
                        LeafNode(None, " 1"),
                    ],
                ),
                ParentNode(
                    "li",
                    [
                        LeafNode(None, "Ordered "),
                        LeafNode("i", "list item"),
                        LeafNode(None, " 2"),
                    ],
                ),
            ],
        )
        # Assert
        self.assertEqual(actual, expect)

    def test_paragraph_block_to_html_node_basic(self):
        # Arrange
        paragraph_block = BlockNode(
            "This is a **paragraph** with *italic* and `code`.\n", "paragraph"
        )
        # Act
        actual = paragraph_block_to_html_node(paragraph_block)
        expect = ParentNode(
            "p",
            [
                LeafNode(None, "This is a "),
                LeafNode("b", "paragraph"),
                LeafNode(None, " with "),
                LeafNode("i", "italic"),
                LeafNode(None, " and "),
                LeafNode("code", "code"),
                LeafNode(None, ".\n"),
            ],
        )
        # Assert
        self.assertEqual(actual, expect)
