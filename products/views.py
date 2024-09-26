from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Arahkan ke halaman list produk
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

@login_required
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
