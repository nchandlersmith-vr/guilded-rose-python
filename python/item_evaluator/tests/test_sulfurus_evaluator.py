import pytest

from python.item_evaluator.sulfuras_evaluator import SulfurasEvaluator
from python.item import Item
from python.exceptions import CannotEvaluateNonItemException

SULFURAS_NAME = "Sulfuras, Hand of Ragnaros"


class TestSulfurasEvaluator:
    def test_update_quality_sulfuras_does_not_change_item_name(self):
        item = Item(SULFURAS_NAME, 10, 10)
        evaluator = SulfurasEvaluator()

        result = evaluator.evaluate(item)

        assert result.name == SULFURAS_NAME

    def test_update_quality_sulfuras_does_not_decrement_sell_in_when_not_expired(self):
        starting_sell_in = 1
        expected_sell_in = 1
        item = Item(SULFURAS_NAME, starting_sell_in, 10)
        evaluator = SulfurasEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_update_quality_sulfuras_does_not_decrement_sell_in_when_expires_today(self):
        starting_sell_in = 0
        expected_sell_in = 0
        item = Item(SULFURAS_NAME, starting_sell_in, 10)
        evaluator = SulfurasEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_update_quality_sulfuras_does_not_decrement_sell_in_when_expired(self):
        starting_sell_in = -1
        expected_sell_in = -1
        item = Item(SULFURAS_NAME, starting_sell_in, 10)
        evaluator = SulfurasEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_update_quality_sulfuras_does_not_degrade_when_not_expired(self):
        sell_in = 1
        starting_quality = 80
        expected_quality = 80
        item = Item(SULFURAS_NAME, sell_in, starting_quality)
        evaluator = SulfurasEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_update_quality_sulfuras_does_not_degrade_when_expires_today(self):
        sell_in = 0
        starting_quality = 80
        expected_quality = 80
        item = Item(SULFURAS_NAME, sell_in, starting_quality)
        evaluator = SulfurasEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_update_quality_sulfuras_does_not_degrade_when_expired(self):
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
