from htmlnode import HTMLNode


class ParentNode(HTMLNode):

    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict[str, str] | None = None,
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        """
        Converts the ParentNode object to an HTML string representation.

        Returns:
            str: The HTML string representation of the ParentNode object.

        Raises:
            ValueError: If the tag or children nodes are not provided.
        """
        if not self.tag:
            raise ValueError("Tag must be provided.")
        if not self.children:
            raise ValueError("Children nodes must be provided.")
        nodes = []
        for node in self.children:
            # Recursion happens here because `node.to_html` calls its own
            # childrens' `to_html` as well.
            nodes.append(node.to_html())
        props_html = self.props_to_html()
        start_tag = f"<{self.tag} {props_html}>" if props_html else f"<{self.tag}>"
        return f"{start_tag}{"".join(nodes)}</{self.tag}>"
