from python.item import Item
from python.item_evaluators.item_evaluator import ItemEvaluator
from python.exceptions.cannot_evaluate_non_item_exception import CannotEvaluateNonItemException
from python.exceptions.cannot_evaluate_item_exception import CannotEvaluateItemException


def _validate_item(item):
    if not isinstance(item, Item):
        raise CannotEvaluateNonItemException(item)
    if not item.name == SulfurasEvaluator.SULFURAS_ITEM_NAME:
        raise CannotEvaluateItemException(SulfurasEvaluator.SULFURAS_ITEM_NAME, item.name)


class SulfurasEvaluator(ItemEvaluator):
    SULFURAS_ITEM_NAME = "Sulfuras, Hand of Ragnaros"

    def evaluate(self, item: Item) -> Item:
        _validate_item(item)
        return item
