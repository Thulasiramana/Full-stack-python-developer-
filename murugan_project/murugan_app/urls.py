from django.contrib import admin
from django.urls import path
from .views import sign_in,verify_otp,product_page,login,index,logout,resend_otp,add_to_cart,cart_view
#,update_cart

urlpatterns = [ 
    path('sign_in',sign_in, name='signin'),
    path('verify_otp', verify_otp, name='verify_otp'),
    path('resend_otp',resend_otp, name='resend_otp'),
    path('classy_products',product_page, name='product_page'),
    path('login/', login, name='login'),
    path('classy',index , name='index'),
    path('logout',logout,name='logout'),
    path('add-to-cart/<int:product_id>/',add_to_cart, name='add_to_cart'),
    path('cart',cart_view, name='cart_view'),  # URL to view the cart
    # path('update_cart/<int:product_id>/', update_cart, name='update_cart'),  # URL to update the cart
]