from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from user.views import RegisterView,LoginView,UserInfoView,LogoutView,ChangeView,Update_oneView,Update_muchView,AgreeView,DisAgreeView,DeleteView,ImgInfoView
urlpatterns = [
    url(r'^register$', RegisterView.as_view(), name='register'),
    url(r'^login$', LoginView.as_view(),name='login'),
    url(r'^logout$',LogoutView.as_view(),name='logout'),
    url(r'^change$', ChangeView.as_view(),name="change"),
    url(r'^update_one$', Update_oneView.as_view(),name="update_one"),
    url(r'^update_much$', Update_muchView.as_view(),name="update_much"),
    url(r'^agree$', AgreeView.as_view(),name="agree"),
    url(r'^disagree$', DisAgreeView.as_view(),name="disagree"),
    url(r'^delete$', DeleteView.as_view(),name="delete"),
    url(r'^img_info$', ImgInfoView.as_view(),name="img_info"),
    url(r'^$',UserInfoView.as_view(), name='user'),

]
