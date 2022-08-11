class CannotEvaluateNonItemException(Exception):
    def __init__(self, obj):
        self.message = "Evaluator expected Item. Received {}.".format(obj.__class__)
        super().__init__(self.message)


class CannotEvaluateItemException(Exception):
    def __init__(self, expected_item_name, actual_item_name):
        self.message = "Evaluator expected {}. Encountered {}.".format(expected_item_name, actual_item_name)
        super().__init__(self.message)

