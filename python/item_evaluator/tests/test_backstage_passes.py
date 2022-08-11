from python.item_evaluator.backstage_passes_evaluator import BackstagePassesEvaluator
from python.item import Item

BACKSTAGE_PASSES_NAME = "Backstage passes to a TAFKAL80ETC concert"
MAX_ITEM_QUALITY = 50


class TestBackstagePasses:
    
    def test_evaluate_does_not_change_item_name(self):
        item = Item(BACKSTAGE_PASSES_NAME, 10, 10)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.name == BACKSTAGE_PASSES_NAME

    def test_evaluate_decrements_sell_in_by_1_when_11_days_til_concert(self):
        starting_sell_in = 1
        expected_sell_in = 0
        item = Item(BACKSTAGE_PASSES_NAME, starting_sell_in, 10)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_decrements_sell_in_by_1_when_10_days_til_concert(self):
        starting_sell_in = 1
        expected_sell_in = 0
        item = Item(BACKSTAGE_PASSES_NAME, starting_sell_in, 10)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_decrements_sell_in_by_5_when_10_days_til_concert(self):
        starting_sell_in = 1
        expected_sell_in = 0
        item = Item(BACKSTAGE_PASSES_NAME, starting_sell_in, 10)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_decrements_sell_in_by_1_when_not_expired(self):
        starting_sell_in = 1
        expected_sell_in = 0
        item = Item(BACKSTAGE_PASSES_NAME, starting_sell_in, 10)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_decrements_sell_in_by_1_when_expires_today(self):
        starting_sell_in = 0
        expected_sell_in = -1
        item = Item(BACKSTAGE_PASSES_NAME, starting_sell_in, 10)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_decrements_sell_in_by_1_when_expired(self):
        starting_sell_in = -1
        expected_sell_in = -2
        item = Item(BACKSTAGE_PASSES_NAME, starting_sell_in, 10)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.sell_in == expected_sell_in

    def test_evaluate_increases_quality_by_1_when_11_days_til_concert(self):
        sell_in = 11
        starting_quality = 20
        expected_quality = 21
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_does_not_exceed_max_when_11_days_til_concert(self):
        sell_in = 11
        starting_quality = 50
        expected_quality = 50
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_increases_quality_by_2_when_10_days_til_concert(self):
        sell_in = 10
        starting_quality = 20
        expected_quality = 22
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_does_not_exceed_max_when_10_days_til_concert_starting_at_max(self):
        sell_in = 10
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_does_not_exceed_max_when_10_days_til_concert_starting_at_max_minus_1(self):
        sell_in = 10
        starting_quality = MAX_ITEM_QUALITY - 1
        expected_quality = MAX_ITEM_QUALITY
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_increases_quality_by_2_when_9_days_til_concert(self):
        sell_in = 9
        starting_quality = 20
        expected_quality = 22
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_does_not_exceed_max_when_9_days_til_concert_starting_at_max(self):
        sell_in = 9
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_does_not_exceed_max_when_9_days_til_concert_starting_at_max_minus_1(self):
        sell_in = 9
        starting_quality = MAX_ITEM_QUALITY - 1
        expected_quality = MAX_ITEM_QUALITY
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_increases_quality_by_3_when_5_days_til_concert(self):
        sell_in = 5
        starting_quality = 20
        expected_quality = 23
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_does_not_exceed_max_when_5_days_til_concert_starting_at_max(self):
        sell_in = 5
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_does_not_exceed_max_when_5_days_til_concert_starting_at_max_minus_1(self):
        sell_in = 5
        starting_quality = MAX_ITEM_QUALITY - 1
        expected_quality = MAX_ITEM_QUALITY
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_does_not_exceed_max_when_5_days_til_concert_starting_at_max_minus_2(self):
        sell_in = 5
        starting_quality = MAX_ITEM_QUALITY - 2
        expected_quality = MAX_ITEM_QUALITY
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_increases_quality_by_3_when_4_days_til_concert(self):
        sell_in = 4
        starting_quality = 20
        expected_quality = 23
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_does_not_exceed_max_when_4_days_til_concert_starting_at_max(self):
        sell_in = 4
        starting_quality = MAX_ITEM_QUALITY
        expected_quality = MAX_ITEM_QUALITY
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_does_not_exceed_max_when_4_days_til_concert_starting_at_max_minus_1(self):
        sell_in = 4
        starting_quality = MAX_ITEM_QUALITY - 1
        expected_quality = MAX_ITEM_QUALITY
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality

    def test_evaluate_quality_does_not_exceed_max_when_4_days_til_concert_starting_at_max_minus_2(self):
        sell_in = 4
        starting_quality = MAX_ITEM_QUALITY - 2
        expected_quality = MAX_ITEM_QUALITY
        item = Item(BACKSTAGE_PASSES_NAME, sell_in, starting_quality)
        evaluator = BackstagePassesEvaluator()

        result = evaluator.evaluate(item)

        assert result.quality == expected_quality