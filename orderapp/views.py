from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from orderapp import serializers
from orderapp.models import *
from django.http import HttpResponse, HttpResponseRedirect



class IndexPage(TemplateView):
    def get(self, request, *args, **kwargs):
        all_product = Product.objects.all().filter(promote=False).order_by('-create_at')[:9]

        promote_data = []
        all_promote_product = Product.objects.filter(promote=True)
        for promote_product in all_promote_product:
            promote_data.append({
                'id': promote_product.id,
                'title': promote_product.title,
                'cover': promote_product.cover.url,
                'price': promote_product.price,
                'description': promote_product.description,
                'create_at': promote_product.create_at.date()
            })
        context = {
            'product_data': all_product,
            'promote_data': promote_data,
        }
        # print(context)
        return render(request, 'index.html', context)


class ContactPage(TemplateView):
    template_name = 'page-contact.html'


class AboutMe(TemplateView):
    template_name = 'page-about.html'


@login_required
def Category(request):
    # if request.user.is_authenticated and request.user.is_active:
    ordersapp = OrderApp.objects.all()
    count = len(ordersapp)
    context = {
        'ordersapp_list': ordersapp,
        'ordersapp_count': count,
    }
    return render(request, 'category.html', context)


# else:
#     # return HttpResponse('اول وارد شوید')
#     return HttpResponseRedirect(reverse('accounts:login') + '?next=/orderapp/category/')


def CustomerList(request):
    customers = Customer.objects.all()
    count = len(customers)
    context = {
        'customer_list': customers,
        'customer_count': count,
    }
    return render(request, 'orderapp/customer_list.html', context)


def ProductList(request):
    products = Product.objects.all()
    count = len(products)
    context = {
        'products': products,
        'products_count': count,
    }
    return render(request, 'orderapp/product_list.html', context)


def CustomerListTest(request):
    customers = Customer.objects.all()
    response_text = '<br/>'.join('{} : {}'.format(i, customer) for i, customer in enumerate(customers, start=1))
    return HttpResponse(response_text)
    # return HttpResponse(customers)
    # return HttpResponse('salam')


def product_list_test(request):
    products = Product.objects.all()
    response_text = """
    <!DOCTYPE html>

    <html lang="fa-ir" dir="rtl">
     <head>
        <title>لیست محصولات</title>
     </head>
    <body>
        <h1>لیست محصولات</h1>
        <h1>
            <ul>
              {}
            </ul>
        </h1>
    </body>
    </html>
    """.format('</br>'.join('<li>{}</li>'.format(product) for product in products))
    return HttpResponse(response_text)


def CustomerDetials(request, customerid):
    # customer=Customer.objects.get(pk=customerid)
    # customer = get_object_or_404(Customer, pk=customerid)
    # return HttpResponse(customer)

    customer = get_object_or_404(Customer, pk=customerid)
    context = {
        'customer': customer,
    }
    return render(request, 'orderapp/customer_details.html', context)


def productDetials(request, productid):
    # product = get_object_or_404(Product, pk=productid)
    # return HttpResponse(product)
    product = get_object_or_404(Product, pk=productid)
    context = {
        'product': product,
    }
    return render(request, 'product_details.html', context)


def orderDetials(request, orderid):
    ordeapp = get_object_or_404(OrderApp, pk=orderid)
    return HttpResponse(ordeapp)


class AllCustomerView(APIView):
    def get(self, request, format=None):
        try:
            all_customer = Customer.objects.all()
            data = []
            for customer in all_customer:
                data.append({
                    'username': customer.user.username,
                    'description': customer.description,
                    'avatar': customer.avatar.url,
                    'name': customer.user.first_name,
                    'family': customer.user.last_name,
                    'email': customer.user.email,

                })

            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error,we'll check It later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SingleCustomerAPIView(APIView):
    def get(self, request, format=None):
        try:
            customer_username = request.GET['customer_username']
            customer = Customer.objects.get(user__username=customer_username)
            serialized_data = serializers.Customerserializer(customer)
            data = serialized_data.data
            return Response({'data': data}, status=status.HTTP_200_OK)

        except:
            pass


class SearchCustomerAPIView(APIView):
    def get(self, request, format=None):
        try:
            customer_description = request.GET['customer_description']
            customers = Customer.objects.filter(description__contains=customer_description)
            serialized_data = serializers.Customerserializer(customers, many=True)
            data = serialized_data.data
            return Response({'data': data}, status=status.HTTP_200_OK)

        except:
            pass


@api_view(['GET'])
def get_customers(request):
    customers = Customer.objects.all()
    permission_ser = serializers.Customerserializer(customers, many=True)
    return Response(permission_ser.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    user_ser = serializers.Customerserializer(customer)
    return Response(user_ser.data, status=status.HTTP_200_OK)
