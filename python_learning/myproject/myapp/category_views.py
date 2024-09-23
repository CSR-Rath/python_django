from pyexpat.errors import messages

from django.contrib.auth.decorators import login_required
# Create your views here.


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category


@login_required(login_url='/login/')
def create_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['details']
        Category.objects.create(name=name, description=description)
        return redirect('/category/index/')
    else:
        return render(request, 'category/create_category.html')

@login_required(login_url='/login/')
def index_category(request):

    categories = Category.objects.order_by('id')
    # Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category/index_category.html', context)

@login_required(login_url='/login/')
def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('/category/index/')

@login_required(login_url='/login/')
def edit_category(request, id):
    category = Category.objects.get(id=id)
    data = {"category": category}
    return render(request, "category/create_category.html", data)

def update_category(request, id):

    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.description = request.POST['details']
        category.save()
        return redirect('/category/index/')
    else:
        print("Can't edit category")