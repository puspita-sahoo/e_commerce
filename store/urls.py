from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

 

urlpatterns = [
    path("", views.home, name = 'home'),
    path("product_detail/<int:id>", views.product_detail, name = 'product_detail'),
    path("cart/", views.cart, name = 'cart'),
    path("add_to_cart/", views.add_to_cart, name = 'add_to_cart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path("checkout/", views.checkout, name = 'checkout'),
    path("add_address/", views.add_address, name = 'add_address'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                          