from django.contrib.auth.decorators import login_required
# views.py
from django.shortcuts import render, redirect
from .models import Category, Product


@login_required(login_url='/login/')
def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        category_id = request.POST['category']
        description = request.POST['description']
        price = request.POST['price']

        category = Product.objects.get(category_id=category_id)
        product = Product.objects.create(
            name=name,
            category=category,
            description=description,
            price=price
        )
        return redirect('/')
    else:
        return render(request, 'product/create_product.html')


@login_required(login_url='/login/')
def index_product(request):

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product/index_product.html', context)