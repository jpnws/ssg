from html_node import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str | None,
        props: dict[str, str | None] | None = None,
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        """
        Converts the LeafNode object to an HTML string.

        Returns:
            str: The HTML representation of the LeafNode object.

        Raises:
            ValueError: If the `value` attribute of the LeafNode is not provided.
        """
        if not self.value:
            raise ValueError("LeafNode `value` must be provided.")
        if not self.tag:
            return self.value
        props = self.props_to_html()
        start_tag = f"<{self.tag} {props}>" if props else f"<{self.tag}>"
        return f"{start_tag}{self.value}</{self.tag}>"
