from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Product 


# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World!</h1>")


def product_detail_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http4
    return HttpResponse(f"Product id {obj.id}")

def product_api_detail_view(request):
    obj = Product.objects.get(id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not Found"},
        status_code=404)
    return JsonResponse({"id": obj.id})