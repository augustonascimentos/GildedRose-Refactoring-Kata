# -*- coding: utf-8 -*-
def decrease_sell_by_day_value_by_one(item):
    item.sell_in -= 1
    return item


def increase_quality_by_one(item):
    item.quality += 1
    return item


def increase_quality_by_two(item):
    item.quality += 2
    if item.quality > 50:
        item.quality = 50
    return item


def increase_quality_by_three(item):
    item.quality += 3
    if item.quality > 50:
        item.quality = 50
    return item


def check_quality_quantity(item):
    if 'Sulfuras' not in item.name:
        if item.quality > 50:
            raise Exception('Quality can not be over 50')
        if item.quality < 0:
            raise Exception('Quality can not be negative')


def aged_brie_quality_increase_when_get_older(item):
    if 'Aged Brie' in item.name:
        decrease_sell_by_day_value_by_one(item)
        increase_quality_by_one(item)


def expired_sell_date(item):
    if 'Sulfuras' not in item.name:
        if item.sell_in < 0:
            item.quality -= 2


def backstage_passes(item):
    if 'Backstage passes to a TAFKAL80ETC concert' in item.name:
        if item.sell_in <= 10:
            increase_quality_by_two(item)
        if item.sell_in <= 5:
            increase_quality_by_three(item)
        if item.sell_in < 0:
            item.quality = 0


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            check_quality_quantity(item)
            expired_sell_date(item)
            aged_brie_quality_increase_when_get_older(item)
            backstage_passes(item)
            a = 2
            # if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            #     if item.quality > 0:
            #         if item.name != "Sulfuras, Hand of Ragnaros":
            #             item.quality = item.quality - 1
            # else:
            #     if item.quality < 50:
            #         item.quality = item.quality + 1
            #         if item.name == "Backstage passes to a TAFKAL80ETC concert":
            #             if item.sell_in < 11:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            #             if item.sell_in < 6:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            # if item.name != "Sulfuras, Hand of Ragnaros":
            #     item.sell_in = item.sell_in - 1
            # if item.sell_in < 0:
            #     if item.name != "Aged Brie":
            #         if item.name != "Backstage passes to a TAFKAL80ETC concert":
            #             if item.quality > 0:
            #                 if item.name != "Sulfuras, Hand of Ragnaros":
            #                     item.quality = item.quality - 1
            #         else:
            #             item.quality = item.quality - item.quality
            #     else:
            #         if item.quality < 50:
            #             item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
