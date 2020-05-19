from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('referrals.urls', namespace="referrals")),
    path('', include('products.urls', namespace="products")),
    path('accounts/', include('django.contrib.auth.urls',)),
    path('accounts/', include('accounts.urls', namespace="registration")),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
