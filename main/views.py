from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse

from .models import product
from .forms import Productform

def get_json(request):
    products= product.objects.all().values()
    return HttpResponse(products, content_type='application/json')
    #return JsonResponse(list(products),safe=False)



def list_products(request):
    products= product.objects.all()
    return render(request,'product.html',{'products': products})
    #return JsonResponse({'products': products})

def create_product(request):
    form =Productform(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'product-form.html',{'form': form})

def update_product(request,id):
    Product =product.objects.get(id=id)
    form= Productform(request.POST or None, instance=Product)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request,'product-form.html',{'form': form,'product':Product })


def delete_product(request, id):
    Product= product.objects.get(id=id)

    if (request.method =='POST'):
        Product.delete()
        return redirect('list_products')

    return render(request, 'prod-delete.html', {'product':Product})


# Create your views here.
