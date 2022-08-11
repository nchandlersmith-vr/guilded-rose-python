import abc

from python.item import Item


class ItemEvaluator(abc.ABC):
    @abc.abstractmethod
    def evaluate(self, item: Item) -> Item:
        pass
