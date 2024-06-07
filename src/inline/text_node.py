class TextNode:
    def __init__(self, text: str, text_type: str, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
        """
        Compare two TextNode objects for equality.

        Args:
            other (TextNode): The TextNode object to compare with.

        Returns:
            bool: True if the two TextNode object attributes are equal, False
            otherwise.
        """
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of the TextNode object.

        The returned string includes the text, text_type, and url attributes of
        the TextNode object.

        Returns:
            str: A string representation of the TextNode object.
        """
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
