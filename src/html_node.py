from __future__ import annotations

from typing import Callable


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list[HTMLNode] | None = None,
        props: dict[str, str | None] | None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        """
        Converts the LeafNode object to an HTML string. Note: Not implemented as
        the children classes should override the method.
        """
        raise NotImplementedError

    def props_to_html(self) -> str:
        """
        Converts the properties of the HTML node to a string of HTML attributes.

        Returns:
            str: A string of HTML attributes in the format 'key="value"'.

        Example:
            >>> node = HTMLNode(None, None, None, {'class': 'container', 'id': 'main'})
            >>> node.props_to_html()
            'class="container" id="main"'
        """
        if not self.props:
            return ""
        func: Callable[[tuple[str, str | None]], str] = (
            lambda prop: f'{prop[0]}="{prop[1]}"'
        )
        props = list(map(func, self.props.items()))
        return " ".join(props)

    def __repr__(self) -> str:
        """
        Returns a string representation of the HTMLNode object.
        """
        return f"""
        HTMLNode(
            tag={repr(self.tag)},
            value={repr(self.value)},
            children={repr(self.children)}
            props={repr(self.props)}
        )
        """
