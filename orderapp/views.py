from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from orderapp.models import Product


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