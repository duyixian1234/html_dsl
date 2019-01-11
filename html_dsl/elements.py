from typing import Optional


class BaseHtmlElement:
    def __init__(self, name: str):
        self.name = name
        self.attrs: dict = {}
        self.children: list = []
        self.parent: Optional[BaseHtmlElement] = None

    def __call__(self, **attrs) -> "BaseHtmlElement":
        element = BaseHtmlElement(self.name)
        if "_class" in attrs:
            attrs["class"] = attrs.pop("_class")
        element.attrs.update(attrs)
        element.parent = self.parent
        return element

    def __getitem__(self, elements) -> "BaseHtmlElement":
        element = BaseHtmlElement(self.name)
        element.attrs.update(self.attrs)
        if isinstance(elements, tuple):
            for one in elements:
                if isinstance(one, BaseHtmlElement):
                    one.parent = element
            element.children.extend(elements)
        else:
            if isinstance(elements, BaseHtmlElement):
                elements.parent = element
            element.children.append(elements)
        return element

    @property
    def level(self):
        return self.parent.level + 1 if self.parent else 0

    def __repr__(self):
        blank = "  " * self.level
        attrs = "({})".format(";".join(f"{key}={repr(self.attrs[key])}" for key in self.attrs)) if self.attrs else ""
        children = "\n".join(repr(child) if isinstance(child, BaseHtmlElement) else blank + repr(child) for child in self.children)
        return "{blank}{name}{attrs}[\n{children}]".format(blank=blank, name=self.name, attrs=attrs, children=children)

    def __str__(self):
        blank = "  " * self.level
        attrs = " {}".format(" ".join(f'{key}="{str(self.attrs[key])}"' for key in self.attrs)) if self.attrs else ""
        children = "\n".join(str(child) if isinstance(child, BaseHtmlElement) else blank + str(child) for child in self.children)
        return "{blank}<{name}{attrs}>\n{children}\n{blank}</{name}>".format(blank=blank, name=self.name, attrs=attrs, children=children)


HTML = BaseHtmlElement("html")
BODY = BaseHtmlElement("body")
P = BaseHtmlElement("p")
DIV = BaseHtmlElement("div")
H1 = BaseHtmlElement("h1")
SPAN = BaseHtmlElement("span")

__all__ = ("BaseHtmlElement", "HTML", "BODY", "P", "DIV", "H1", "SPAN")
