"""
URL configuration for almurut_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path


from market.views import HomeView, Custom404View, FaqView, FavoritesView, ProductDetailView, ProductListView, \
    ShoppingCartView, AddProductToFavorite
from users.views import LoginView, UsersRegisterView, UserMakeRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('404_error/', Custom404View.as_view(), name = '404_error'),
    path('faq_page/', FaqView.as_view(), name = 'faq_page'),

    path('favorites/', FavoritesView.as_view(), name = 'favorites_list'),
    path('add-product-to-favorite/<int:pk>/', AddProductToFavorite.as_view()),

    path('home/', HomeView.as_view(), name = 'home'),

    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name = 'product_detail_list'),
    path('product_list/', ProductListView.as_view(), name = 'send-feedback-url'),

    path('shopping_cart/', ShoppingCartView.as_view(), name = 'shopping_cart_list' ),

    path('register_page/', UsersRegisterView.as_view(), name='register_page'),
    path('login_page/', LoginView.as_view(), name='login_page'),

    path('user_registration_page/', UserMakeRegistrationView.as_view(), name='make_registration_user')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)