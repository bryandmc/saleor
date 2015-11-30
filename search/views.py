from django.shortcuts import render
from saleor.product.models.base import Product

# Create your views here.
from datetime import date
from haystack.generic_views import FacetedSearchView
from forms import ProductSearchForm
from facet import FacetMunger

class ProductSearchView(FacetedSearchView):
    facet_fields = ['brand', 'category', 'rating', 'attributes', 'price']
    form_class = ProductSearchForm

    def get_queryset(self):
        queryset = super(ProductSearchView, self).get_queryset()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ProductSearchView, self).get_context_data(*args, **kwargs)
        pk_list = [a.pk for a in context['object_list']]
        products = Product.objects.get_available_products().select_subclasses()
        products = products.prefetch_related('categories', 'images',
                                             'variants__stock')
        products = products.in_bulk(pk_list)
        product_list = []
        for a in pk_list:
            if int(a) in products:
                product_list.append(products[int(a)])
        context['products'] = product_list
        url = self.request.get_full_path()
        facet_data = context['facets']['fields']
        facets = FacetMunger(facet_data, url).clean_facets()
        context['facets'] = facets
        return context
