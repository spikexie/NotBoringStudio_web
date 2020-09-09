from django.contrib import admin

# Register your models here.
from goods.models import GoodsInfo

from cart.models import OrderInfo

from goods.models import GoodsCategory


class GoodsInfoAdmin(admin.ModelAdmin):
    # 显示的字段
    list_display = ['goods_name', 'goods_price', 'goods_desc',
                    'goods_cag']
    # 每一页多少
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = True
    # 搜索框
    search_fields = ['id', 'goods_name']


class GoodsCategoryAdmin(admin.ModelAdmin):
    # 搜索框
    search_fields = ['cag_name', 'cag_css']
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['cag_name', 'cag_css']


class OrderInfoAdmin(admin.ModelAdmin):
    search_fields = ['order_recv','order_tel', 'order_comment']
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['order_tel','order_addr', 'order_recv', 'order_comment', 'order_status']


admin.site.register(GoodsInfo, GoodsInfoAdmin)
admin.site.register(OrderInfo,OrderInfoAdmin)
admin.site.register(GoodsCategory, GoodsCategoryAdmin)
