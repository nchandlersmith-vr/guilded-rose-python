import pytest


from python.exceptions.exceptions import UnsupportedItem
from python.item_evaluator_factories.item_evaluator_factory import ItemEvaluatorFactory


class TestItemEvaluatorFactory:
    def test_create_raises_exception_when_item_name_is_unknown(self):
        unknown_item_name = "unknown"
        with pytest.raises(UnsupportedItem) as exception_info:
            factory = ItemEvaluatorFactory()
            factory.create(unknown_item_name)
        assert str(exception_info.value) == "Attempted to create evaluator for unsupported item with the name: unknown."
