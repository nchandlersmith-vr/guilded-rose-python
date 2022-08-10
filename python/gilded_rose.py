# -*- coding: utf-8 -*-

class GildedRose(object):
    SULFURUS = "Sulfuras, Hand of Ragnaros"
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == GildedRose.SULFURUS:
                pass  # sulfurus does not degrade
                break
            elif item.name == GildedRose.AGED_BRIE:
                if item.sell_in > 0:
                    item.quality += 1
                else:
                    item.quality += 2
                item.quality = min(item.quality, 50)
                item.sell_in -= 1
                break
            elif item.name == GildedRose.BACKSTAGE_PASSES:
                item.quality += 1
                if item.sell_in < 11:
                    item.quality += 1
                if item.sell_in < 6:
                    item.quality += 1
                item.quality = min(item.quality, 50)
                item.sell_in -= 1
                break
            else:
                item.quality -= 1
                if item.sell_in < 1:
                    item.quality -= 1
                item.quality = max(item.quality, 0)
                item.sell_in -= 1
                break


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
