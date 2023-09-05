from django.shortcuts import render

from main.models import Product


def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Skystore',
        'title_comments': 'Skystore - это отличный вариант выбора товара на любой вкус!'
    }
    return render(request, 'main/home.html', context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'main/contacts.html')

def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(product_id=pk),
        'title': product_item.name
    }
    return render(request, 'main/product.html', context)