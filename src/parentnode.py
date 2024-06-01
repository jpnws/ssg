from htmlnode import HTMLNode


class ParentNode(HTMLNode):

    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag must be provided.")
        if not self.children:
            raise ValueError("Children nodes must be provided.")
        nodes = []
        for node in self.children:
            nodes.append(node.to_html())
        props_html = self.props_to_html()
        start_tag = f"<{self.tag} {props_html}>" if props_html else f"<{self.tag}>"
        return f"{start_tag}{"".join(nodes)}</{self.tag}>"
