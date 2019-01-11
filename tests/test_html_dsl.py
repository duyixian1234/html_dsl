import pytest
from html_dsl.elements import BaseHtmlElement, HTML, BODY, H1, P, DIV, SPAN


@pytest.fixture
def html():
    yield HTML[
        BODY[
            H1["Title"],
            P(color="yellow")["Hello, World.", SPAN["something in span"], "Out of the span"],
            P["This is the second paragraph."],
            DIV[
                DIV(_class="row")[
                    DIV(_class="column", color="red")["col1"], DIV(_class="column", color="blue")["col2"], DIV(_class="column", color="green")["col3"]
                ]
            ],
        ]
    ]


def test_html(html: BaseHtmlElement):
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
    assert str(html) == output

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
    assert repr(html) == repr_str
