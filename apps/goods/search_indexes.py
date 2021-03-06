#定义索引类
from haystack import indexes
from goods.models import GoodsSKU,Goods

class GoodsIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return Goods
    # 建立索引数据
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

