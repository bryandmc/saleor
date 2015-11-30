import datetime
from haystack import indexes
from saleor.product.models.base import Product, Brand
from star_ratings.models import Rating
from django.shortcuts import get_object_or_404


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField()
    link = indexes.CharField()
    price = indexes.DecimalField(faceted=True)
    category = indexes.MultiValueField(null=True, faceted=True)
    rating = indexes.DecimalField(null=True, faceted=True)
    brand = indexes.CharField(null=True, faceted=True)
    attributes = indexes.MultiValueField(null=True, faceted=True)

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        products = Product.objects.get_available_products().select_subclasses()
        products = products.prefetch_related('attributes', 'categories', 'brand')
        return products

    def prepare_title(self, obj):
        return obj.name

    def prepare_price(self, obj):
        print obj.price.net
        return obj.price.net

    def prepare_brand(self, obj):
        brand = Brand.objects.filter(id=obj.brand_id).first()
        return brand

    def prepare_attributes(self, obj):
        return [a.name for a in obj.attributes.all()]

    def prepare_rating(self, obj):
        rating = Rating.objects.ratings_for_instance(obj)
        return rating.average

    def prepare_link(self, obj):
        return obj.get_absolute_url()

    def prepare_category(self, obj):
        return [a.name for a in obj.categories.all()]
