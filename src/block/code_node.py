from block.block_node import BlockNode


class CodeNode(BlockNode):
    def __init__(self, block_text: str, block_type: str, block_language: str) -> None:
        super().__init__(block_text, block_type)
        self.block_language = block_language

    def __eq__(self, other: object) -> bool:
        """
        Compare two CodeNode objects for equality.

        Args:
            other (CodeNode): The CodeNode object to compare with.

        Returns:
            bool: True if two CodeNode object attributes are equal. False
            otherwise.
        """
        if not isinstance(other, CodeNode):
            return False
        return (
            self.block_text == other.block_text
            and self.block_type == other.block_type
            and self.block_language == other.block_language
        )

    def __repr__(self) -> str:
        """
        Returns astring representation of the CodeNode object.

        Returns:
            str: A string representation of the CodeNode object.
        """
        return f"CodeNode({self.block_text}, {self.block_type}, {self.block_language})"
