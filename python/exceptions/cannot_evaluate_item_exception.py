class CannotEvaluateItemException(Exception):
    def __init__(self, expected_item_name, actual_item_name):
        self.message = "Evaluator expected {}. Encountered {}.".format(expected_item_name, actual_item_name)
        super().__init__(self.message)
