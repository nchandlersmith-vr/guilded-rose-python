from python.exceptions.exceptions import CannotEvaluateNonItemException
from python.item import Item
from python.item_evaluator.item_evaluator import ItemEvaluator


class NormalItemEvaluator(ItemEvaluator):
    def evaluate(self, item: Item) -> Item:
        if not isinstance(item, Item):
            raise CannotEvaluateNonItemException(item)
        item.quality -= 1
        if item.sell_in < 1:
            item.quality -= 1
        item.quality = max(item.quality, 0)
        item.sell_in -= 1
        return item