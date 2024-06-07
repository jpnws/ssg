class BlockNode:
    def __init__(self, block_text: str, block_type: str):
        self.block_text = block_text
        self.block_type = block_type

    def __eq__(self, other: object) -> bool:
        """
        Compare two BlockNode objects for equality.

        Args:
            other (BlockNode): The BlockNode object to compare with.

        Returns:
            bool: True if the two BlockNode object attributes are equal. False
            otherwise.
        """
        if not isinstance(other, BlockNode):
            return False
        return (
            self.block_text == other.block_text and self.block_type == other.block_type
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of the BlockNode object.

        The returned string includes the block_text and block_type.

        Returns:
            str: A string representation of the BlockNode object.
        """
        return f"BlockNode({self.block_text}, {self.block_type})"
