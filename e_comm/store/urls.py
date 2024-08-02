# store/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Assuming you have a home view
    path('login.html/', views.login, name='login.html'),
    path('log/', views.log, name='log'),
    path("logout", views.logout, name=""),
    path('signup/',views.signup,name='signup'),
    path('sign/',views.sign,name='sign'),
    # path('shop.html', views.shop)
    path('404.html/', views.error_404, name='error_404'),
    path('cart.html/', views.cart, name='cart'),
    path('checkout.html/', views.checkout, name='checkout'),
    path('contact.html/', views.contact, name='contact'),
    path('shop-detail.html/', views.shop_detail, name='shop_detail'),
    path('shop.html/', views.shop, name='shop'),
    path('testimonial.html/', views.testimonial, name='testimonial'),
    path('addToCart/<int:id>', views.addToCart, name="add to cart")
]
