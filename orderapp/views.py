from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

# Create your views here.
from orderapp.models import *
from django.http import HttpResponse


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
        print(context)
        return render(request, 'index.html', context)


class ContactPage(TemplateView):
    template_name = 'page-contact.html'


class AboutMe(TemplateView):
    template_name = 'page-about.html'


class Category(TemplateView):
    template_name = 'category.html'


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
