# adf_builder
Python builder for the Atlassian Document Format (ADF)

# Installation

```bash
pip install adf-builder
```

# Table of Content

<!-- TOC -->
* [Basic plain text](#basic-plain-text)
* [Text with markings](#text-with-markings)
* [Code blocks](#code-blocks)
* [Lists](#lists)
  * [Bullet list](#bullet-list)
  * [Ordered list](#ordered-list)
* [Heading](#heading)
* [Panel](#panel)
* [Quote](#quote)
<!-- TOC -->

### Basic plain text

```python
from adf_builder import ADFDocument
from adf_builder.top import Paragraph
from adf_builder.inline import Text


document = ADFDocument(
    Paragraph(
        Text("This is a simple sentence")
    )
)
print(document.build())
# {'version': 1, 'type': 'doc', 'content': [{'type': 'paragraph', 'content': [{'type': 'text', 'text': 'This is a simple sentence'}]}]}
```
You could also add elements on the fly if that'd be more convenient:
```python
from adf_builder import ADFDocument
from adf_builder.top import Paragraph
from adf_builder.inline import Text

document = ADFDocument()
with open("some_file.txt") as file:
    for line in file.read().splitlines():
        document.add(
            Paragraph(
                Text(f"This {line} will be on a new line in JIRA/Confluence")
            )
        )

print(document.build())
# {"version": 1, "type": "doc", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "This line1 will be on a new line in JIRA/Confluence"}]}, {"type": "paragraph", "content": [{"type": "text", "text": "This line2 will be on a new line in JIRA/Confluence"}]}]}
```
Paragraphs are what dictates if a new line should be inserted or not; the example below will be on the same line:
```
document = ADFDocument(
    Paragraph(
        Text("This is a simple sentence."),
        Text("This sentence will be concatenated to the one above")
    )
)
```
and this will end up on multiple lines in the GUI:
```
document = ADFDocument(
    Paragraph(
        Text("This is a simple sentence.")
    ),
    Paragraph(
        Text("I will be displayed on a new line.")
    )
)
```

### Text with markings

Similarly to the example above, adding markings to a text is done via the `mark` method of the `Text` class. It's 
important to note, that applying a mark will apply it to the entire text provided, so if you need just a portion of your
text marked, you should add it as a separate `Text` entry to the paragraph:
```python
from adf_builder import ADFDocument
from adf_builder.top import Paragraph
from adf_builder.inline import Text
from adf_builder.marks import MarkEnum

document = ADFDocument(
            Paragraph(
                Text(f"The word "),
                Text("this").mark(MarkEnum.BOLD),
                Text("will be bold.")
            )
        )
```
Stylistical marks are available via the `MarkEnum` class, however, if you need to add a link or color to any part of a
text, you need to also import the `Link` and `Color` classes from the `marks` module:
```python
from adf_builder import ADFDocument
from adf_builder.top import Paragraph
from adf_builder.inline import Text
from adf_builder.marks import Link, Color

document = ADFDocument(
            Paragraph(
                Text(f"If you "),
                Text("click here").mark(Link(href="https://icanhas.cheezburger.com/")),
                Text("you'll know I'm old "),
                Text("(and likely immature)").mark(Color("#808080")),
                Text(".")
            )
        )
document.build()
```
Note that some restrictions still apply; for example, you can't combine color with a text that has been marked as a link
or code:
```python
from adf_builder import ADFDocument
from adf_builder.top import Paragraph
from adf_builder.inline import Text
from adf_builder.marks import Link, Color

document = ADFDocument(
            Paragraph(
                Text(f"If you "),
                # This will result in a ValueError being thrown
                Text("click here").mark(Link(href="https://icanhas.cheezburger.com/")).mark(Color("#808080")),
                Text("you'll know I'm old "),
                Text("(and likely immature)"),
                Text(".")
            )
        )
```
Attempting to do so will result in a `ValueError`.

### Code blocks

Code blocks accept a string (the code) and a string value for the `language` keyword; there's no validation on what you 
choose to set for it, the default value is plain text. Atlassian will automatically set it to the same if the value you 
have added fails validation on the product side.
```python
from adf_builder import ADFDocument
from adf_builder.top import CodeBlock

document = ADFDocument(
    CodeBlock(
        ("from adf_builder import ADFDocument\n"
         "from adf_builder.top import CodeBlock\n"
         "doc = ADFDocument(CodeBlock('test code', language='java'))"),
        language="python"
    )
)
```

### Lists

#### Bullet list

Bullet lists take an instance of a `CodeBlock`, `Text` or a nested bullet or ordered list. It's important to note that 
you need to have at least text (code or plain text) entry before being able to add a nested list.

Here's an example of a simple bullet list:
```python
from adf_builder import ADFDocument
from adf_builder.top import BulletList
from adf_builder.inline import Text

# This will be displayed as:
#   * First list item
#   * Second list item
document = ADFDocument(
    BulletList(
        Text("First list item"),
        Text("Second list item")
    )
)
```

Here's an example of a nested list:
```python
from adf_builder import ADFDocument
from adf_builder.top import BulletList
from adf_builder.inline import Text

# This will be displayed as:
#   * First list item
#       - Nested list item
document = ADFDocument(
    BulletList(
        Text("First list item"),
        BulletList(
            Text("Nested list item")
        )
    )
)
```
When nesting even deeper, the nested list needs to be part of the list that's one level above it, that is to say:

```python
from adf_builder import ADFDocument
from adf_builder.top import BulletList
from adf_builder.inline import Text

# Properly nested list and items that will be displayed as:
#   * First list item
#       - Nested list item
#           . Even deeper nest
document = ADFDocument(
    BulletList(
        Text("First list item"),
        BulletList(
            Text("Nested list item"),
            BulletList(
                Text("Even deeper nest")
            ) # <- closes the BulletList for "Even deeper nest"
        ) # <- closes the BulletList for "Nested list item"
    ) # <- closes the BulletList for the "First list item"
)

# Versus improperly nested items:
document = ADFDocument(
    BulletList(
        Text("First list item"),
        BulletList(
            Text("Nested list item"),
        ),
        BulletList(
            Text("Even deeper nest")
        )
    )
)
```

#### Ordered list

Ordered lists follow the same building logic as the bullet lists, with the only difference that you can also provide a 
starting number for the order via the `start_at` keyword:
```python
from adf_builder import ADFDocument
from adf_builder.top import OrderedList
from adf_builder.inline import Text

# This will be displayed as:
#   1. First list item
#   2. Second list item
document = ADFDocument(
    OrderedList(
        Text("First list item"),
        Text("Second list item"),
        start_at=1
    )
)
```

#### Heading

```python
from adf_builder import ADFDocument
from adf_builder.top import Heading
from adf_builder.inline import Text

document  = ADFDocument(
    Heading(
        # Since this is a text node, it can also be marked with the various marks provided
        Text("This is a header"),
        level=1
    )
)
```

#### Panel

```python
from adf_builder import ADFDocument
from adf_builder.top import Paragraph
from adf_builder.top.panel import Panel, PanelType
from adf_builder.inline import Text

document = ADFDocument(
    Panel(
        Paragraph(
            Text("This is an important message in the panel block")
        ),
        panel_type=PanelType.INFO
    )
)
```

#### Quote

```python
from adf_builder import ADFDocument
from adf_builder.top import Quote, Paragraph
from adf_builder.inline import Text

document = ADFDocument(
    Quote(
        Paragraph(
            Text("This is a quote block, just like any text-based block, it will take a paragraph.")
        ),
        Paragraph(
            Text("By using multiple paragraphs, you can build multi-line text.")
        )
    )
)
```