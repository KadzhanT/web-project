from gc import get_objects
from django.shortcuts import render

from goods.models import Products


def catolog(request, category_slug):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)
        

    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catolog.html",context)


def product(request, product_slug):

    product = Products.objects.get(slug = product_slug)

    context = {
        'product': product
    }

    return render(request, "goods/product.html", context = context)

