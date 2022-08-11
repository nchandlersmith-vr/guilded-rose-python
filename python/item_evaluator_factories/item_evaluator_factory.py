from python.item_evaluator_factories.item_evaluator_factory_abstract_class import ItemEvaluatorFactoryAbstractClass
from python.item_evaluators.item_evaluator import ItemEvaluator
from python.exceptions.exceptions import UnsupportedItem


class ItemEvaluatorFactory(ItemEvaluatorFactoryAbstractClass):
    def create(self, item_name: str) -> ItemEvaluator:
        raise UnsupportedItem(item_name)
