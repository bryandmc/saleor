from __future__ import unicode_literals

from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from prices import Price
from satchless.item import ItemSet


class BaseDelivery(ItemSet):
    group = None
    name = ''

    def __iter__(self):
        return iter(self.group)

    def get_delivery_total(self, **kwargs):
        return Price(0, currency=settings.DEFAULT_CURRENCY)

    def get_total_with_delivery(self):
        return self.group.get_total() + self.get_delivery_total()


@python_2_unicode_compatible
class DummyShipping(BaseDelivery):
    name = 'dummy_shipping'

    def __str__(self):
        return 'Dummy shipping'

    def get_delivery_total(self, items, **kwargs):
        weight = sum(
            line.product.get_weight() * line.quantity for line in items)
        #rate table stuff
        return Price(weight, currency=settings.DEFAULT_CURRENCY)

@python_2_unicode_compatible
class UspsShipping(BaseDelivery):
    name = 'USPS'

    def __str__(self):
        return 'USPS/DHL -- Economy (Free)'

    def get_delivery_total(self, items, **kwargs):
        weight = sum(
            line.product.get_weight() * line.quantity for line in items)
        #rate table stuff
        return Price((2.01 + float(weight)*0.5), currency=settings.DEFAULT_CURRENCY)

@python_2_unicode_compatible
class PriorityShipping(BaseDelivery):
    name = 'Priority'

    def __str__(self):
        return 'USPS Priority -- Expedited (+$10.00)'

    def get_delivery_total(self, items, **kwargs):
        weight = sum(
            line.product.get_weight() * line.quantity for line in items)
        #rate table stuff
        return Price(10, currency=settings.DEFAULT_CURRENCY)


def get_delivery_options_for_items(items, **kwargs):
    if 'address' in kwargs:
        for one in [UspsShipping(), PriorityShipping()]:
            yield one
    else:
        raise ValueError('Unknown delivery type')


def get_delivery(name):
    return DummyShipping()
