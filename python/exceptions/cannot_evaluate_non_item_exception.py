class CannotEvaluateNonItemException(Exception):
    def __init__(self, obj):
        self.message = "Evaluator expected Item. Received {}.".format(obj.__class__)
        super().__init__(self.message)

