from django.shortcuts import render, redirect
from .models import Product, Category, Cart
from .forms import SearchForm, RegForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


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


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegForm(request.POST)

        # Если данные корректны
        if form.is_valid():
            username = form.clean_username()
            password2 = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password2)
            user.save()
            login(request, user)
            return redirect('/')
        # Если данные некорректны
        context = {'form': RegForm}
        return render(request, self.template_name, context)


def logout_view(request):
    logout(request)
    return redirect('/')


def to_cart(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        if product.product_count >= int(request.POST.get('pr_amount')):
            Cart.objects.create(user_id=request.user.id,
                                user_product=product,
                                user_product_quantity=int(request.POST.get('pr_amount'))).save()
            return redirect('/')


def del_from_cart(request, pk):
    product_to_del = Product.objects.get(id=pk)
    Cart.objects.filter(user_product=product_to_del, user_id=request.user.id).delete()

    return redirect('/cart')
