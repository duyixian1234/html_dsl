from collections.abc import Iterable
from typing import Any, Optional


def flatten(source: Any):
    if isinstance(source, str):
        yield source
    elif isinstance(source, Iterable):
        for element in source:
            yield from flatten(element)
    else:
        yield source


class BaseHtmlElement:
    def __init__(self, name: str, single: bool = False, no_content: bool = False):
        self.name = name
        self.attrs: dict = {}
        self.children: list = []
        self.parent: Optional[BaseHtmlElement] = None
        self.single = single
        self.no_content = no_content

    def __call__(self, **attrs) -> "BaseHtmlElement":
        element = BaseHtmlElement(self.name)
        if "_class" in attrs:
            attrs["class"] = attrs.pop("_class")
        element.attrs.update(attrs)
        element.parent = self.parent
        element.single = self.single
        element.no_content = self.no_content
        return element

    def __getitem__(self, children) -> "BaseHtmlElement":
        element = BaseHtmlElement(self.name)
        element.attrs.update(self.attrs)
        true_children = list(flatten(children))
        for one in true_children:
            if isinstance(one, BaseHtmlElement):
                one.parent = element
        element.children.extend(true_children)
        element.single = self.single
        element.no_content = self.no_content
        return element

    @property
    def level(self):
        return self.parent.level + 1 if self.parent else 0

    def __repr__(self):
        blank = "  " * self.level
        attrs = "({})".format(";".join(f"{key}={repr(self.attrs[key])}" for key in self.attrs)) if self.attrs else ""
        children = "\n".join(repr(child) if isinstance(child, BaseHtmlElement) else blank + repr(child) for child in self.children)
        if self.single or self.no_content:
            return "{blank}{name}{attrs}".format(blank=blank, name=self.name, attrs=attrs)
        return "{blank}{name}{attrs}[\n{children}]".format(blank=blank, name=self.name, attrs=attrs, children=children)

    def __str__(self):
        blank = "  " * self.level
        attrs = " {}".format(" ".join(f'{key.replace("_", "-")}="{str(self.attrs[key])}"' for key in self.attrs)) if self.attrs else ""
        children = "\n".join(str(child) if isinstance(child, BaseHtmlElement) else blank + str(child) for child in self.children)
        if self.single:
            return "{blank}<{name}{attrs}>".format(blank=blank, name=self.name, attrs=attrs)
        elif self.no_content:
            return "{blank}<{name}{attrs}/>".format(blank=blank, name=self.name, attrs=attrs)
        return "{blank}<{name}{attrs}>\n{children}\n{blank}</{name}>".format(blank=blank, name=self.name, attrs=attrs, children=children)


A = BaseHtmlElement("a")
ABBR = BaseHtmlElement("abbr")
ADDRESS = BaseHtmlElement("address")
AREA = BaseHtmlElement("area")
ARTICLE = BaseHtmlElement("article")
ASIDE = BaseHtmlElement("aside")
AUDIO = BaseHtmlElement("audio")
B = BaseHtmlElement("b")
BASE = BaseHtmlElement("base")
BLOCKQUOTE = BaseHtmlElement("blockquote")
BODY = BaseHtmlElement("body")
BR = BaseHtmlElement("br", no_content=True)
BUTTON = BaseHtmlElement("button")
CANVAS = BaseHtmlElement("canvas")
CAPTION = BaseHtmlElement("caption")
CODE = BaseHtmlElement("code")
COL = BaseHtmlElement("col")
COLGROUP = BaseHtmlElement("colgroup")
CONTENT = BaseHtmlElement("content")
DATA = BaseHtmlElement("data")
DATALIST = BaseHtmlElement("datalist")
DD = BaseHtmlElement("dd")
DEL = BaseHtmlElement("del")
DETAILS = BaseHtmlElement("details")
DIALOG = BaseHtmlElement("dialog")
DIR = BaseHtmlElement("dir")
DIV = BaseHtmlElement("div")
DL = BaseHtmlElement("dl")
DT = BaseHtmlElement("dt")
ELEMENT = BaseHtmlElement("element")
EM = BaseHtmlElement("em")
EMBED = BaseHtmlElement("embed")
FIGURE = BaseHtmlElement("figure")
FOOTER = BaseHtmlElement("footer")
FORM = BaseHtmlElement("form")
H1 = BaseHtmlElement("h1")
H2 = BaseHtmlElement("h2")
H3 = BaseHtmlElement("h3")
H4 = BaseHtmlElement("h4")
H5 = BaseHtmlElement("h5")
H6 = BaseHtmlElement("h6")
HEAD = BaseHtmlElement("head")
HGROUP = BaseHtmlElement("hgroup")
HR = BaseHtmlElement("hr")
HTML = BaseHtmlElement("html")
IFRAME = BaseHtmlElement("iframe")
IMG = BaseHtmlElement("img")
INPUT = BaseHtmlElement("input")
INS = BaseHtmlElement("ins")
LABEL = BaseHtmlElement("label")
LEGEND = BaseHtmlElement("legend")
LI = BaseHtmlElement("li")
LINK = BaseHtmlElement("link", no_content=True)
MAIN = BaseHtmlElement("main")
MAP = BaseHtmlElement("map")
MARK = BaseHtmlElement("mark")
MENU = BaseHtmlElement("menu")
MENUITEM = BaseHtmlElement("menuitem")
META = BaseHtmlElement("meta", single=True)
NAV = BaseHtmlElement("nav")
NOSCRIPT = BaseHtmlElement("noscript")
OBJECT = BaseHtmlElement("object")
OL = BaseHtmlElement("ol")
OPTGROUP = BaseHtmlElement("optgroup")
OPTION = BaseHtmlElement("option")
OUTPUT = BaseHtmlElement("output")
P = BaseHtmlElement("p")
PARAM = BaseHtmlElement("param")
PICTURE = BaseHtmlElement("picture")
PRE = BaseHtmlElement("pre")
PROGESS = BaseHtmlElement("progess")
S = BaseHtmlElement("s")
SCRIPT = BaseHtmlElement("script")
SECTION = BaseHtmlElement("section")
SELECT = BaseHtmlElement("select")
SHADOW = BaseHtmlElement("shadow")
SLOT = BaseHtmlElement("slot")
SMALL = BaseHtmlElement("small")
SOURCE = BaseHtmlElement("source")
SPAN = BaseHtmlElement("span")
STRONG = BaseHtmlElement("strong")
STYLE = BaseHtmlElement("style")
SUB = BaseHtmlElement("sub")
SUMMARY = BaseHtmlElement("summary")
TABLE = BaseHtmlElement("table")
TD = BaseHtmlElement("td")
TEMPLATE = BaseHtmlElement("template")
TEXTAREA = BaseHtmlElement("textarea")
TFOOT = BaseHtmlElement("tfoot")
TH = BaseHtmlElement("th")
THEAD = BaseHtmlElement("thead")
TIME = BaseHtmlElement("time")
TITLE = BaseHtmlElement("title")
TR = BaseHtmlElement("tr")
TRACK = BaseHtmlElement("track")
U = BaseHtmlElement("u")
UL = BaseHtmlElement("ul")
VAR = BaseHtmlElement("var")
VIDEO = BaseHtmlElement("video")
