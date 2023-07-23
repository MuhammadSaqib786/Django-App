# products/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from reviews.models import Review
# products/views.py
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
# products/views.py
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)
    review_count = reviews.count()
    return render(request, 'product_detail.html', {'product': product, 'reviews': reviews, 'review_count': review_count})


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

@login_required
def product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_edit.html', {'form': form})



def product_list(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products, 'form': form})
