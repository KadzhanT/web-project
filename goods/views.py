from django.shortcuts import render

from goods.models import Products


def catolog(request):
    goods = Products.objects.all()

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

