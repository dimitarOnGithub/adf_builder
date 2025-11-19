from adf_builder.top.divider import Divider


class TestDivider:

    def test_to_json(self):
        assert Divider().to_dict() == {
            "type": "rule"
        }