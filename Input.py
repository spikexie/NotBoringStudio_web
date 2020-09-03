import pandas as pd  # install pandas if not exist
from goods.models import *

# Initialize the dataframe with the first file, consisting of just column names
# Install xlrd using pip
xls = pd.ExcelFile('GoodsInfo.xlsx')
Info = pd.read_excel(xls, 'GoodsInfo')
Cag = pd.read_excel(xls, 'GoodsCag')

# 商户信息
for i in range(Cag.shape[0]):
    c = GoodsCategory(id=i+1)  # 实例化对象，只更改id对应商户
    c.cag_name = Cag['cag_name'][i]  # '填写你想要的分类名称'
    c.cag_css = Cag['cag_css'][i]  # '填写分类名称， i.e. fruit'
    c.cag_image = Cag['cag_image'][i]  # '填写图片位置（绝对路径）'
    c.save()  # insert进数据库

"""商品信息数据的插入"""
for i in range(Info.shape[0]):
    goods = GoodsInfo(id=i+1)  # 实例化对象, 只更改ID对应商品
    goods.goods_name = Info['goods_name'][i]  # 商品名字
    goods.goods_price = Info['goods_price'][i]  # '商品价格
    goods.goods_image = str(Info['goods_image'][i])  # '填写图片位置（绝对路径）'
    goods.goods_desc = Info['goods_desc'][i]  # '填写商品信息'
    goods.goods_cag_id = int(Info['goods_cag'][i])  # 插入一个int 关联到哪一个分类
    goods.save()
