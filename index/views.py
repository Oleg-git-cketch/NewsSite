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


def product_page(request):
    return render(request, 'product.html')


def category_page(request):
    return render(request, 'category.html')
