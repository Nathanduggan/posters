from django.shortcuts import render
from products.models import Product
from django.template.context_processors import media

# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})