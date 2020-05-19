from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Refer
from products.models import Product
import uuid

'''
when user clicks on refer button, first check if he/she is logged in or not. If not logged in,
return user to log in page so that they are authenticated and will get to refer the product.
If its the case of authenticated user
1) get the product which they are trying to refer.
2) Generate ref id and it should be unique so that it can be sharable
3) get requested user i.e get the user who wants to invite/refer that particular product to other users
4) save those data to Refer model.
'''


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_ref_id():
    ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
    return ref_id


'''
check if user is referring same product again and again
'''


@login_required
def refer_product(request, product_id):
    # get the product which they are trying to refer.
    product = get_object_or_404(Product, id=product_id)
    # get requested user. because we need to know which user is trying to refer(invite)
    user = request.user
    print("product", product)
    print("#########################")
    refer_instance, created = Refer.objects.get_or_create(product=product, inviter=user)
    print("refer_instance", refer_instance, created)
    print("##########################")
    if created:
        refer_instance.ref_id = get_ref_id()
    refer_instance.ip_address = get_ip(request)
    refer_instance.save()
    return HttpResponseRedirect("/products")


def refer(request):
    products = Refer.objects.filter(inviter=request.user)
    context = {
        'products': products,
        'user': request.user.email
    }

    return render(request, template_name="referrals/referrals.html", context=context)


@login_required
def accept_invitation_page(request, product_id):
    refer_instance = Refer.objects.get(ref_id=request.GET.get('ref', None))
    context = {
        'inviter': refer_instance.inviter,
        'product': refer_instance.product.name,
    }
    template = "referrals/accept_invitations_page.html"
    return render(request, template, context)
