class UnknownItemEvaluatorFactoryException(Exception):
    def __init__(self, factory_class):
        self.message = "Expected {} to inherit from ItemEvaluatorFactoryAbstractClass".format(factory_class)
        super().__init__(self.message)
