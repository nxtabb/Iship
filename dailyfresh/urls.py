from django.conf.urls import url
from django.contrib import admin
from django.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce', include('tinymce.urls')),
    url(r'^user/', include(('user.urls','user'), namespace='user')),#用户模块
    url(r'^search',include('haystack.urls')),
    url(r'^', include(('goods.urls', 'goods'), namespace='goods')),

]
