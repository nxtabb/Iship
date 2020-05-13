from django.conf.urls import url
from goods.views import IndexView,DetailView,ListView,DownloadFile,ListCheckView,DownloadImageView,DetailCheckView,DetailOtherView,ListMoreView,ListNoView,ListOkView,ListYetView,DetailMoreView,DetailOkView,DetailNoView,DetailYetView,ListMoreCheckView,DetailMoreCheckView
urlpatterns = [
    url(r'^index$', IndexView.as_view(), name='index'),
    url(r'^goods_check/(?P<good_id>\d+)$', DetailCheckView.as_view(), name='detail_check'),
    url(r'^goods_other/(?P<good_id>\d+)$', DetailOtherView.as_view(), name='detail_other'),
    url(r'^goods/(?P<good_id>\d+)$', DetailView.as_view(), name='detail'),
    url(r'^goodsok/(?P<good_id>\d+)$', DetailOkView.as_view(), name='detailok'),
    url(r'^goodsno/(?P<good_id>\d+)$', DetailNoView.as_view(), name='detailno'),
    url(r'^goodsyet/(?P<good_id>\d+)$', DetailYetView.as_view(), name='detailyet'),
    url(r'^goods_more/(?P<type_id>\d+)/(?P<good_id>\d+)$', DetailMoreView.as_view(), name='detail_more'),
    url(r'^goods_more_check/(?P<type_id>\d+)/(?P<good_id>\d+)$', DetailMoreCheckView.as_view(), name='detail_more_check'),
    url(r'^list_check/(?P<page>\d+)$' , ListCheckView.as_view(), name='list_check'),#审查员我的审查
    url(r'^list/(?P<page>\d+)$', ListView.as_view(), name='list'),#我的上传
    url(r'^listno/(?P<page>\d+)$', ListNoView.as_view(), name='listno'),#我的驳回
    url(r'^listok/(?P<page>\d+)$', ListOkView.as_view(), name='listok'),#我的已审
    url(r'^listyet/(?P<page>\d+)$', ListYetView.as_view(), name='listyet'),#我的未审
    url(r'^list_more/(?P<type_id>\d+)/(?P<page>\d+)$', ListMoreView.as_view(), name='list_more'),#index页面查看更多
    url(r'^list_more_check/(?P<type_id>\d+)/(?P<page>\d+)$', ListMoreCheckView.as_view(), name='list_more_check'),#index页面查看更多
    url(r'^download_img/(?P<image_id>\d+)$', DownloadImageView.as_view(), name='download_img'),
    url(r'^download$', DownloadFile.as_view(), name="download"),

]

