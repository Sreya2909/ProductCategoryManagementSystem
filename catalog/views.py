# Create your views here.
from django.shortcuts import render
from .models import Product

def product_list(request):
    # efficient query
    products = Product.objects.select_related('category').all()
    return render(request, 'catalog/product_list.html', {'products': products})
