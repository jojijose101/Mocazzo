from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.shortcuts import render

from moc_app.models import Product


# Create your views here.

def search_view(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request,'search.html',{'query':query,'products':products})