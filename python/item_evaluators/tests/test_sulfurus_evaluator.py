import pytest

from python.item_evaluators.sulfuras_evaluator import SulfurasEvaluator
from python.item import Item
from python.exceptions.cannot_evaluate_item_exception import CannotEvaluateItemException
from python.exceptions.cannot_evaluate_non_item_exception import CannotEvaluateNonItemException

SULFURAS_NAME = "Sulfuras, Hand of Ragnaros"


class TestSulfurasEvaluator:
    def test_evaluate_does_not_change_item_name(self):
        item = Item(SULFURAS_NAME, 10, 10)
        evaluator = SulfurasEvaluator()

        result = evaluator.evaluate(item)

        assert result.name == SULFURAS_NAME

    def test_evaluate_does_not_decrement_sell_in_when_not_expired(self):
        starting_sell_in = 1
        expected_sell_in = 1
        item = Item(SULFURAS_NAME, starting_sell_in, 10)
        evaluator = SulfurasEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_does_not_decrement_sell_in_when_expires_today(self):
        starting_sell_in = 0
        expected_sell_in = 0
        item = Item(SULFURAS_NAME, starting_sell_in, 10)
        evaluator = SulfurasEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_does_not_decrement_sell_in_when_expired(self):
        starting_sell_in = -1
        expected_sell_in = -1
        item = Item(SULFURAS_NAME, starting_sell_in, 10)
        evaluator = SulfurasEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_does_not_degrade_when_not_expired(self):
        sell_in = 1
        starting_quality = 80
        expected_quality = 80
        item = Item(SULFURAS_NAME, sell_in, starting_quality)
        evaluator = SulfurasEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_does_not_degrade_when_expires_today(self):
        sell_in = 0
        starting_quality = 80
        expected_quality = 80
        item = Item(SULFURAS_NAME, sell_in, starting_quality)
        evaluator = SulfurasEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_does_not_degrade_when_expired(self):
        sell_in = -1
        starting_quality = 80
        expected_quality = 80
        item = Item(SULFURAS_NAME, sell_in, starting_quality)
        evaluator = SulfurasEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_throws_error_when_not_item_input(self):
        with pytest.raises(CannotEvaluateNonItemException) as exc_info:
            evaluator = SulfurasEvaluator()
            evaluator.evaluate("")
        assert str(exc_info.value) == "Evaluator expected Item. Received <class 'str'>."

    def test_evaluate_throws_error_when_item_not_aged_brie(self):
        with pytest.raises(CannotEvaluateItemException) as exc_info:
            evaluator = SulfurasEvaluator()
            evaluator.evaluate(Item("Aged Brie", 10, 10))
        assert str(exc_info.value) == "Evaluator expected Sulfuras, Hand of Ragnaros. Encountered Aged Brie."
