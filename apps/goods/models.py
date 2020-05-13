from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField
from user.models import User

class GoodsType(BaseModel):
    TYPE_NAME = (
        ('邮轮', '邮轮'),
        ('集装箱船', '集装箱船'),
        ('散货船及油轮', '散货船及油轮'),
        ('岛礁', '岛礁'),
        ('渔船', '渔船'),
        ('航母', '航母'),
        ('军舰', '军舰'),
        ('帆船', '帆船'),
        ('滚装船', '滚装船'),
        ('危化品船', '危化品船'),
        ('艇型船', '艇型船'),
        ('工程船舶', '工程船舶'),
        ('浮标', '浮标'),
        ('灯桩', '灯桩'),
        ('海工平台', '海工平台'),
        ('浮冰', '浮冰'),
        ('其他船舶', '其他船舶')
    )
    name = models.CharField(default='', max_length=20, choices=TYPE_NAME, verbose_name='种类名称')
    image = models.ImageField(upload_to='type',verbose_name='图片')
    type_name = models.CharField(default='', max_length=20,choices=TYPE_NAME, verbose_name='种类名称')
    class Meta:
        db_table = 'df_goods_type'
        verbose_name = '图片种类'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class GoodsSKU(BaseModel):
    status_choices = (
        (0,'未审核'),
        (1,'已审核'),
    )
    type_name = models.ForeignKey('GoodsType',verbose_name='种类名称',on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods',verbose_name='具体属性',on_delete=models.CASCADE)
    name = models.CharField(max_length=20,verbose_name='图片名称')
    image = models.ImageField(upload_to='goods',verbose_name='图片')
    status = models.SmallIntegerField(default=0, choices=status_choices,verbose_name='状态')
    class Meta:
        db_table = 'df_goods_sku'
        verbose_name= '图片粗略属性'
        verbose_name_plural=verbose_name


class Goods(BaseModel):
    SPU1 = (
        ('邮轮', '邮轮'),
        ('集装箱船', '集装箱船'),
        ('散货船及油轮', '散货船及油轮'),
        ('岛礁', '岛礁'),
        ('渔船', '渔船'),
        ('航母', '航母'),
        ('军舰', '军舰'),
        ('帆船', '帆船'),
        ('滚装船', '滚装船'),
        ('危化品船', '危化品船'),
        ('艇型船', '艇型船'),
        ('工程船舶', '工程船舶'),
        ('浮标', '浮标'),
        ('灯桩', '灯桩'),
        ('海工平台', '海工平台'),
        ('浮冰', '浮冰'),
        ('其他船舶', '其他船舶')
    )

    ENAME = (
        ('liner', 'liner'),
        ('container ship', 'container ship'),
        ('bulk carrier', 'bulk carrier'),
        ('island reef', 'island reef'),
        ('fishing boat', 'fishing boat'),
        ('aircraft carrier', 'aircraft carrier'),
        ('warship', 'warship'),
        ('sailboat', 'sailboat'),
        ('ro-ro ship', 'ro-ro ship'),
        ('chemical tanker', 'chemical tanker'),
        ('canoe', 'canoe'),
        ('engineering ship', 'engineering ship'),
        ('buoy', 'buoy'),
        ('light beacon', 'light beacon'),
        ('offshore platform', 'offshore platform'),
        ('floating ice', 'floating ice'),
        ('other ship', 'other ship')
    )


    status_choices = (
        (0, '未审'),
        (1, '已审'),
        (2, '驳回'),
    )
    image = models.ImageField(verbose_name='图片')
    iname = models.CharField(default='', max_length=100, verbose_name='图片名称')
    spu1 = models.CharField(default='', max_length=10, choices=SPU1, verbose_name='所属种类')
    ename = models.CharField(default='',max_length=30,verbose_name='英文名称')
    xl=models.IntegerField(default='',verbose_name='左上X坐标')
    yl=models.IntegerField(default='',verbose_name='左上Y坐标')
    xr=models.IntegerField(default='',verbose_name='右下X坐标')
    yr=models.IntegerField(default='',verbose_name='右下Y坐标')
    imagefrom=models.CharField(default='',max_length=50,verbose_name='数据来源')
    imageunite = models.CharField(default='',max_length=50,verbose_name='数据提供单位')
    imagetime=models.CharField(default='',max_length=50,verbose_name='采集时间')
    imagesite=models.CharField(default='',max_length=50,verbose_name='数据采集地点')
    imageweather=models.CharField(default='',max_length=30,verbose_name='气象条件')
    imageocean=models.CharField(default='',max_length=50,verbose_name='采集海域')
    imagedistance = models.CharField(default='',max_length=20,verbose_name='拍摄距离（米）')
    toais=models.CharField(default='',max_length=256,verbose_name='目标船舶AIS信息')
    fromais=models.CharField(default='',max_length=256,verbose_name='数据采集船舶AIS信息')
    user_id=models.IntegerField(verbose_name='所属上传人id')
    status = models.SmallIntegerField(default=0, choices=status_choices, verbose_name='状态')
    class Meta:
        db_table = 'df_goods'
        verbose_name = '图片具体属性'
        verbose_name_plural=verbose_name

class IndexGoodsBanner(BaseModel):
    #首页轮播展示商品模型类
    image = models.ImageField(upload_to='banner', verbose_name='图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')
    class Meta:
        db_table = 'df_index_banner'
        verbose_name = '首页轮播图片'
        verbose_name_plural=verbose_name
#首页分类展示模型类

class IndexTypeGoodsBanner(BaseModel):
    type = models.ForeignKey('GoodsType',verbose_name='图片类型',on_delete=models.CASCADE)
    sku = models.ForeignKey('GoodsSKU',verbose_name='图片',on_delete=models.CASCADE)
    index = models.SmallIntegerField(default=0,verbose_name='展示顺序')
    class Meta:
        db_table = 'df_index_type_goods'
        verbose_name = '主页分类展示图片'
        verbose_name_plural = verbose_name

class IndexPromotionBanner(BaseModel):
    #首页促销活动类
    name = models.CharField(max_length=20,verbose_name='图片名称')
    image =models.ImageField(upload_to='banner',verbose_name='图片')
    index =models.SmallIntegerField(default=0,verbose_name='展示顺序')
    class Meta:
        db_table= 'df_index_promotion'
        verbose_name='主页图片范例'
        verbose_name_plural = verbose_name
