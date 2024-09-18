from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from market.models import Product
from users.models import ProductUserRating


class Custom404View(TemplateView):
    template_name = '404.html'



class FaqView(TemplateView):
    template_name = 'faq.html'



class FavoritesView(TemplateView):
    template_name = 'favorites.html'



class HomeView(TemplateView):
    template_name = 'index.html'


class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'

    def get_context_data(self, **kwargs):

        try:
            product: Product.object.get(id=kwargs['pk'])
        except Product.DoesNotExist:
            raise Http404

        context = {
            'product': product

        }




class SendProductFeedbackView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST
        rating_value = data['rating_value']

        product = Product.object.get(id = kwargs['pk'])
        user = request.user

       # ProductUserRating.object.create(
       #     rating=rating_value,
       #     product=product,
       #     user=user,
       # )


class ProductListView(TemplateView):
    template_name = 'product-list.html'
    # def get_context_data(self, **kwargs):
    #     product = Product.objects.all()
    #     paginator = Paginator(product, 10)
    #     page_number = self.request.GET.get('page', 1)
    #     page_obj = paginator.get_page(page_number)
    #
    #     context = {
    #         'page_obj': page_obj
    #     }
    #     return context


class ShoppingCartView(TemplateView):
    template_name = 'shopping-cart.html'