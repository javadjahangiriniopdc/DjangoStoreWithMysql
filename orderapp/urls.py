from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "orderapp"
urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('customer/listtest', views.CustomerListTest, name='CustomerListTest'),
    path('product/listtest', views.product_list_test, name='product_list_test'),
    path('customer/list/', views.CustomerList, name='CustomerList'),
    path('product/list/', views.ProductList, name='ProductList'),

    # path('customer/list', views.CustomerList.as_view(), name='CustomerList'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('contact/static/', document_root=settings.STATIC_ROOT)
