from python.item import Item
from python.item_evaluators.item_evaluator import ItemEvaluator
from python.exceptions.exceptions import CannotEvaluateNonItemException, CannotEvaluateItemException


def _validate_item(item):
    if not isinstance(item, Item):
        raise CannotEvaluateNonItemException(item)
    if item.name != AgedBrieEvaluator.AGED_BRIE_ITEM_NAME:
        raise CannotEvaluateItemException(AgedBrieEvaluator.AGED_BRIE_ITEM_NAME, item.name)


class AgedBrieEvaluator(ItemEvaluator):
    AGED_BRIE_ITEM_NAME = "Aged Brie"

    def evaluate(self, item: Item) -> Item:
        _validate_item(item)
        if item.sell_in > 0:
            item.quality += 1
        else:
            item.quality += 2
        item.quality = min(item.quality, 50)
        item.sell_in -= 1
        return item
