import pytest
from adf_builder.inline.text import Text
from adf_builder.top.code import CodeBlock
from adf_builder.top.list import BulletList


class TestBulletList:


    def test_simple_list(self):
        # A simple two point list:
        #   * foo
        #   * bar
        assert BulletList(
            Text("foo"),
            Text("bar")
        ).to_dict() == {
            "type": "bulletList",
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
        assert BulletList(
            Text("foo"),
            BulletList(
                Text("bar")
            ),
        ).to_dict() == {
            "type": "bulletList",
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
                            "type": "bulletList",
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
        assert BulletList(
            Text("foo"),
            CodeBlock("bar", language="java")
        ).to_dict() == {
            "type": "bulletList",
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
        assert BulletList(
            Text("foo"),
            BulletList(
                Text("bar"),
                BulletList(
                    Text("foobar")
                )
            )
        ).to_dict() == {
            "type": "bulletList",
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
                            "type": "bulletList",
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
                                            "type": "bulletList",
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
        assert BulletList(
            Text("foo"),
            BulletList(
                Text("bar"),
                BulletList(
                    Text("foobar")
                ),
                Text("foobar")
            ),
            Text("barfoo")
        ).to_dict() == {
            "type": "bulletList",
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
                            "type": "bulletList",
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
                                            "type": "bulletList",
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
        assert BulletList(
            Text("level 0"),
            BulletList(
                Text("level 1"),
                BulletList(
                    Text("level 2"),
                    BulletList(
                        Text("level 3"),
                        BulletList(
                            Text("level 4"),
                            BulletList(
                                Text("level 5"),
                            )
                        )
                    )
                )
            )
        ).to_dict() == {
            "type": "bulletList",
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
                            "type": "bulletList",
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
                                            "type": "bulletList",
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
                                                            "type": "bulletList",
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
                                                                            "type": "bulletList",
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
                                                                                            "type": "bulletList",
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
            BulletList(
                Text("level 0"),
                BulletList(
                    Text("level 1"),
                    BulletList(
                        Text("level 2"),
                        BulletList(
                            Text("level 3"),
                            BulletList(
                                Text("level 4"),
                                BulletList(
                                    Text("level 5"),
                                    BulletList(
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
            BulletList(
                BulletList(
                    Text("foo")
                )
            )
