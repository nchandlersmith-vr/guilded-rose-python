from python.gilded_rose import GildedRose, Item

NORMAL_ITEM_NAME = "normal"
AGED_BRIE_NAME = "Aged Brie"


class TestGildedRose:
    def test_update_quality_normal_item_does_not_change_normal_item_name(self):
        items = [Item(NORMAL_ITEM_NAME, 10, 10)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.name == NORMAL_ITEM_NAME

    def test_update_quality_normal_item_decrements_sell_in_by_1_when_not_expired(self):
        starting_sell_in = 1
        expected_sell_in = 0
        items = [Item(NORMAL_ITEM_NAME, starting_sell_in, 10)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update__normal_item_quality_decrements_sell_in_by_1_when_expires_today(self):
        starting_sell_in = 0
        expected_sell_in = -1
        items = [Item(NORMAL_ITEM_NAME, starting_sell_in, 10)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_normal_item_decrements_sell_in_by_1_when_expired(self):
        starting_sell_in = -1
        expected_sell_in = -2
        items = [Item(NORMAL_ITEM_NAME, starting_sell_in, 10)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_normal_item_decrements_quality_by_1_when_not_expired(self):
        sell_in = 1
        starting_quality = 10
        expected_quality = 9
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_decrements_quality_by_2_when_expires_today(self):
        sell_in = 0
        starting_quality = 10
        expected_quality = 8
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_decrements_quality_by_2_when_expired(self):
        sell_in = -1
        starting_quality = 10
        expected_quality = 8
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_cannot_be_negative_when_not_expired(self):
        sell_in = 1
        starting_quality = 0
        expected_quality = 0
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_cannot_be_negative_when_expires_today_starting_at_0_quality(self):
        sell_in = 0
        starting_quality = 0
        expected_quality = 0
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_cannot_be_negative_when_expires_today_starting_at_1_quality(self):
        sell_in = 0
        starting_quality = 1
        expected_quality = 0
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_cannot_be_negative_when_expired_starting_at_1_quality(self):
        sell_in = -1
        starting_quality = 1
        expected_quality = 0
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_normal_item_cannot_be_negative_when_expired_starting_at_0_quality(self):
        sell_in = -1
        starting_quality = 0
        expected_quality = 0
        items = [Item(NORMAL_ITEM_NAME, sell_in, starting_quality)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_aged_brie_does_not_change_normal_item_name(self):
        items = [Item(AGED_BRIE_NAME, 10, 10)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.name == AGED_BRIE_NAME

    def test_update_quality_aged_brie_decrements_sell_in_by_1_when_not_expired(self):
        starting_sell_in = 1
        expected_sell_in = 0
        items = [Item(AGED_BRIE_NAME, starting_sell_in, 10)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_aged_brie_decrements_sell_in_by_1_when_expires_today(self):
        starting_sell_in = 0
        expected_sell_in = -1
        items = [Item(AGED_BRIE_NAME, starting_sell_in, 10)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_aged_brie_decrements_sell_in_by_1_when_expired(self):
        starting_sell_in = -1
        expected_sell_in = -2
        items = [Item(AGED_BRIE_NAME, starting_sell_in, 10)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.sell_in == expected_sell_in

    def test_update_quality_aged_brie_increments_quality_by_1_when_not_expired(self):
        sell_in = 1
        starting_quality = 10
        expected_quality = 11
        items = [Item(AGED_BRIE_NAME, sell_in, starting_quality)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_aged_brie_increments_quality_by_2_when_expires_today(self):
        sell_in = 0
        starting_quality = 10
        expected_quality = 12
        items = [Item(AGED_BRIE_NAME, sell_in, starting_quality)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality

    def test_update_quality_aged_brie_increments_quality_by_2_when_expired(self):
        sell_in = -1
        starting_quality = 10
        expected_quality = 12
        items = [Item(AGED_BRIE_NAME, sell_in, starting_quality)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.quality == expected_quality
