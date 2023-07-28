
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>', views.productview, name='detail'),
    path('shop/', views.shop, name='shop'),
    path('search/', views.productsearch, name='search'),
    path('cart/', views.cartPage, name='cart'),
    path('category/<int:cat_id>', views.category, name='category'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

]