from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Any, Optional


def flatten(source: Any):
    if isinstance(source, str) or not isinstance(source, Iterable):
        yield source
        return
    for element in source:
        yield from flatten(element)


@dataclass
class BaseHtmlElement:
    name: str
    single: bool = False
    no_content: bool = False
    parent: Optional["BaseHtmlElement"] = None
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)

    def __call__(self, **attrs) -> "BaseHtmlElement":
        if "_class" in attrs:
            attrs["class"] = attrs.pop("_class")
        return BaseHtmlElement(self.name, self.single, self.no_content, self.parent, attrs)

    def __getitem__(self, children) -> "BaseHtmlElement":
        element = BaseHtmlElement(self.name, self.single, self.no_content, self.parent, self.attrs)
        true_children = list(flatten(children))
        for one in true_children:
            if isinstance(one, BaseHtmlElement):
                one.parent = element
        element.children = true_children
        return element

    def level(self) -> int:
        return self.parent.level() + 1 if self.parent else 0

    def __repr__(self):
        blank = "  " * self.level()
        attrs = "({})".format(";".join(f"{key}={repr(self.attrs[key])}" for key in self.attrs)) if self.attrs else ""
        children = "\n".join(
            repr(child) if isinstance(child, BaseHtmlElement) else blank + repr(child) for child in self.children
        )
        if self.single or self.no_content:
            return "{blank}{name}{attrs}".format(blank=blank, name=self.name, attrs=attrs)
        return "{blank}{name}{attrs}[\n{children}]".format(blank=blank, name=self.name, attrs=attrs, children=children)

    def __str__(self):
        blank = "  " * self.level()
        attrs = (
            " {}".format(" ".join(f'{key.replace("_", "-")}="{str(self.attrs[key])}"' for key in self.attrs))
            if self.attrs
            else ""
        )
        children = "\n".join(
            str(child) if isinstance(child, BaseHtmlElement) else blank + str(child) for child in self.children
        )
        if self.single:
            return "{blank}<{name}{attrs}>".format(blank=blank, name=self.name, attrs=attrs)
        if self.no_content:
            return "{blank}<{name}{attrs}/>".format(blank=blank, name=self.name, attrs=attrs)
        return "{blank}<{name}{attrs}>\n{children}\n{blank}</{name}>".format(
            blank=blank, name=self.name, attrs=attrs, children=children
        )
