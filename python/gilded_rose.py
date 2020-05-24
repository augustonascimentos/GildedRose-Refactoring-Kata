# -*- coding: utf-8 -*-
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if not especial_item_case(item):
                decrease_sell_by_day_value_by_one(item)
                decrease_quality_by_one(item)


def decrease_sell_by_day_value_by_one(item):
    item.sell_in -= 1
    return item


def increase_quality_by_one(item):
    item.quality += 1
    return item


def decrease_quality_by_one(item):
    item.quality -= 1
    return item


def decrease_quality_by_two(item):
    item.quality -= 2
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
        return item


def expired_sell_date(item):
    if 'Sulfuras' not in item.name and 'Backstage' not in item.name:
        if item.sell_in < 0:
            item.quality -= 2
            return item


def backstage_passes(item):
    if 'Backstage passes to a TAFKAL80ETC concert' in item.name:
        if 10 >= item.sell_in > 5:
            increase_quality_by_two(item)
            decrease_sell_by_day_value_by_one(item)
            return item
        if 5 >= item.sell_in > 0:
            increase_quality_by_three(item)
            decrease_sell_by_day_value_by_one(item)
            return item
        if item.sell_in < 0:
            item.quality = 0
            decrease_sell_by_day_value_by_one(item)
            return item
        if item.sell_in > 10:
            decrease_sell_by_day_value_by_one(item)
            increase_quality_by_one(item)
            return item


def sulfuras(item):
    if 'Sulfuras' in item.name:
        return item


def conjured_items(item):
    if 'Conjured' in item.name:
        decrease_sell_by_day_value_by_one(item)
        decrease_quality_by_two(item)
        return item


def especial_item_case(item):
    if check_quality_quantity(item):
        return True
    if expired_sell_date(item):
        return True
    if aged_brie_quality_increase_when_get_older(item):
        return True
    if backstage_passes(item):
        return True
    if sulfuras(item):
        return True
    if conjured_items(item):
        return True
    return False


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
