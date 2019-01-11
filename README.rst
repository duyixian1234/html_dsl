html-dsl
--------
A HTML-DSL for Python

USE
---


>>> from html_dsl.elements import BaseHtmlElement, HTML, BODY, H1, P, DIV, SPAN
>>> html = HTML[
        BODY[
            H1["Title"],
            P(color="yellow")[
                "Hello, World.", SPAN["something in span"], "Out of the span"
            ],
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
>>> print(html)
<html>
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
</html>

Install
-------

.. code-block:: shell
    
    pip install html_dsl


Author
------
Yixian Du