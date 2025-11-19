from adf_builder.base import TopLevelNode


class Divider(TopLevelNode):

    def to_dict(self):
        return {
            "type": "rule"
        }
