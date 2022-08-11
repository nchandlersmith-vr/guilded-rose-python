import pytest


from python.exceptions.exceptions import UnsupportedItem
from python.item_evaluator_factories.item_evaluator_factory import ItemEvaluatorFactory
from python.item_evaluators.sulfuras_evaluator import SulfurasEvaluator

SULFURUS_ITEM_NAME = "Sulfuras, Hand of Ragnaros"


class TestItemEvaluatorFactory:
    def test_create_raises_exception_when_item_name_is_unknown(self):
        unknown_item_name = "unknown"
        with pytest.raises(UnsupportedItem) as exception_info:
            factory = ItemEvaluatorFactory()
            factory.create(unknown_item_name, 10, 10)
        assert str(exception_info.value) == "Attempted to create evaluator for unsupported item with the name: unknown."

    def test_create_creates_a_sulfurus_evaluator(self):
        factory = ItemEvaluatorFactory()

        item = factory.create(SULFURUS_ITEM_NAME, 20, 80)

        assert isinstance(item, SulfurasEvaluator)
