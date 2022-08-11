import pytest

from python.gilded_rose import GildedRose
from python.item import Item
from python.item_evaluator_factories.item_evaluator_factory import ItemEvaluatorFactory
from python.exceptions.exceptions import UnknownItemEvaluatorFactoryException

NORMAL_ITEM_NAME = "any string not already used in another name"
AGED_BRIE_NAME = "Aged Brie"
SULFURAS_NAME = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES_NAME = "Backstage passes to a TAFKAL80ETC concert"
MAX_ITEM_QUALITY = 50


class TestGildedRose:
    def test_update_quality_normal_item_does_not_change_item_name(self):
        items = [Item(NORMAL_ITEM_NAME, 10, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.name == NORMAL_ITEM_NAME

    def test_update_quality_normal_item_decrements_sell_in_by_1_when_not_expired(self):
        starting_sell_in = 1
        expected_sell_in = 0
        items = [Item(NORMAL_ITEM_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update__normal_item_quality_decrements_sell_in_by_1_when_expires_today(self):
        starting_sell_in = 0
        expected_sell_in = -1
        items = [Item(NORMAL_ITEM_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_normal_item_decrements_sell_in_by_1_when_expired(self):
        starting_sell_in = -1
        expected_sell_in = -2
        items = [Item(NORMAL_ITEM_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_normal_item_decrements_quality_by_1_when_not_expired(self):
        sell_in = 1
        starting_quality = 10
        expected_quality = 9
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_decrements_quality_by_2_when_expires_today(self):
        sell_in = 0
        starting_quality = 10
        expected_quality = 8
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_decrements_quality_by_2_when_expired(self):
        sell_in = -1
        starting_quality = 10
        expected_quality = 8
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_cannot_be_negative_when_not_expired(self):
        sell_in = 1
        starting_quality = 0
        expected_quality = 0
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_cannot_be_negative_when_expires_today_starting_at_0_quality(self):
        sell_in = 0
        starting_quality = 0
        expected_quality = 0
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_cannot_be_negative_when_expires_today_starting_at_1_quality(self):
        sell_in = 0
        starting_quality = 1
        expected_quality = 0
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_cannot_be_negative_when_expired_starting_at_1_quality(self):
        sell_in = -1
        starting_quality = 1
        expected_quality = 0
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_cannot_be_negative_when_expired_starting_at_0_quality(self):
        sell_in = -1
        starting_quality = 0
        expected_quality = 0
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_aged_brie_does_not_change_item_name(self):
        items = [Item(AGED_BRIE_NAME, 10, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.name == AGED_BRIE_NAME

    def test_update_quality_aged_brie_decrements_sell_in_by_1_when_not_expired(self):
        starting_sell_in = 1
        expected_sell_in = 0
        items = [Item(AGED_BRIE_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_aged_brie_decrements_sell_in_by_1_when_expires_today(self):
        starting_sell_in = 0
        expected_sell_in = -1
        items = [Item(AGED_BRIE_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_aged_brie_decrements_sell_in_by_1_when_expired(self):
        starting_sell_in = -1
        expected_sell_in = -2
        items = [Item(AGED_BRIE_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_aged_brie_increments_quality_by_1_when_not_expired(self):
        sell_in = 1
        starting_quality = 10
        expected_quality = 11
        items = [Item(AGED_BRIE_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_aged_brie_increments_quality_by_2_when_expires_today(self):
        sell_in = 0
        starting_quality = 10
        expected_quality = 12
        items = [Item(AGED_BRIE_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_aged_brie_increments_quality_by_2_when_expired(self):
        sell_in = -1
        starting_quality = 10
        expected_quality = 12
        items = [Item(AGED_BRIE_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_aged_brie_quality_cannot_exceed_max_when_not_expired(self):
        sell_in = 1
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(AGED_BRIE_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_aged_brie_quality_cannot_exceed_max_when_expires_today_starting_quality_at_max(self):
        sell_in = 0
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(AGED_BRIE_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_aged_brie_quality_cannot_exceed_max_when_expires_today_starting_quality_at_max_minus_1(
            self):
        sell_in = 0
        starting_quality = MAX_ITEM_QUALITY - 1
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(AGED_BRIE_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_aged_brie_quality_cannot_exceed_max_when_expired_starting_quality_at_max(self):
        sell_in = -1
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(AGED_BRIE_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_aged_brie_quality_cannot_exceed_max_when_expired_starting_quality_at_max_minus_1(self):
        sell_in = -1
        starting_quality = MAX_ITEM_QUALITY - 1
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(AGED_BRIE_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_sulfuras_does_not_change_item_name(self):
        items = [Item(SULFURAS_NAME, 10, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.name == SULFURAS_NAME

    def test_update_quality_sulfuras_does_not_decrement_sell_in_when_not_expired(self):
        starting_sell_in = 1
        expected_sell_in = 1
        items = [Item(SULFURAS_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_sulfuras_does_not_decrement_sell_in_when_expires_today(self):
        starting_sell_in = 0
        expected_sell_in = 0
        items = [Item(SULFURAS_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_sulfuras_does_not_decrement_sell_in_when_expired(self):
        starting_sell_in = -1
        expected_sell_in = -1
        items = [Item(SULFURAS_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_sulfuras_does_not_degrade_when_not_expired(self):
        sell_in = 1
        starting_quality = 80
        expected_quality = 80
        items = [Item(SULFURAS_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_sulfuras_does_not_degrade_when_expires_today(self):
        sell_in = 0
        starting_quality = 80
        expected_quality = 80
        items = [Item(SULFURAS_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_sulfuras_does_not_degrade_when_expired(self):
        sell_in = -1
        starting_quality = 80
        expected_quality = 80
        items = [Item(SULFURAS_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_does_not_change_item_name(self):
        items = [Item(BACKSTAGE_PASSES_NAME, 10, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.name == BACKSTAGE_PASSES_NAME

    def test_update_quality_backstage_passes_decrements_sell_in_by_1_when_11_days_til_concert(self):
        starting_sell_in = 1
        expected_sell_in = 0
        items = [Item(BACKSTAGE_PASSES_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_backstage_passes_decrements_sell_in_by_1_when_10_days_til_concert(self):
        starting_sell_in = 1
        expected_sell_in = 0
        items = [Item(BACKSTAGE_PASSES_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_backstage_passes_decrements_sell_in_by_5_when_10_days_til_concert(self):
        starting_sell_in = 1
        expected_sell_in = 0
        items = [Item(BACKSTAGE_PASSES_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_backstage_passes_decrements_sell_in_by_1_when_not_expired(self):
        starting_sell_in = 1
        expected_sell_in = 0
        items = [Item(BACKSTAGE_PASSES_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_backstage_passes_decrements_sell_in_by_1_when_expires_today(self):
        starting_sell_in = 0
        expected_sell_in = -1
        items = [Item(BACKSTAGE_PASSES_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_backstage_passes_decrements_sell_in_by_1_when_expired(self):
        starting_sell_in = -1
        expected_sell_in = -2
        items = [Item(BACKSTAGE_PASSES_NAME, starting_sell_in, 10)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_backstage_passes_increases_quality_by_1_when_11_days_til_concert(self):
        sell_in = 11
        starting_quality = 20
        expected_quality = 21
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_quality_does_not_exceed_max_when_11_days_til_concert(self):
        sell_in = 11
        starting_quality = 50
        expected_quality = 50
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_increases_quality_by_2_when_10_days_til_concert(self):
        sell_in = 10
        starting_quality = 20
        expected_quality = 22
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_quality_does_not_exceed_max_when_10_days_til_concert_starting_at_max(self):
        sell_in = 10
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_quality_does_not_exceed_max_when_10_days_til_concert_starting_at_max_minus_1(self):
        sell_in = 10
        starting_quality = MAX_ITEM_QUALITY - 1
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_increases_quality_by_2_when_9_days_til_concert(self):
        sell_in = 9
        starting_quality = 20
        expected_quality = 22
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_quality_does_not_exceed_max_when_9_days_til_concert_starting_at_max(self):
        sell_in = 9
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_quality_does_not_exceed_max_when_9_days_til_concert_starting_at_max_minus_1(self):
        sell_in = 9
        starting_quality = MAX_ITEM_QUALITY - 1
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_increases_quality_by_3_when_5_days_til_concert(self):
        sell_in = 5
        starting_quality = 20
        expected_quality = 23
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_quality_does_not_exceed_max_when_5_days_til_concert_starting_at_max(self):
        sell_in = 5
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_quality_does_not_exceed_max_when_5_days_til_concert_starting_at_max_minus_1(self):
        sell_in = 5
        starting_quality = MAX_ITEM_QUALITY - 1
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_quality_does_not_exceed_max_when_5_days_til_concert_starting_at_max_minus_2(self):
        sell_in = 5
        starting_quality = MAX_ITEM_QUALITY - 2
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_increases_quality_by_3_when_4_days_til_concert(self):
        sell_in = 4
        starting_quality = 20
        expected_quality = 23
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_quality_does_not_exceed_max_when_4_days_til_concert_starting_at_max(self):
        sell_in = 4
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_quality_does_not_exceed_max_when_4_days_til_concert_starting_at_max_minus_1(self):
        sell_in = 4
        starting_quality = MAX_ITEM_QUALITY - 1
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_backstage_passes_quality_does_not_exceed_max_when_4_days_til_concert_starting_at_max_minus_2(self):
        sell_in = 4
        starting_quality = MAX_ITEM_QUALITY - 2
        expected_quality = MAX_ITEM_QUALITY
        items = [Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)]
        item_evaluator_factory = ItemEvaluatorFactory
        app = GildedRose(items, item_evaluator_factory)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_raises_exception_when_known_factory_encountered(self):
        items = [Item("any item", 10, 10)]
        item_evaluator_factory = UnknownItemEvaluatorFactory

        with pytest.raises(UnknownItemEvaluatorFactoryException) as exception_info:
            GildedRose(items, item_evaluator_factory)
        assert str(exception_info.value) == "Expected " \
                                            "<class 'python.tests.test_gilded_rose.UnknownItemEvaluatorFactory'> " \
                                            "to inherit from ItemEvaluatorFactoryAbstractClass"


class UnknownItemEvaluatorFactory:
    def create(self, name: str):
        pass
