class CannotEvaluateNonItemException(Exception):
    def __init__(self, object):
        self.message = "Expected Item. Received {}.".format(object.__class__)