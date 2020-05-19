# -*- coding: utf-8 -*-
import unittest
from python.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_sell_date_expired_and_quality_degrades_twice(self):
        items = [Item("foo", -1, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_negative_quality_value(self):
        items = [Item("foo", 1, -2)]
        gilded_rose = GildedRose(items)
        with self.assertRaises(Exception):
            gilded_rose.update_quality()

    def test_aged_brie_quality_increase_when_get_older(self):
        items = [Item("Aged Brie", 2, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality)
        self.assertEqual(1, items[0].sell_in)

    def test_quality_cant_be_over_50(self):
        items = [Item("foo", 2, 51)]
        gilded_rose = GildedRose(items)
        with self.assertRaises(Exception):
            gilded_rose.update_quality()

    def test_sulfuras_is_not_decreasing_quality(self):
        items = [Item("Sulfuras, Hand of Ragnarose", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_passess_improving_quality_by_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

    def test_backstage_passess_improving_quality_by_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)

    def test_backstage_passess_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_conjured_item_degrade_quality_twice_fast(self):
        items = [Item("Conjured Mana Cake", 2, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)


if __name__ == '__main__':
    unittest.main()
