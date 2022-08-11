from python.item import Item
from python.item_evaluator.item_evaluator import ItemEvaluator
from python.exceptions import CannotEvaluateNonItemException


class SulfurasEvaluator(ItemEvaluator):
    def evaluate(self, item: Item) -> Item:
        if not isinstance(item, Item):
            raise CannotEvaluateNonItemException(item)
        return item
