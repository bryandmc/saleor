from django.db import models
from django.db.models import Manager

from saleor.product.models import Product
from saleor.userprofile.models import User
from django.utils.translation import pgettext_lazy

# Create your models here.

class Review(models.Model):
    print "Review"
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    review_date = models.DateTimeField(pgettext_lazy('Review field', 'review date'), auto_now_add=True)
    subject = models.CharField(max_length=100)
    user_name = models.CharField(pgettext_lazy('Review field', 'display name'), max_length=50)
    comment = models.TextField(max_length=1000)
    rating = models.IntegerField(choices=RATING_CHOICES)
    validated = models.BooleanField(default=False)

    objects = Manager()

    def __str__(self):
        return self.user_name
    class Meta:
        ordering = ['-review_date']
        app_label = 'reviews'
