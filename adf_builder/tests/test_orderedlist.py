import pytest

from adf_builder.inline.text import Text
from adf_builder.top.code import CodeBlock
from adf_builder.top.list import OrderedList


class TestOrderedList:


    def test_simple_list(self):
        # A simple two point list:
        #   * foo
        #   * bar
        assert OrderedList(
            Text("foo"),
            Text("bar")
        ).to_dict() == {
            "type": "orderedList",
            "attrs": {
                "order": 1
            },
            "content": [
                {
                    "type": "listItem",
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "foo"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "listItem",
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "bar"
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    def test_nested_list(self):
        # A nested list
        #   * foo
        #       - bar
        assert OrderedList(
            Text("foo"),
            OrderedList(
                Text("bar")
            )
        ).to_dict() == {
            "type": "orderedList",
            "attrs": {
                "order": 1
            },
            "content": [
                {
                    "type": "listItem",
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "foo"
                                }
                            ]
                        },
                        {
                            "type": "orderedList",
                            "attrs": {
                                "order": 1
                            },
                            "content": [
                                {
                                    "type": "listItem",
                                    "content": [
                                        {
                                            "type": "paragraph",
                                            "content": [
                                                {
                                                    "type": "text",
                                                    "text": "bar"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    def test_mix_and_match(self):
        # A str and code block list
        #   * foo
        #   * {code}bar{code}
        assert OrderedList(
            Text("foo"),
            CodeBlock("bar", language="java")
        ).to_dict() == {
            "type": "orderedList",
            "attrs": {
                "order": 1
            },
            "content": [
                {
                    "type": "listItem",
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "foo"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "listItem",
                    "content": [
                        {
                            "type": "codeBlock",
                            "attrs": {
                                "language": "java"
                            },
                            "content": [
                                {
                                    "type": "text",
                                    "text": "bar"
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    def test_deeper_nest(self):
        # A nested list
        #   * foo
        #       - bar
        #           . foobar
        assert OrderedList(
            Text("foo"),
            OrderedList(
                Text("bar"),
                OrderedList(
                    Text("foobar")
                )
            )
        ).to_dict() == {
                "type": "orderedList",
                "attrs": {
                    "order": 1
                },
                "content": [
                    {
                        "type": "listItem",
                        "content": [
                            {
                                "type": "paragraph",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": "foo"
                                    }
                                ]
                            },
                            {
                                "type": "orderedList",
                                "attrs": {
                                    "order": 1
                                },
                                "content": [
                                    {
                                        "type": "listItem",
                                        "content": [
                                            {
                                                "type": "paragraph",
                                                "content": [
                                                    {
                                                        "type": "text",
                                                        "text": "bar"
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "orderedList",
                                                "attrs": {
                                                    "order": 1
                                                },
                                                "content": [
                                                    {
                                                        "type": "listItem",
                                                        "content": [
                                                            {
                                                                "type": "paragraph",
                                                                "content": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "foobar"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }

    def test_varied_nesting(self):
        # A nested list
        #   * foo
        #       - bar
        #           . foobar
        #       - foobar
        #   * barfoo
        assert OrderedList(
            Text("foo"),
            OrderedList(
                Text("bar"),
                OrderedList(
                    Text("foobar")
                ),
                Text("foobar")
            ),
            Text("barfoo")
        ).to_dict() == {
            "type": "orderedList",
            "attrs": {
                "order": 1
            },
            "content": [
                {
                    "type": "listItem",
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "foo"
                                }
                            ]
                        },
                        {
                            "type": "orderedList",
                            "attrs": {
                                "order": 1
                            },
                            "content": [
                                {
                                    "type": "listItem",
                                    "content": [
                                        {
                                            "type": "paragraph",
                                            "content": [
                                                {
                                                    "type": "text",
                                                    "text": "bar"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "orderedList",
                                            "attrs": {
                                                "order": 1
                                            },
                                            "content": [
                                                {
                                                    "type": "listItem",
                                                    "content": [
                                                        {
                                                            "type": "paragraph",
                                                            "content": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "foobar"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "listItem",
                                    "content": [
                                        {
                                            "type": "paragraph",
                                            "content": [
                                                {
                                                    "type": "text",
                                                    "text": "foobar"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "listItem",
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "barfoo"
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    def test_maximum_nesting(self):
        assert OrderedList(
            Text("level 0"),
            OrderedList(
                Text("level 1"),
                OrderedList(
                    Text("level 2"),
                    OrderedList(
                        Text("level 3"),
                        OrderedList(
                            Text("level 4"),
                            OrderedList(
                                Text("level 5"),
                            )
                        )
                    )
                )
            )
        ).to_dict() == {
            "type": "orderedList",
            "attrs": {
                "order": 1
            },
            "content": [
                {
                    "type": "listItem",
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "level 0"
                                }
                            ]
                        },
                        {
                            "type": "orderedList",
                            "attrs": {
                                "order": 1
                            },
                            "content": [
                                {
                                    "type": "listItem",
                                    "content": [
                                        {
                                            "type": "paragraph",
                                            "content": [
                                                {
                                                    "type": "text",
                                                    "text": "level 1"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "orderedList",
                                            "attrs": {
                                                "order": 1
                                            },
                                            "content": [
                                                {
                                                    "type": "listItem",
                                                    "content": [
                                                        {
                                                            "type": "paragraph",
                                                            "content": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "level 2"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "orderedList",
                                                            "attrs": {
                                                                "order": 1
                                                            },
                                                            "content": [
                                                                {
                                                                    "type": "listItem",
                                                                    "content": [
                                                                        {
                                                                            "type": "paragraph",
                                                                            "content": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "level 3"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "orderedList",
                                                                            "attrs": {
                                                                                "order": 1
                                                                            },
                                                                            "content": [
                                                                                {
                                                                                    "type": "listItem",
                                                                                    "content": [
                                                                                        {
                                                                                            "type": "paragraph",
                                                                                            "content": [
                                                                                                {
                                                                                                    "type": "text",
                                                                                                    "text": "level 4"
                                                                                                }
                                                                                            ]
                                                                                        },
                                                                                        {
                                                                                            "type": "orderedList",
                                                                                            "attrs": {
                                                                                                "order": 1
                                                                                            },
                                                                                            "content": [
                                                                                                {
                                                                                                    "type": "listItem",
                                                                                                    "content": [
                                                                                                        {
                                                                                                            "type": "paragraph",
                                                                                                            "content": [
                                                                                                                {
                                                                                                                    "type": "text",
                                                                                                                    "text": "level 5"
                                                                                                                }
                                                                                                            ]
                                                                                                        }
                                                                                                    ]
                                                                                                }
                                                                                            ]
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    def test_max_nesting_exceeded(self):
        with pytest.raises(ValueError):
            OrderedList(
                Text("level 0"),
                OrderedList(
                    Text("level 1"),
                    OrderedList(
                        Text("level 2"),
                        OrderedList(
                            Text("level 3"),
                            OrderedList(
                                Text("level 4"),
                                OrderedList(
                                    Text("level 5"),
                                    OrderedList(
                                        Text("this is too much")
                                    )
                                )
                            )
                        )
                    )
                )
            )

    def test_incorrect_nesting(self):
        with pytest.raises(ValueError):
            OrderedList(
                OrderedList(
                    Text("foo")
                )
            )