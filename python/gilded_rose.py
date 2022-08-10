# -*- coding: utf-8 -*-

class GildedRose(object):
    SULFURUS = "Sulfuras, Hand of Ragnaros"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == GildedRose.SULFURUS:
                pass
            if self._item_is_normal(item):
                self._safe_degrade_quality(item)
            else:
                self._backstage_pass_rules(item)
            self._safe_decrement_sell_in(item)
            self._expiration_rules(item)

    def _expiration_rules(self, item):
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1

    def _backstage_pass_rules(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 11:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                if item.sell_in < 6:
                    if item.quality < 50:
                        item.quality = item.quality + 1

    def _safe_decrement_sell_in(self, item):
        if self._item_is_not_sulfurus(item):
            item.sell_in = item.sell_in - 1

    def _safe_degrade_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def _item_is_normal(self, item):
        return item.name != "Aged Brie" \
               and item.name != "Backstage passes to a TAFKAL80ETC concert" \
               and item.name != "Sulfuras, Hand of Ragnaros"

    def _item_is_not_sulfurus(self, item):
        return item.name != "Sulfuras, Hand of Ragnaros"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
