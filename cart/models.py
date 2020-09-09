from django.db import models


# Create your models here.
class OrderInfo(models.Model):
    # 订单信息
    status = (
        (1, '待付款'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '已完成'),
    )
    # 订单编号
    order_id = models.CharField(max_length=100)
    # 收货地址
    order_addr = models.CharField(max_length=100)
    # 收件人
    order_recv = models.CharField(max_length=50)
    # 电话
    order_tel = models.CharField(max_length=10)
    # 运费
    order_fee = models.IntegerField(default=1)
    # 订单备注
    order_comment = models.CharField(max_length=200)
    # 订单状态
    order_status = models.IntegerField(default=1, choices=status)

    def __str__(self):
        return self.order_tel


class OrderGoods(models.Model):
    # 订单商品模型
    # 所属商品
    goods_info = models.ForeignKey('goods.GoodsInfo',on_delete=models.CASCADE)
    # 数量
    goods_num = models.IntegerField()
    # 所属订单
    goods_order = models.ForeignKey('OrderInfo',on_delete=models.CASCADE)
