# -*- coding: utf-8 -*-
from python.item import Item
from python.item_evaluator_factories.item_evaluator_factory import ItemEvaluatorFactory


class GildedRose(object):
    SULFURUS = "Sulfuras, Hand of Ragnaros"
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"

    def __init__(self, items: [Item]):
        self.items = items
        self.item_evaluator_factory = ItemEvaluatorFactory()

    def update_quality(self):
        for item in self.items:
            evaluator = self.item_evaluator_factory.create(item.name)
            evaluator.evaluate(item)
