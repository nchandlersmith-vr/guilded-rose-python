import pytest

from python.exceptions.exceptions import CannotEvaluateNonItemException
from python.item import Item
from python.item_evaluator.aged_brie_evaluator import AgedBrieEvaluator

AGED_BRIE_NAME = "Aged Brie"
MAX_ITEM_QUALITY = 50


class TestAgedBrieEvaluator:
    def test_evaluate_does_not_change_item_name(self):
        item = Item(AGED_BRIE_NAME, 10, 10)
        evaluator = AgedBrieEvaluator()

        result = evaluator.evaluate(item)

        assert result.name == AGED_BRIE_NAME

    def test_evaluate_decrements_sell_in_by_1_when_not_expired(self):
        starting_sell_in = 1
        expected_sell_in = 0
        item = Item(AGED_BRIE_NAME, starting_sell_in, 10)
        evaluator = AgedBrieEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_decrements_sell_in_by_1_when_expires_today(self):
        starting_sell_in = 0
        expected_sell_in = -1
        item = Item(AGED_BRIE_NAME, starting_sell_in, 10)
        evaluator = AgedBrieEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_decrements_sell_in_by_1_when_expired(self):
        starting_sell_in = -1
        expected_sell_in = -2
        item = Item(AGED_BRIE_NAME, starting_sell_in, 10)
        evaluator = AgedBrieEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_increments_quality_by_1_when_not_expired(self):
        sell_in = 1
        starting_quality = 10
        expected_quality = 11
        item = Item(AGED_BRIE_NAME, sell_in, starting_quality)
        evaluator = AgedBrieEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_increments_quality_by_2_when_expires_today(self):
        sell_in = 0
        starting_quality = 10
        expected_quality = 12
        item = Item(AGED_BRIE_NAME, sell_in, starting_quality)
        evaluator = AgedBrieEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_increments_quality_by_2_when_expired(self):
        sell_in = -1
        starting_quality = 10
        expected_quality = 12
        item = Item(AGED_BRIE_NAME, sell_in, starting_quality)
        evaluator = AgedBrieEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_cannot_exceed_max_when_not_expired(self):
        sell_in = 1
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        item = Item(AGED_BRIE_NAME, sell_in, starting_quality)
        evaluator = AgedBrieEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_cannot_exceed_max_when_expires_today_starting_quality_at_max(self):
        sell_in = 0
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        item = Item(AGED_BRIE_NAME, sell_in, starting_quality)
        evaluator = AgedBrieEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_cannot_exceed_max_when_expires_today_starting_quality_at_max_minus_1(self):
        sell_in = 0
        starting_quality = MAX_ITEM_QUALITY - 1
        expected_quality = MAX_ITEM_QUALITY
        item = Item(AGED_BRIE_NAME, sell_in, starting_quality)
        evaluator = AgedBrieEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_cannot_exceed_max_when_expired_starting_quality_at_max(self):
        sell_in = -1
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        item = Item(AGED_BRIE_NAME, sell_in, starting_quality)
        evaluator = AgedBrieEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_cannot_exceed_max_when_expired_starting_quality_at_max_minus_1(self):
        sell_in = -1
        starting_quality = MAX_ITEM_QUALITY - 1
        expected_quality = MAX_ITEM_QUALITY
        item = Item(AGED_BRIE_NAME, sell_in, starting_quality)
        evaluator = AgedBrieEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_throws_error_when_not_item_input(self):
        with pytest.raises(CannotEvaluateNonItemException) as exc_info:
            evaluator = AgedBrieEvaluator()
            evaluator.evaluate("")
        assert str(exc_info.value) == "Evaluator expected Item. Received <class 'str'>."
