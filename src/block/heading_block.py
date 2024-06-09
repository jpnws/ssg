from block.block_node import BlockNode


class HeadingBlock(BlockNode):
    def __init__(self, block_text: str, block_type: str, block_level: int) -> None:
        super().__init__(block_text, block_type)
        self.block_level = block_level

    def __eq__(self, other: object) -> bool:
        """
        Compare two HeadingBlock objects for equality.

        Args:
            other (HeadingBlock): The HeadingBlock object to compare with.

        Returns:
            bool: True if two HeadingBlock object attributes are equal. False
            otherwise.
        """
        if not isinstance(other, HeadingBlock):
            return False
        return (
            self.block_text == other.block_text
            and self.block_type == other.block_type
            and self.block_level == other.block_level
        )

    def __repr__(self) -> str:
        """
        Returns astring representation of the HeadingBlock object.

        Returns:
            str: A string representation of the HeadingBlock object.
        """
        return f"HeadingBlock({repr(self.block_text)}, {repr(self.block_type)}, {repr(self.block_level)})"
