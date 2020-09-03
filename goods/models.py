from django.db import models


# Create your models here.


# 商品分类表
# 模型类
class GoodsCategory(models.Model):
    # 分类名称
    cag_name = models.CharField(max_length=30)
    # 分类样式
    cag_css = models.CharField(max_length=20)
    # 分类图片
    cag_img = models.ImageField(upload_to='cag')


# 商品表
# 模型类
class GoodsInfo(models.Model):
    # 商品名字
    goods_name = models.CharField(max_length=100)
    # 商品价格 Decimal?  DecimalField(max_digits=None, decimal_places=None, **options)
    goods_price = models.IntegerField(default=0)
    # 商品描述
    goods_desc = models.CharField(max_length=2000)
    # 商品图片
    goods_image = models.ImageField(upload_to='goods')
    # 所属分类
    goods_cag = models.ForeignKey('GoodsCategory', on_delete=models.CASCADE)
