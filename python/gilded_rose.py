# -*- coding: utf-8 -*-
from python.item_evaluators.sulfuras_evaluator import SulfurasEvaluator
from python.item_evaluators.aged_brie_evaluator import AgedBrieEvaluator
from python.item_evaluators.backstage_passes_evaluator import BackstagePassesEvaluator
from python.item_evaluators.normal_item_evaluator import NormalItemEvaluator


class GildedRose(object):
    SULFURUS = "Sulfuras, Hand of Ragnaros"
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"

    def __init__(self, items):
        self.items = items
        self.evaluator_lookup = {
            GildedRose.SULFURUS: SulfurasEvaluator(),
            GildedRose.AGED_BRIE: AgedBrieEvaluator(),
            GildedRose.BACKSTAGE_PASSES: BackstagePassesEvaluator()
        }

    def update_quality(self):
        for item in self.items:
            if item.name in self.evaluator_lookup.keys():
                self.evaluator_lookup[item.name].evaluate(item)
            else:
                NormalItemEvaluator().evaluate(item)
