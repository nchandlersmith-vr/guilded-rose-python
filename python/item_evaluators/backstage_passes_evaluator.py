from python.exceptions.cannot_evaluate_non_item_exception import CannotEvaluateNonItemException
from python.exceptions.cannot_evaluate_item_exception import CannotEvaluateItemException
from python.item import Item
from python.item_evaluators.item_evaluator import ItemEvaluator


def _validate_item(item):
    if not isinstance(item, Item):
        raise CannotEvaluateNonItemException(item)
    if not item.name == BackstagePassesEvaluator.BACKSTAGE_PASSES_ITEM_NAME:
        raise CannotEvaluateItemException(BackstagePassesEvaluator.BACKSTAGE_PASSES_ITEM_NAME, item.name)


class BackstagePassesEvaluator(ItemEvaluator):
    BACKSTAGE_PASSES_ITEM_NAME = "Backstage passes to a TAFKAL80ETC concert"

    def evaluate(self, item: Item) -> Item:
        _validate_item(item)
        item.quality += 1
        if item.sell_in < 11:
            item.quality += 1
        if item.sell_in < 6:
            item.quality += 1
        item.quality = min(item.quality, 50)
        item.sell_in -= 1
        return item
