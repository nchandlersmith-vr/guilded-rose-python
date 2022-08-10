from python.gilded_rose import GildedRose, Item

NORMAL_ITEM_NAME = "normal"


class TestGildedRose:
    def test_update_quality_does_not_change_normal_item_name(self):
        items = [Item(NORMAL_ITEM_NAME, 1, 10)]
        app = GildedRose(items)

        app.update_quality()

        result = app.items[0]

        assert result.name == NORMAL_ITEM_NAME
