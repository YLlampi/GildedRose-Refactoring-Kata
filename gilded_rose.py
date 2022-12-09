# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

            if item.name == "Aged brie":
                self.age_brie_funtion(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.backstage_funtion(item)
            elif item.name == "Conjured Mana Cake":
                self.conjured_funtion(item)
            elif item.name != "Sulfuras, Hand of Ragnaros":
                self.common_funtion(item)

            if item.quality > 50:
                item.quality = 50

            if item.quality < 0:
                item.quality = 0

    def age_brie_funtion(self, item):
        if item.sell_in < 0:
            item.quality += 2
        else:
            item.quality += 1

    def backstage_funtion(self, item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1

    def conjured_funtion(self, item):
        item.quality -= 2

    def common_funtion(self, item):

        if item.sell_in < 0:
            item.quality -= 2
        else:
            item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
