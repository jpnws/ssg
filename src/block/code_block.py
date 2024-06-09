from block.block_node import BlockNode


class CodeBlock(BlockNode):
    def __init__(self, block_text: str, block_type: str, block_language: str) -> None:
        super().__init__(block_text, block_type)
        self.block_language = block_language

    def __eq__(self, other: object) -> bool:
        """
        Compare two CodeBlock objects for equality.

        Args:
            other (CodeBlock): The CodeBlock object to compare with.

        Returns:
            bool: True if two CodeBlock object attributes are equal. False
            otherwise.
        """
        if not isinstance(other, CodeBlock):
            return False
        return (
            self.block_text == other.block_text
            and self.block_type == other.block_type
            and self.block_language == other.block_language
        )

    def __repr__(self) -> str:
        """
        Returns astring representation of the CodeBlock object.

        Returns:
            str: A string representation of the CodeBlock object.
        """
        return f"CodeBlock({repr(self.block_text)}, {repr(self.block_type)}, {repr(self.block_language)})"
