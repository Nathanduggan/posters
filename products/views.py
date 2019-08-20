from django.shortcuts import render
from .models import Product
from cart.context import cart_contents

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    contexts = cart_contents(request)
    contexts.update({"products": products})
    return render(request, "products.html", contexts)