from python.item_evaluator_factories.item_evaluator_factory_abstract_class import ItemEvaluatorFactoryAbstractClass
from python.item_evaluators.item_evaluator import ItemEvaluator
from python.item_evaluators.sulfuras_evaluator import SulfurasEvaluator
from python.exceptions.exceptions import UnsupportedItem


class ItemEvaluatorFactory(ItemEvaluatorFactoryAbstractClass):
    SULFURUS_ITEM_NAME = "Sulfuras, Hand of Ragnaros"

    def create(self, name: str, sell_in: int, quantity: int) -> ItemEvaluator:
        if name == ItemEvaluatorFactory.SULFURUS_ITEM_NAME:
            return SulfurasEvaluator()
        raise UnsupportedItem(name)
