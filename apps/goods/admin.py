from django.contrib import admin
from goods.models import GoodsType,IndexPromotionBanner,IndexGoodsBanner,IndexTypeGoodsBanner,Goods,GoodsSKU
from django.core.cache import cache
class BaseModelAdmin(admin.ModelAdmin):
    #更新表中数据时调用
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        cache.delete('index_page_data')
    def delete_model(self, request, obj):
        super().delete_model(request,obj)
class GoodsTypeAdmin(BaseModelAdmin):
    pass
class GoodsAdmin(BaseModelAdmin):
    pass
class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    pass
class IndexGoodsBannerAdmin(BaseModelAdmin):
    pass
class IndexPromotionBannerAdmin(BaseModelAdmin):
    pass
class GoodsImageAdmin(BaseModelAdmin):
    pass
class GoodsSKUAdmin(BaseModelAdmin):
    pass
admin.site.register(GoodsType,GoodsTypeAdmin)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)
admin.site.register(IndexTypeGoodsBanner,IndexTypeGoodsBannerAdmin)
admin.site.register(IndexGoodsBanner,IndexGoodsBannerAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsSKU, GoodsSKUAdmin)
# Register your models here.
