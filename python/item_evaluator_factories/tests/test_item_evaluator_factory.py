import pytest

from python.exceptions.exceptions import UnsupportedItem
from python.item_evaluator_factories.item_evaluator_factory import ItemEvaluatorFactory
from python.item_evaluators.backstage_passes_evaluator import BackstagePassesEvaluator
from python.item_evaluators.sulfuras_evaluator import SulfurasEvaluator
from python.item_evaluators.aged_brie_evaluator import AgedBrieEvaluator


class TestItemEvaluatorFactory:
    def test_create_raises_exception_when_item_name_is_unknown(self):
        unknown_item_name = "unknown"
        with pytest.raises(UnsupportedItem) as exception_info:
            factory = ItemEvaluatorFactory()
            factory.create(unknown_item_name)
        assert str(exception_info.value) == "Attempted to create evaluator for unsupported item with the name: unknown."

    def test_create_creates_a_sulfurus_evaluator(self):
        factory = ItemEvaluatorFactory()
        evaluator = factory.create("Sulfuras, Hand of Ragnaros")
        assert isinstance(evaluator, SulfurasEvaluator)

    def test_create_creates_a_aged_brie_evaluator(self):
        factory = ItemEvaluatorFactory()
        evaluator = factory.create("Aged Brie")
        assert isinstance(evaluator, AgedBrieEvaluator)

    def test_create_creates_a_backstage_passes_evaluator(self):
        factory = ItemEvaluatorFactory()
        evaluator = factory.create("Backstage passes to a TAFKAL80ETC concert")
        assert isinstance(evaluator, BackstagePassesEvaluator)
