"""nbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from cart.views import add_cart, show_cart, remove_cart, place_order
from goods.views import index, detail, goods, new

from cart.views import submit_order

from cart.views import submit_success

urlpatterns = [
    path('admin/', admin.site.urls),
    # para1: url 要访问的地址正则表达式 para2：访问的视图函数名字
    # 主页url
    path('index/', index),
    # 详情页url
    path('detail/', detail),
    # 添加购物车
    path('cart/add_cart/', add_cart),
    # 商品分类详情页面
    path('goods/', goods),
    # 购物车页面
    path('cart/show_cart/', show_cart),
    # 在购物车删除商品
    path('cart/remove_cart/', remove_cart),
    # 订单页面
    path('place_order/', place_order),
    # 提交订单页面
    path('cart/submit_order/', submit_order),
    # 提交订单成功页面
    path('cart/submit_order/cart/submit_success/', submit_success),

    # TESTING front page
    path('new/', new),
]
