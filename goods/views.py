from django.http import HttpResponse
from django.shortcuts import render
from goods.models import GoodsCategory, GoodsInfo


# Create your views here.
def index(request):
    # 查询商品分类
    categories = GoodsCategory.objects.all()
    # 每个分类提取数据
    for cag in categories:
        # 一对多关系查询所有数据
        # cag.goodsinfo_set.all()
        cag.goods_list = cag.goodsinfo_set.order_by('-id')[:4]

    # 购物车获取所有商品 cookie key:value(商品id:数量)
    # 购物车商品列表
    cart_goods_list = []
    # 购物车商品总数
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        # 过滤cookie判断是不是商品
        if not goods_id.isdigit():
            continue
        # 遍历cookie获取对象
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        # 将对象放入列表
        cart_goods_list.append(cart_goods)
        cart_goods_count = cart_goods_count + int(goods_num)

    # 购物车商品总数
    return render(request, 'index.html', {'categories': categories, 'cart_goods_list': cart_goods_list,
                                          'cart_goods_count': cart_goods_count})


def detail(request):
    """商品详情页面"""
    # 商品分类
    categories = GoodsCategory.objects.all()
    # 购物车数据
    cart_goods_list = []
    # 当前商品数据
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
            # 根据id查数据
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods_list.append(cart_goods)
        cart_goods_count = cart_goods_count + int(goods_num)
    # 显示需要显示的信息
    # 获取传来的商品id
    goods_id = request.GET.get('id', 1)
    goods_data = GoodsInfo.objects.get(id=goods_id)
    return render(request, 'detail.html',
                  {'categories': categories, 'cart_goods_list': cart_goods_list, 'cart_goods_count': cart_goods_count,
                   'goods_data': goods_data})


def goods(request):
    """商品分类页面"""

    # 获取传过来的分类id
    cag_id = request.GET.get('cag', 1)
    # 获取分类对象
    current_cag = GoodsCategory.objects.get(id=cag_id)
    # 当前分类下所有商品
    # 一样可以用
    goods_data = GoodsInfo.objects.filter(goods_cag=current_cag)
    #goods_data = current_cag.goodsinfo_set.all()
    # 所有分类
    categories = GoodsCategory.objects.all()
    # 购物车所有商品总数
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods_count = cart_goods_count + int(cart_goods.goods_num)

    return render(request, 'goods.html', {'current_cag': current_cag,
                                          'goods_data': goods_data,
                                          'cart_goods_count': cart_goods_count,
                                          'categories': categories})

