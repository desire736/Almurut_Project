from datetime import datetime
from lib2to3.fixes.fix_input import context

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

        categoty_other_product_list = (
            Product.object.filter(category=product.category).exlude(id=product.id)
        )

        context = {
            'product': product,
            'other_product_len': categoty_other_product_list,
            'new': datetime.datetime.now().date()
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

    def get_context_data(self, **kwargs):
        context = {
            'public_list': Product.object.all(),
            'new': datetime.datetime.now().date()
        }
        return context


class ShoppingCartView(TemplateView):
    template_name = 'shopping-cart.html'




class AddProductToFavorite(TemplateView):
    template_name = 'favorites.html'

    def get_context_data(self, **kwargs):
        context = {}
        return context