from django.template.response import TemplateResponse
from saleor.product.models import Product, Category
from django.shortcuts import get_object_or_404


def home(request):
    products = Product.objects.get_available_products()[:12]
    products = products.prefetch_related('categories', 'images',
                                         'variants__stock')

    all_categories = Category.tree.root_nodes()
    for a in all_categories:
        print "child.."
        print a.get_children()
    print all_categories
    #category = get_object_or_404(Category, id=products[0].categories[0])
    #children_categories = category.get_children()
    return TemplateResponse(
        request, 'base.html',
        {'products': products, 'parent': None, 'categories': all_categories})
