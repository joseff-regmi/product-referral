from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from referrals.models import Refer
from .models import Product
from .forms import ProductForm
from django.views.generic import ListView
from django.db.models import Q


# decorator
def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    # if not request.user.is_authenticated:
    #     return redirect("/auth/login?next=/products")
    return render(request, template_name="products/products.html", context=context)


def product(request, id):
    ref_id = Product.objects.get()
    product = get_object_or_404(Product, id=ref_id)
    context = {
            'product': product
    }
    return render(request, template_name="products/product.html", context=context)


def create_product(request):
    print("request method", request.method)
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                product_instance = form.save(commit=False)
                product_instance.owner = request.user
                product_instance.save()
                return redirect('/products')
            except:
                pass
    else:
        form = ProductForm()
    return render(request, "products/create_product.html", {'form': form})


def edit_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect("/products")
    return render(request, "products/edit_product.html", {'form': form})


def delete_product(request, id):
    delete_product = Product.objects.get(id=id)
    delete_product.delete()
    return redirect("/accounts/profile")


# class Search(ListView):
#     model = products
#     template_name = 'products/search.html'
#
#     def get_queryset(self):  # new
#         query = self.request.GET.get('q')
#         object_list = Product.objects.filter(
#             Q(name__icontains=query) | Q(state__icontains=query)
#         )
#         return object_list

    # def get_queryset(self):
    #     books = Product.objects.all()
    #     query = self.request.GET.get('genre', None)
    #     if query:
    #         return products.filter(genre=query)
    #     return books


def search(request):
    query = request.request.GET.get('q')
    products = Product.objects.filter(Q(name__icontains=query) | Q(price__icontains=query))
    context = {
        'products': products
    }
    return render(request, template_name="products/search.html", context=context)

    # i am testing git hub
    # i am testing git hub1
    # i am teesting git hub2
