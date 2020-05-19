from django.urls import path
from .views import refer_product
from .views import refer, accept_invitation_page

app_name = "referrals"

urlpatterns = [
    path('refer-product/<int:product_id>', refer_product, name='refer-product'),
    path('referred', refer, name='referred-product'),
    path('share/<int:product_id>', accept_invitation_page, name='accept-invitation-page'),
]
