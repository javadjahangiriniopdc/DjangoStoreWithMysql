from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from orderapp.models import *
from django.http import HttpResponse


class IndexPage(TemplateView):
    def get(self, request, *args, **kwargs):
        product_data = []
        all_product = Product.objects.all().order_by('-create_at')[:9]
        for product in all_product:
            product_data.append({
                'title': product.title,
                'cover': product.cover.url,
                'price': product.price,
                'description': product.description,
                'create_at': product.create_at.date()
            })
        promote_data = []
        all_promote_product = Product.objects.filter(promote=True)
        for promote_product in all_promote_product:
            promote_data.append({
                'title': promote_product.title,
                'cover': promote_product.cover.url,
                'price': promote_product.price,
                'description': promote_product.description,
                'create_at': promote_product.create_at.date()
            })
        context = {
            'product_data': product_data,
            'promote_data': promote_data,
        }
        print(context)
        return render(request, 'index.html', context)


class ContactPage(TemplateView):
    template_name = 'page-contact.html'


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
