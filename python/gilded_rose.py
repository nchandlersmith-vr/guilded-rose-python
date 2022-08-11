# -*- coding: utf-8 -*-
from python.item import Item
from python.item_evaluator_factories.item_evaluator_factory_abstract_class import ItemEvaluatorFactoryAbstractClass
from python.exceptions.exceptions import UnknownItemEvaluatorFactoryException


class GildedRose(object):
    def __init__(self, items: [Item], item_evaluator_factory):
        self.items = items
        self.item_evaluator_factory = item_evaluator_factory()
        self._validate_item_evaluator_factory()

    def update_quality(self) -> None:
        for item in self.items:
            evaluator = self.item_evaluator_factory.create(item.name)
            evaluator.evaluate(item)

    def _validate_item_evaluator_factory(self):
        if not isinstance(self.item_evaluator_factory, ItemEvaluatorFactoryAbstractClass):
            raise UnknownItemEvaluatorFactoryException(self.item_evaluator_factory.__class__)
