from python.item import Item
from python.item_evaluator.item_evaluator import ItemEvaluator


class BackstagePassesEvaluator(ItemEvaluator):
    def evaluate(self, item: Item) -> Item:
        item.quality += 1
        if item.sell_in < 11:
            item.quality += 1
        if item.sell_in < 6:
            item.quality += 1
        item.quality = min(item.quality, 50)
        item.sell_in -= 1
        return item