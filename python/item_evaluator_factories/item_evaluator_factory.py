from python.item_evaluator_factories.item_evaluator_factory_abstract_class import ItemEvaluatorFactoryAbstractClass
from python.item_evaluators.aged_brie_evaluator import AgedBrieEvaluator
from python.item_evaluators.backstage_passes_evaluator import BackstagePassesEvaluator
from python.item_evaluators.item_evaluator import ItemEvaluator
from python.item_evaluators.sulfuras_evaluator import SulfurasEvaluator
from python.item_evaluators.normal_item_evaluator import NormalItemEvaluator


class ItemEvaluatorFactory(ItemEvaluatorFactoryAbstractClass):
    SULFURUS_ITEM_NAME = "Sulfuras, Hand of Ragnaros"
    AGED_BRIE_ITEM_NAME = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    lookup = {
        SULFURUS_ITEM_NAME: SulfurasEvaluator(),
        AGED_BRIE_ITEM_NAME: AgedBrieEvaluator(),
        BACKSTAGE_PASSES: BackstagePassesEvaluator()
    }

    def create(self, name: str) -> ItemEvaluator:
        if name not in ItemEvaluatorFactory.lookup.keys():
            return NormalItemEvaluator()
        return ItemEvaluatorFactory.lookup[name]
