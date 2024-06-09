import unittest

from block.code_block import CodeBlock


class TestCodeBlock(unittest.TestCase):
    def test_eq(self):
        # Arrange / Act
        code1 = CodeBlock("Here is code\nmore code", "code", "python")
        code2 = CodeBlock("Here is code\nmore code", "code", "python")
        # Assert
        self.assertEqual(code1, code2)

    def test_repr(self):
        # Assert
        code = CodeBlock("Here is code\nmore code", "code", "python")
        expected = "CodeBlock('Here is code\\nmore code', 'code', 'python')"
        # Act
        actual = repr(code)
        # Assert
        self.assertEqual(actual, expected)
