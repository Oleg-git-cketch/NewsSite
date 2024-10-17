from django.shortcuts import render
from .models import Product, Category, Cart


# Create your views here.
def home_page(request):
    # Достаем данные из БД
    products = Product.objects.all()
    categories = Category.objects.all()
    # Отправляем данные на фронт
    context = {'products': products, 'categories': categories}

    return render(request, 'home.html', context)


def product_page(request, pk):
    # Достаем данные из БД
    product = Product.objects.get(id=pk)
    # Отправляем данные на фронт
    context = {'product': product}
    return render(request, 'product.html', context)


def category_page(request, pk):
    # Определяем выбранную категорию
    category = Category.objects.get(id=pk)
    exact_products = Product.objects.filter(product_category=category)
    # Отправляем данные на фронт
    context = {'category': category, 'products': exact_products}
    return render(request, 'category.html', context)
