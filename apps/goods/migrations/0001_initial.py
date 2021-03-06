# Generated by Django 2.2 on 2020-03-12 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updata_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('image', models.ImageField(upload_to='', verbose_name='图片')),
                ('iname', models.CharField(default='', max_length=100, verbose_name='图片名称')),
                ('spu1', models.CharField(choices=[('邮轮', '邮轮'), ('集装箱船', '集装箱船'), ('散货船及油轮', '散货船及油轮'), ('岛礁', '岛礁'), ('渔船', '渔船'), ('航母', '航母'), ('军舰', '军舰'), ('帆船', '帆船'), ('滚装船', '滚装船'), ('危化品船', '危化品船'), ('艇型船', '艇型船'), ('工程船舶', '工程船舶'), ('浮标', '浮标'), ('灯桩', '灯桩'), ('海工平台', '海工平台'), ('浮冰', '浮冰'), ('其他船舶', '其他船舶')], default='', max_length=10, verbose_name='所属种类')),
                ('ename', models.CharField(choices=[('liner', 'liner'), ('container ship', 'container ship'), ('bulk carrier', 'bulk carrier'), ('island reef', 'island reef'), ('fishing boat', 'fishing boat'), ('aircraft carrier', 'aircraft carrier'), ('warship', 'warship'), ('sailboat', 'sailboat'), ('ro-ro ship', 'ro-ro ship'), ('chemical tanker', 'chemical tanker'), ('canoe', 'canoe'), ('engineering ship', 'engineering ship'), ('buoy', 'buoy'), ('light beacon', 'light beacon'), ('offshore platform', 'offshore platform'), ('floating ice', 'floating ice'), ('other ship', 'other ship')], default='', max_length=30, verbose_name='英文名称')),
                ('xl', models.IntegerField(default='', verbose_name='左上X坐标')),
                ('yl', models.IntegerField(default='', verbose_name='左上Y坐标')),
                ('xr', models.IntegerField(default='', verbose_name='右下X坐标')),
                ('yr', models.IntegerField(default='', verbose_name='右下Y坐标')),
                ('imagefrom', models.CharField(default='', max_length=50, verbose_name='数据来源')),
                ('imageunite', models.CharField(default='', max_length=50, verbose_name='数据提供单位')),
                ('imagetime', models.CharField(default='', max_length=50, verbose_name='采集时间')),
                ('imagesite', models.CharField(default='', max_length=50, verbose_name='数据采集地点')),
                ('imageweather', models.CharField(default='', max_length=30, verbose_name='气象条件')),
                ('imageocean', models.CharField(default='', max_length=50, verbose_name='采集海域')),
                ('imagedistance', models.CharField(default='', max_length=20, verbose_name='拍摄距离（米）')),
                ('toais', models.CharField(default='', max_length=128, verbose_name='目标船舶AIS信息')),
                ('fromais', models.CharField(default='', max_length=128, verbose_name='数据采集船舶AIS信息')),
                ('user_id', models.IntegerField(verbose_name='所属上传人id')),
                ('status', models.SmallIntegerField(choices=[(0, '未审'), (1, '已审'), (2, '驳回')], default=0, verbose_name='状态')),
            ],
            options={
                'verbose_name': '图片具体属性',
                'verbose_name_plural': '图片具体属性',
                'db_table': 'df_goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsSKU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updata_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=20, verbose_name='图片名称')),
                ('image', models.ImageField(upload_to='goods', verbose_name='图片')),
                ('status', models.SmallIntegerField(choices=[(0, '未审核'), (1, '已审核')], default=0, verbose_name='状态')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='具体属性')),
            ],
            options={
                'verbose_name': '图片粗略属性',
                'verbose_name_plural': '图片粗略属性',
                'db_table': 'df_goods_sku',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updata_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('name', models.CharField(choices=[('邮轮', '邮轮'), ('集装箱船', '集装箱船'), ('散货船及油轮', '散货船及油轮'), ('岛礁', '岛礁'), ('渔船', '渔船'), ('航母', '航母'), ('军舰', '军舰'), ('帆船', '帆船'), ('滚装船', '滚装船'), ('危化品船', '危化品船'), ('艇型船', '艇型船'), ('工程船舶', '工程船舶'), ('浮标', '浮标'), ('灯桩', '灯桩'), ('海工平台', '海工平台'), ('浮冰', '浮冰'), ('其他船舶', '其他船舶')], default='', max_length=20, verbose_name='种类名称')),
                ('image', models.ImageField(upload_to='type', verbose_name='图片')),
                ('type_name', models.CharField(choices=[('邮轮', '邮轮'), ('集装箱船', '集装箱船'), ('散货船及油轮', '散货船及油轮'), ('岛礁', '岛礁'), ('渔船', '渔船'), ('航母', '航母'), ('军舰', '军舰'), ('帆船', '帆船'), ('滚装船', '滚装船'), ('危化品船', '危化品船'), ('艇型船', '艇型船'), ('工程船舶', '工程船舶'), ('浮标', '浮标'), ('灯桩', '灯桩'), ('海工平台', '海工平台'), ('浮冰', '浮冰'), ('其他船舶', '其他船舶')], default='', max_length=20, verbose_name='种类名称')),
            ],
            options={
                'verbose_name': '图片种类',
                'verbose_name_plural': '图片种类',
                'db_table': 'df_goods_type',
            },
        ),
        migrations.CreateModel(
            name='IndexGoodsBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updata_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片')),
                ('index', models.SmallIntegerField(default=0, verbose_name='展示顺序')),
            ],
            options={
                'verbose_name': '首页轮播图片',
                'verbose_name_plural': '首页轮播图片',
                'db_table': 'df_index_banner',
            },
        ),
        migrations.CreateModel(
            name='IndexPromotionBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updata_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=20, verbose_name='图片名称')),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片')),
                ('index', models.SmallIntegerField(default=0, verbose_name='展示顺序')),
            ],
            options={
                'verbose_name': '主页图片范例',
                'verbose_name_plural': '主页图片范例',
                'db_table': 'df_index_promotion',
            },
        ),
        migrations.CreateModel(
            name='IndexTypeGoodsBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updata_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('index', models.SmallIntegerField(default=0, verbose_name='展示顺序')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsSKU', verbose_name='图片')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsType', verbose_name='图片类型')),
            ],
            options={
                'verbose_name': '主页分类展示图片',
                'verbose_name_plural': '主页分类展示图片',
                'db_table': 'df_index_type_goods',
            },
        ),
        migrations.AddField(
            model_name='goodssku',
            name='type_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsType', verbose_name='种类名称'),
        ),
    ]
