import abc

from python.item_evaluators.item_evaluator import ItemEvaluator


class ItemEvaluatorFactoryAbstractClass(abc.ABC):
    @abc.abstractmethod
    def create(self, name: str) -> ItemEvaluator:
        pass
