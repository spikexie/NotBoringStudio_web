from django.shortcuts import render, redirect

# Create your views here.
from goods.models import GoodsInfo


def add_cart(request):
    """添加购物车 cookie ( goods_id:count )"""
    # 获取GET方法过来的商品id
    goods_id = request.GET.get('id', '')
    if goods_id:
        # 获取上一个请求页面
        # 字典调用中括号
        prev_url = request.META['HTTP_REFERER']
        print(prev_url)
        response = redirect(prev_url)
        # 商品id存入cookie
        goods_count = request.COOKIES.get(goods_id)
        # 如果之前有相同商品，先取出数量后相加再放cart
        if goods_count:
            goods_count = int(goods_count) + 1
        else:
            goods_count = 1
        # 把当前id数量和商品保存进cookie
        response.set_cookie(goods_id, goods_count)
    return response


def show_cart(request):
    """显示购物车商品"""
    # 获取购物车商品列表
    cart_goods_list = []
    # 购物车商品总数
    cart_goods_count = 0
    # 购物车总价格
    cart_goods_money = 0
    # c从cookie遍历获取数据
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        # 商品价格小计
        cart_goods.total_money = int(goods_num) * cart_goods.goods_price
        # 存入list
        cart_goods_list.append(cart_goods)
        # 所有商品总数
        cart_goods_count += int(goods_num)
        # 所有商品总价
        cart_goods_money += int(goods_num) * cart_goods.goods_price
    return render(request, 'cart.html', {'cart_goods_list': cart_goods_list,
                                         'cart_goods_count': cart_goods_count,
                                         'cart_goods_money': cart_goods_money})


def remove_cart(request):
    # 获取上一个页面地址
    # 删除商品
    # 获取要删除的商品id
    goods_id = request.GET.get('id', '')
    if goods_id:
        prev_url = request.META['HTTP_REFERER']
        # 获取要返回的url对象， redirect是重定向，删除后要重新加载购物车页面
        response = redirect(prev_url)
        # 先去cookie获取当前商品
        goods_count = request.COOKIES.get(goods_id, '')
        # 通过是否存在于cookie，来判断是否可以删除
        if goods_count:
            response.delete_cookie(goods_id)
    return response


def place_order(request):
    """提交订单页面"""
    # 购物车所有商品
    cart_goods_list = []
    # 购物车所有商品数量
    cart_goods_count = 0
    # 购物车总价格
    cart_goods_money = 0
    # 从cookie 获取数据 商品id:商品数量
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        # 根据商品id获取商品对象
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 根据商品id获取商品数量
        cart_goods.goods_num = goods_num
        # 计算商品小计价格
        cart_goods.total_money = cart_goods.goods_price * int(goods_num)
        # 商品对象存入列表
        cart_goods_list.append(cart_goods)
        # 商品总数量
        cart_goods_count += int(goods_num)
        # 总价格
        cart_goods_money += cart_goods.total_money

    return render(request, 'place_order.html',{'cart_goods_list':cart_goods_list,
                                               'cart_goods_count':cart_goods_count,
                                               'cart_goods_money':cart_goods_money})
