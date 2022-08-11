# -*- coding: utf-8 -*-
from python.item import Item


class GildedRose(object):
    def __init__(self, items: [Item], item_evaluator_factory):
        self.items = items
        self.item_evaluator_factory = item_evaluator_factory

    def update_quality(self) -> None:
        for item in self.items:
            evaluator = self.item_evaluator_factory().create(item.name)
            evaluator.evaluate(item)
