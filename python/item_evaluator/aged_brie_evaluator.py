from python.item import Item
from python.item_evaluator.item_evaluator import ItemEvaluator
from python.exceptions.exceptions import CannotEvaluateNonItemException


class AgedBrieEvaluator(ItemEvaluator):
    def evaluate(self, item: Item) -> Item:
        if not isinstance(item, Item):
            raise CannotEvaluateNonItemException(item)
        if item.sell_in > 0:
            item.quality += 1
        else:
            item.quality += 2
        item.quality = min(item.quality, 50)
        item.sell_in -= 1
        return item
