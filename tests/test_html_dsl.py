import pytest

from html_dsl import common
from html_dsl.elements import BaseHtmlElement, flatten
from html_dsl.common import BODY, DIV, H1, HTML, SPAN, P


@pytest.fixture
def html_content():
    yield HTML[
        BODY[
            H1["Title"],
            P(color="yellow")["Hello, World.", SPAN["something in span"], "Out of the span"],
            P["This is the second paragraph."],
            DIV[
                DIV(_class="row")[
                    DIV(_class="column", color="red")["col1"],
                    DIV(_class="column", color="blue")["col2"],
                    DIV(_class="column", color="green")["col3"],
                ]
            ],
        ]
    ]


def test_flatten():
    assert list(flatten(1)) == [1]
    assert list(flatten("aaa")) == ["aaa"]
    assert list(flatten([1, 2, 3, "aaa"])) == [1, 2, 3, "aaa"]
    assert list(flatten([1, 2, 3, "aaa", [4, 5]])) == [1, 2, 3, "aaa", 4, 5]


def test_html(html_content: BaseHtmlElement):
    output = """<html>
  <body>
    <h1>
    Title
    </h1>
    <p color="yellow">
    Hello, World.
      <span>
      something in span
      </span>
    Out of the span
    </p>
    <p>
    This is the second paragraph.
    </p>
    <div>
      <div class="row">
        <div color="red" class="column">
        col1
        </div>
        <div color="blue" class="column">
        col2
        </div>
        <div color="green" class="column">
        col3
        </div>
      </div>
    </div>
  </body>
</html>"""
    assert str(html_content) == output

    repr_str = """html[
  body[
    h1[
    'Title']
    p(color='yellow')[
    'Hello, World.'
      span[
      'something in span']
    'Out of the span']
    p[
    'This is the second paragraph.']
    div[
      div(class='row')[
        div(color='red';class='column')[
        'col1']
        div(color='blue';class='column')[
        'col2']
        div(color='green';class='column')[
        'col3']]]]]"""
    assert repr(html_content) == repr_str


def test_elements():
    assert all(
        name == value.name.upper()
        for name, value in common.__dict__.items()
        if isinstance(value, common.BaseHtmlElement)
    )


def test_single():
    META = BaseHtmlElement("meta", single=True)
    assert str(META(a="aaa")) == '<meta a="aaa">'
    assert repr(META(a="aaa")) == "meta(a='aaa')"


def test_hyphen():
    assert str(HTML(a_b="a-b")) == '<html a-b="a-b">\n\n</html>'


def test_no_content():
    LINK = BaseHtmlElement("link", no_content=True)
    assert str(LINK(href="//a.css")) == '<link href="//a.css"/>'
    assert repr(LINK(href="//a.css")) == "link(href='//a.css')"
