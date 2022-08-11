import abc

from python.item_evaluators.item_evaluator import ItemEvaluator


class ItemEvaluatorFactoryAbstractClass(abc.ABC):
    @abc.abstractmethod
    def create(self, name: str, sell_in: int, quantity: int) -> ItemEvaluator:
        pass
