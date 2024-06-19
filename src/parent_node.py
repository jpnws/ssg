from .html_node import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict[str, str | None] | None = None,
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
        nodes: list[str] = []
        for node in self.children:
            # Recursion happens here because `node.to_html` calls its own
            # children's `to_html` as well.
            nodes.append(node.to_html())
        props_html = self.props_to_html()
        start_tag = f"<{self.tag} {props_html}>" if props_html else f"<{self.tag}>"
        return f"{start_tag}{"".join(nodes)}</{self.tag}>"

    def __repr__(self) -> str:
        """
        Returns a string representation of the ParentNode object.
        """

        def func(node: HTMLNode) -> str:
            return f"{node}"

        children_nodes = None
        if self.children:
            children_list = list(map(func, self.children))
            children_string = "".join(children_list)
            children_nodes = f"""
    [
        {children_string}
    ]"""
        return f"""
ParentNode(
    tag={repr(self.tag)},
    value={repr(self.value)},
    children={children_nodes}
    props={repr(self.props)}
)"""

    def __eq__(self, other: object) -> bool:
        """
        Args:
            -
        """
        if not isinstance(other, ParentNode):
            return False
        return (
            self.tag == other.tag
            and self.children == other.children
            and self.props == other.props
        )
