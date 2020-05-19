from django.utils.deprecation import MiddlewareMixin
from products.models import Product


class ReferMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # import pdb; pdb.set_trace()
        ref_id = request.GET.get("join_ref_id")
        try:
            obj = Product.objects.get(ref_id=ref_id)
        except:
            obj = None
        if obj:
            request.session['join_id_ref'] = obj.id
