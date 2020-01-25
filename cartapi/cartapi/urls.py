"""cartapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from product import views as product_views
from cart import views as cart_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = []

urlpatterns += [
    path('admin/', admin.site.urls),
    url(r'^api/product/(?P<id>[0-9]+)/$', product_views.api_product, name='api_product'),
    url(r'^add-to-cart/$', cart_views.add_to_cart, name='add-to-cart'),
    url(r'^edit-count-cart/$', cart_views.edit_count_cart, name='edit-count-cart'),
    url(r'^delete-cart/$', cart_views.delete_cart, name='delete-cart'),
    url(r'^cart/$', cart_views.cart, name='cart'),
    url(r'^thanks/$', cart_views.thanks, name='thanks'),
    url(r'^shipping/$', cart_views.shipping, name='shipping'),
    url(r'^$', product_views.home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
