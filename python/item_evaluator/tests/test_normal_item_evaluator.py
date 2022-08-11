from python.item import Item
from python.item_evaluator.normal_item_evaluator import NormalItemEvaluator

NORMAL_ITEM_NAME = "any string not already used in another name"


class TestNormalItemEvaluator:
    def test_evaluate_does_not_change_item_name(self):
        item = Item(NORMAL_ITEM_NAME, 10, 10)
        evaluator = NormalItemEvaluator()

        result = evaluator.evaluate(item)

        assert result.name == NORMAL_ITEM_NAME

    def test_evaluate_decrements_sell_in_by_1_when_not_expired(self):
        starting_sell_in = 1
        expected_sell_in = 0
        item = Item(NORMAL_ITEM_NAME, starting_sell_in, 10)
        evaluator = NormalItemEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_update__normal_item_quality_decrements_sell_in_by_1_when_expires_today(self):
        starting_sell_in = 0
        expected_sell_in = -1
        item = Item(NORMAL_ITEM_NAME, starting_sell_in, 10)
        evaluator = NormalItemEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_decrements_sell_in_by_1_when_expired(self):
        starting_sell_in = -1
        expected_sell_in = -2
        item = Item(NORMAL_ITEM_NAME, starting_sell_in, 10)
        evaluator = NormalItemEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_decrements_quality_by_1_when_not_expired(self):
        sell_in = 1
        starting_quality = 10
        expected_quality = 9
        item = Item(NORMAL_ITEM_NAME, sell_in, starting_quality)
        evaluator = NormalItemEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_decrements_quality_by_2_when_expires_today(self):
        sell_in = 0
        starting_quality = 10
        expected_quality = 8
        item = Item(NORMAL_ITEM_NAME, sell_in, starting_quality)
        evaluator = NormalItemEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_decrements_quality_by_2_when_expired(self):
        sell_in = -1
        starting_quality = 10
        expected_quality = 8
        item = Item(NORMAL_ITEM_NAME, sell_in, starting_quality)
        evaluator = NormalItemEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_cannot_be_negative_when_not_expired(self):
        sell_in = 1
        starting_quality = 0
        expected_quality = 0
        item = Item(NORMAL_ITEM_NAME, sell_in, starting_quality)
        evaluator = NormalItemEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_cannot_be_negative_when_expires_today_starting_at_0_quality(self):
        sell_in = 0
        starting_quality = 0
        expected_quality = 0
        item = Item(NORMAL_ITEM_NAME, sell_in, starting_quality)
        evaluator = NormalItemEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_cannot_be_negative_when_expires_today_starting_at_1_quality(self):
        sell_in = 0
        starting_quality = 1
        expected_quality = 0
        item = Item(NORMAL_ITEM_NAME, sell_in, starting_quality)
        evaluator = NormalItemEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_cannot_be_negative_when_expired_starting_at_1_quality(self):
        sell_in = -1
        starting_quality = 1
        expected_quality = 0
        item = Item(NORMAL_ITEM_NAME, sell_in, starting_quality)
        evaluator = NormalItemEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_cannot_be_negative_when_expired_starting_at_0_quality(self):
        sell_in = -1
        starting_quality = 0
        expected_quality = 0
        item = Item(NORMAL_ITEM_NAME, sell_in, starting_quality)
        evaluator = NormalItemEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality