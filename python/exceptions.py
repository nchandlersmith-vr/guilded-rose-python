class CannotEvaluateNonItemException(Exception):
    def __init__(self, object):
        self.message = "Evaluator expected Item. Received {}.".format(object.__class__)
        super().__init__(self.message)