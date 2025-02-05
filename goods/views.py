from django.shortcuts import render

from goods.models import Products


def catolog(request):
    goods = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catolog.html",context)


def product(request, product_id):

    product = Products.objects.get(id = product_id)

    context = {
        'product': product
    }

    return render(request, "goods/product.html", context = context)

