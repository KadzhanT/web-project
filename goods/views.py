from django.shortcuts import render


def catolog(request):
    return render(request, 'goods/catolog.html')

def product(request):
    return render(request, 'goods/product.html')
