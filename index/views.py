from django.shortcuts import render, redirect
from .models import Product, Category, Cart
from .forms import SearchForm
from django.views import View


# Create your views here.
def home_page(request):
    # Достаем данные из БД
    products = Product.objects.all()
    categories = Category.objects.all()
    # Достаем форму
    form = SearchForm
    # Отправляем данные на фронт
    context = {'products': products,
               'categories': categories,
               'form': form}

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


def search(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_bar')

        if Product.objects.get(product_name__iregex=get_product):
            exact_product = Product.objects.get(product_name__iregex=get_product)
            return redirect(f'/product/{exact_product.id}')
        else:
            print('Не нашел')
            return redirect('/')





