from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import View
from goods.models import GoodsType, GoodsSKU,IndexGoodsBanner, IndexPromotionBanner, IndexTypeGoodsBanner,Goods
from django.core.paginator import Paginator
from user.models import User
from django.conf import settings
import cv2
class IndexView(View):
    def get(self, request):
        # 获取商品种类信息：
        types = GoodsType.objects.all()
        # 获取首页轮播商品信息
        goods_banners = IndexGoodsBanner.objects.all().order_by('index')  # 排序
        # 获取首页促销活动信息
        promotion_banners = IndexPromotionBanner.objects.all().order_by('index')
        # 获取首页分类 商品展示信息
        for type in types:
            image_banners = IndexTypeGoodsBanner.objects.filter(type=type).order_by('index')
            type.image_banners = image_banners
        user = request.user
        goods = Goods.objects.filter(user_id=user.id , status=0)
        count = goods.count()
        context = {'types': types,
                   'goods_banners': goods_banners,
                   'promotion_banners': promotion_banners,
                   'count':count}

        return render(request, 'index.html', context)


#/goods/商品id
class DetailView(View):
    def get(self,request,good_id):
        #获取商品
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==3:
            return redirect(reverse('user:login'))
        try:
            good = Goods.objects.get(id=good_id)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        good_next_end = Goods.objects.order_by('-id').filter(user_id=user.id, id__gte=good.id)[0]
        good_before_end = Goods.objects.filter(user_id=user.id, id__lte=good.id)[0]
        if good.id == good_next_end.id:
            next_page = good.id
        else:
            good_next = Goods.objects.filter(user_id=user.id, id__gt=good.id)[0]
            next_page = good_next.id

        if good.id == good_before_end.id:
            before_page = good.id
        else:
            good_before = Goods.objects.order_by('-id').filter(user_id=user.id, id__lt=good.id)[0]
            before_page = good_before.id
        a = Goods.objects.filter(user_id=user.id, status=0)
        count = int(a.count())
        context = {'good': good,'user':user,'next_page':next_page,'before_page':before_page,'count':count}
        return render(request,'detail.html',context)

class DetailOkView(View):
    def get(self,request,good_id):
        #获取商品
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==3:
            return redirect(reverse('user:login'))
        try:
            good = Goods.objects.get(id=good_id)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        good_next_end = Goods.objects.order_by('-id').filter(status=1, user_id=user.id, id__gte=good.id)[0]
        good_before_end = Goods.objects.filter(status=1, user_id=user.id, id__lte=good.id)[0]
        if good.id == good_next_end.id:
            next_page = good.id
        else:
            good_next = Goods.objects.filter(status=1, user_id=user.id, id__gt=good.id)[0]
            next_page = good_next.id

        if good.id == good_before_end.id:
            before_page = good.id
        else:
            good_before = Goods.objects.order_by('-id').filter(status=1, user_id=user.id, id__lt=good.id)[0]
            before_page = good_before.id
        a = Goods.objects.filter(user_id=user.id, status=0)
        count = int(a.count())
        context = {'good': good,'user':user,'next_page':next_page,'before_page':before_page,'count':count}
        return render(request,'detailok.html',context)

class DetailNoView(View):
    def get(self,request,good_id):
        #获取商品
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==3:
            return redirect(reverse('user:login'))
        try:
            good = Goods.objects.get(id=good_id)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        good_next_end = Goods.objects.order_by('-id').filter(status=2, user_id=user.id, id__gte=good.id)[0]
        good_before_end = Goods.objects.filter(status=2, user_id=user.id, id__lte=good.id)[0]
        if good.id == good_next_end.id:
            next_page = good.id
        else:
            good_next = Goods.objects.filter(status=2, user_id=user.id, id__gt=good.id)[0]
            next_page = good_next.id

        if good.id == good_before_end.id:
            before_page = good.id
        else:
            good_before = Goods.objects.order_by('-id').filter(status=2, user_id=user.id, id__lt=good.id)[0]
            before_page = good_before.id
        a = Goods.objects.filter(user_id=user.id, status=0)
        count = int(a.count())
        context = {'good': good,'user':user,'next_page':next_page,'before_page':before_page,'count':count}
        return render(request,'detailno.html',context)

class DetailYetView(View):
    def get(self,request,good_id):
        #获取商品
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==3:
            return redirect(reverse('user:login'))
        try:
            good = Goods.objects.get(id=good_id)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        good_next_end = Goods.objects.order_by('-id').filter(status=0, user_id=user.id, id__gte=good.id)[0]
        good_before_end = Goods.objects.filter(status=0, user_id=user.id, id__lte=good.id)[0]
        if good.id == good_next_end.id:
            next_page = good.id
        else:
            good_next = Goods.objects.filter(status=0, user_id=user.id, id__gt=good.id)[0]
            next_page = good_next.id

        if good.id == good_before_end.id:
            before_page = good.id
        else:
            good_before = Goods.objects.order_by('-id').filter(status=0, user_id=user.id, id__lt=good.id)[0]
            before_page = good_before.id
        a = Goods.objects.filter(user_id=user.id, status=0)
        count = int(a.count())
        context = {'good': good,'user':user,'next_page':next_page,'before_page':before_page,'count':count}
        return render(request,'detailyet.html',context)


#获取单种类图片的详情
class DetailMoreView(View):
    def get(self,request,type_id ,good_id):
        #获取商品
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==3:
            return redirect(reverse('user:login'))
        try:
            Goods.objects.filter(spu1=type)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        try:
            name = str(GoodsType.objects.get(id=type_id).name)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        try:
            good = Goods.objects.get(id=good_id)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        good_next_end = Goods.objects.order_by('-id').filter(status=1, spu1=name, id__gte=good.id)[0]
        good_before_end = Goods.objects.filter(status=1, spu1=name, id__lte=good.id)[0]
        if good.id == good_next_end.id:
            next_page = good.id
        else:
            good_next = Goods.objects.filter(status=1, spu1=name, id__gt=good.id)[0]
            next_page = good_next.id

        if good.id == good_before_end.id:
            before_page = good.id
        else:
            good_before = Goods.objects.order_by('-id').filter(status=1, spu1=name, id__lt=good.id)[0]
            before_page = good_before.id
        user = request.user
        goods = Goods.objects.filter(user_id=user.id, status=0)
        count = goods.count()
        user1 = User.objects.get(id=good.user_id)
        usern = str(user1.username)
        context = {'good': good,'user':user,'next_page':next_page,'before_page':before_page,"type_id":type_id,'usern':usern,'count':count}
        return render(request,'detail_more.html',context)






#需要种类id 页码 排序方式
#list/种类id/页码/排序方式
#list/种类id/页码？sort=排序方式
#list>type_id=种类id&page=页码&sort=排序方式
class ListView(View):
    def get(self, request, page):
        #获取种信息
        user=request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==3:
            return redirect(reverse('user:login'))
        try:
            Goods.objects.filter(user_id=user.id)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        goods = Goods.objects.filter(user_id=user.id).order_by('create_time')
        #对数据进行分页 需要使用Paginator
        paginator = Paginator(goods, 5)

        #获取第page页的内容
        try:
            page = int(page)
            #如果用户自行输入的页码不是int类型
        except Exception as e:
            page = 1
        if page > paginator.num_pages:
            page = 1
        #获取第page页的page实例对象
        goods_page = paginator.page(page)
        #todo:进行页码的控制:
        #1.总页数小于5页，页面显示所有页码
        #2.页面大于等于5页。
        #如果当前页是前三页：显示1-5页
        #如果当前页是后三页显示最后五页
        #其他情况显示当前页的前两页+后两页
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1,num_pages+1)
        elif page < 3:
            pages = range(1,6)
        elif num_pages-page<2:
            pages= range(num_pages-4, num_pages+1)
        else:pages = range(page-2, page+3)
        a = Goods.objects.filter(user_id=user.id, status=0)
        count = int(a.count())
        context = {'goods':goods,'pages':pages,'goods_page':goods_page,'count':count,'num_pages':num_pages}
        return render(request,'list.html', context)


class ListNoView(View):
    #驳回
    def get(self, request, page):
        #获取种信息
        user=request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==3:
            return redirect(reverse('user:login'))
        try:
            Goods.objects.filter(user_id=user.id).filter(status=2)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        goods = Goods.objects.filter(user_id=user.id).filter(status=2).order_by('create_time')
        #对数据进行分页 需要使用Paginator
        paginator = Paginator(goods, 5)
        #获取第page页的内容
        try:
            page = int(page)
            #如果用户自行输入的页码不是int类型
        except Exception as e:
            page = 1
        if page > paginator.num_pages:
            page = 1
        #获取第page页的page实例对象
        goods_page = paginator.page(page)
        #todo:进行页码的控制:
        #1.总页数小于5页，页面显示所有页码
        #2.页面大于等于5页。
        #如果当前页是前三页：显示1-5页
        #如果当前页是后三页显示最后五页
        #其他情况显示当前页的前两页+后两页
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1,num_pages+1)
        elif page < 3:
            pages = range(1,6)
        elif num_pages-page<2:
            pages= range(num_pages-4, num_pages+1)
        else:pages = range(page-2, page+3)
        a = Goods.objects.filter(user_id=user.id, status=0)
        count = int(a.count())
        context = {'goods':goods,'pages':pages,'goods_page':goods_page,'count':count,'num_pages':num_pages}
        return render(request,'listno.html', context)


class ListOkView(View):
    #已审
    def get(self, request, page):
        #获取种信息
        user=request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==3:
            return redirect(reverse('user:login'))
        try:
            Goods.objects.filter(user_id=user.id)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        goods = Goods.objects.filter(user_id=user.id).filter(status=1).order_by('create_time')
        #对数据进行分页 需要使用Paginator
        paginator = Paginator(goods, 5)
        #获取第page页的内容
        try:
            page = int(page)
            #如果用户自行输入的页码不是int类型
        except Exception as e:
            page = 1
        if page > paginator.num_pages:
            page = 1
        #获取第page页的page实例对象
        goods_page = paginator.page(page)
        #todo:进行页码的控制:
        #1.总页数小于5页，页面显示所有页码
        #2.页面大于等于5页。
        #如果当前页是前三页：显示1-5页
        #如果当前页是后三页显示最后五页
        #其他情况显示当前页的前两页+后两页
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1,num_pages+1)
        elif page < 3:
            pages = range(1,6)
        elif num_pages-page<2:
            pages= range(num_pages-4, num_pages+1)
        else:pages = range(page-2, page+3)
        a = Goods.objects.filter(user_id=user.id, status=0)
        count = int(a.count())
        context = {'goods':goods,'pages':pages,'goods_page':goods_page,'count':count,'num_pages':num_pages}
        return render(request,'listok.html', context)


class ListYetView(View):
    #未审
    def get(self, request, page):
        #获取种信息
        user=request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==3:
            return redirect(reverse('user:login'))
        try:
            Goods.objects.filter(user_id=user.id)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        goods = Goods.objects.filter(user_id=user.id).filter(status=0).order_by('create_time')
        #对数据进行分页 需要使用Paginator
        paginator = Paginator(goods, 5)
        #获取第page页的内容
        try:
            page = int(page)
            #如果用户自行输入的页码不是int类型
        except Exception as e:
            page = 1
        if page > paginator.num_pages:
            page = 1
        #获取第page页的page实例对象
        goods_page = paginator.page(page)
        #todo:进行页码的控制:
        #1.总页数小于5页，页面显示所有页码
        #2.页面大于等于5页。
        #如果当前页是前三页：显示1-5页
        #如果当前页是后三页显示最后五页
        #其他情况显示当前页的前两页+后两页
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1,num_pages+1)
        elif page < 3:
            pages = range(1,6)
        elif num_pages-page<2:
            pages= range(num_pages-4, num_pages+1)
        else:pages = range(page-2, page+3)

        a = Goods.objects.filter(user_id=user.id, status=0)
        count = int(a.count())

        context = {'goods':goods,'pages':pages,'goods_page':goods_page,'count':count,'num_pages':num_pages}
        return render(request,'listyet.html', context)


class ListMoreView(View):
    def get(self, request,type_id,page):
        #获取种信息
        user=request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==3:
            return redirect(reverse('user:login'))
        try:
            type = str(GoodsType.objects.get(id=type_id).name)
        except GoodsType.DoesNotExist:
            return redirect(reverse('goods:index'))
        try:
            Goods.objects.filter(spu1=type)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        goods = Goods.objects.filter(spu1=type).filter(status=1).order_by('create_time')
        #对数据进行分页 需要使用Paginator
        paginator = Paginator(goods, 5)
        #获取第page页的内容
        try:
            page = int(page)
            #如果用户自行输入的页码不是int类型
        except Exception as e:
            page = 1
        if page > paginator.num_pages:
            page = 1
        #获取第page页的page实例对象
        goods_page = paginator.page(page)
        #todo:进行页码的控制:
        #1.总页数小于5页，页面显示所有页码
        #2.页面大于等于5页。
        #如果当前页是前三页：显示1-5页
        #如果当前页是后三页显示最后五页
        #其他情况显示当前页的前两页+后两页
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1,num_pages+1)
        elif page < 3:
            pages = range(1,6)
        elif num_pages-page<2:
            pages= range(num_pages-4, num_pages+1)
        else:pages = range(page-2, page+3)
        a = Goods.objects.filter(user_id=user.id, status=0)
        count = int(a.count())
        context = {'goods':goods,'pages':pages,'goods_page':goods_page,'type_id':int(type_id),'count':count,'num_pages':num_pages}
        return render(request,'list_more.html', context)


class ListMoreCheckView(View):
    def get(self, request,type_id,page):
        #获取种信息
        user=request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==2:
            return redirect(reverse('user:login'))
        try:
            type = str(GoodsType.objects.get(id=type_id).name)
        except GoodsType.DoesNotExist:
            return redirect(reverse('goods:index'))
        try:
            Goods.objects.filter(spu1=type)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        goods = Goods.objects.filter(spu1=type).filter(status=0).order_by('create_time')
        #对数据进行分页 需要使用Paginator
        paginator = Paginator(goods, 5)
        #获取第page页的内容
        try:
            page = int(page)
            #如果用户自行输入的页码不是int类型
        except Exception as e:
            page = 1
        if page > paginator.num_pages:
            page = 1
        #获取第page页的page实例对象
        goods_page = paginator.page(page)
        #todo:进行页码的控制:
        #1.总页数小于5页，页面显示所有页码
        #2.页面大于等于5页。
        #如果当前页是前三页：显示1-5页
        #如果当前页是后三页显示最后五页
        #其他情况显示当前页的前两页+后两页
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1,num_pages+1)
        elif page < 3:
            pages = range(1,6)
        elif num_pages-page<2:
            pages= range(num_pages-4, num_pages+1)
        else:pages = range(page-2, page+3)
        a = Goods.objects.filter(user_id=user.id, status=0)
        count = int(a.count())
        context = {'goods':goods,'pages':pages,'goods_page':goods_page,'type_id':int(type_id),'count':count,'num_pages':num_pages}
        return render(request,'list_more_check.html', context)




class DownloadFile(View):
    def get(self,request):
        file = open('static/tools.zip', 'rb')
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="tools.zip"'
        return response


class ListCheckView(View):
    def get(self,request,page):
        # 获取信息
        user = request.user
        if not user.is_authenticated:
            redirect(reverse('user:login'))
        if user.authority==2:
            return redirect(reverse('user:login'))
        try:
            Goods.objects.filter(status=0)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        goods = Goods.objects.filter(status=0).order_by('create_time')
        # 对数据进行分页 需要使用Paginator
        paginator = Paginator(goods, 5)
        # 获取第page页的内容
        try:
            page = int(page)
            # 如果用户自行输入的页码不是int类型
        except Exception as e:
            page = 1
        if page > paginator.num_pages:
            page = 1
        # 获取第page页的page实例对象
        goods_page = paginator.page(page)
        # todo:进行页码的控制:
        # 1.总页数小于5页，页面显示所有页码
        # 2.页面大于等于5页。
        # 如果当前页是前三页：显示1-5页
        # 如果当前页是后三页显示最后五页
        # 其他情况显示当前页的前两页+后两页
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1, num_pages + 1)
        elif page < 3:
            pages = range(1, 6)
        elif num_pages - page < 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)


        context = {'goods': goods, 'pages': pages, 'goods_page': goods_page}
        return render(request, 'list_check.html', context)


class DownloadImageView(View):
    def get(self,request,image_id):
        user = request.user
        if not user.is_authenticated:
            return render(request,'login.html')
        image = Goods.objects.get(id=image_id)
        image_path = image.image
        image_path = str(image_path)
        image_path = 'static/'+ image_path
        image_path = str(image_path)
        name = str(image.iname)
        file = open(image_path, 'rb')
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename='+name
        return response

class DetailOtherView(View):
    def get(self,request,good_id):
        #获取商品
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        try:
            good = Goods.objects.get(id=good_id)
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))
        good_next_end = Goods.objects.order_by('-id').filter(id__gte=good.id)[0]
        good_before_end = Goods.objects.filter(id__lte=good.id)[0]
        if good.id == good_next_end.id:
            next_page = good.id
        else:
            good_next = Goods.objects.filter(id__gt=good.id)[0]
            next_page = good_next.id

        if good.id == good_before_end.id:
            before_page = good.id
        else:
            good_before = Goods.objects.order_by('-id').filter( id__lt=good.id)[0]
            before_page = good_before.id
        username = User.objects.get(id=good.user_id).username
        a = Goods.objects.filter(user_id=user.id, status=0)
        count = int(a.count())
        context = {'good': good, 'user': user, 'next_page': next_page, 'before_page': before_page,'username':username,'count':count}
        return render(request, 'detail_other_user.html', context)

class DetailCheckView(View):
    def get(self,request,good_id):
        #获取图片
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==2:
            return redirect(reverse('user:login'))
        try:
            good = Goods.objects.get(id=good_id)
            path = settings.BASE_DIR + '/static/' + str(good.image)
            # img1 = cv2.imread(path)
            # # rec = cv2.rectangle(img1, (int(good.xl), int(good.yl)), (int(good.xr), int(good.yr)), (255, 0, 0), 2)
            # # path1 = path.replace('upload', 'upload1')
            # # cv2.imwrite(path1, rec)
            a=len(settings.BASE_DIR)
            good.image1 = path[a+8:]
            xl = good.xl
            yl = good.yl
            xr = good.xr
            yr = good.yr
        except Goods.DoesNotExist:
            return redirect(reverse('goods:index'))

        good_next_end = Goods.objects.order_by('-id').filter(status=0, id__gte=good.id)[0]
        good_before_end = Goods.objects.filter(status=0, id__lte=good.id)[0]
        if good.id == good_next_end.id:
            next_page = good.id
        else:
            good_next = Goods.objects.filter(status=0, id__gt=good.id)[0]
            next_page = good_next.id


        if good.id == good_before_end.id:
            before_page = good.id
        else:
            good_before = Goods.objects.order_by('-id').filter(status=0, id__lt=good.id)[0]
            before_page = good_before.id

        username = User.objects.get(id=good.user_id).username
        context = {'good': good, 'user': user, 'next_page': next_page, 'before_page': before_page,'username':username,'xl':xl,'yl':yl,'xr':xr,'yr':yr}
        return render(request, 'detail_check.html', context)


class DetailMoreCheckView(View):
    def get(self,request,type_id ,good_id):
        #获取商品
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==2:
            return redirect(reverse('user:login'))
        name = str(GoodsType.objects.get(id=type_id).name)
        good = Goods.objects.get(id=good_id)
        path = settings.BASE_DIR + '/static/' + str(good.image)
        # img1 = cv2.imread(path)
        # rec = cv2.rectangle(img1, (int(good.xl), int(good.yl)), (int(good.xr), int(good.yr)), (255, 0, 0), 2)
        # path1 = path.replace('upload', 'upload1')
        # cv2.imwrite(path1, rec)
        a=len(settings.BASE_DIR)
        good.image1 = path[a+8:]
        xl = good.xl
        yl = good.yl
        xr = good.xr
        yr = good.yr
        good_next_end = Goods.objects.order_by('-id').filter(status=0,spu1=good.spu1,id__gte=good.id)[0]
        good_before_end = Goods.objects.filter(status=0,spu1=good.spu1, id__lte=good.id)[0]
        if good.id == good_next_end.id:
            next_page = good.id
        else:
            good_next = Goods.objects.filter(status=0,spu1=good.spu1, id__gt=good.id)[0]
            next_page = good_next.id

        if good.id == good_before_end.id:
            before_page = good.id
        else:
            good_before = Goods.objects.order_by('-id').filter(status=0,spu1=good.spu1, id__lt=good.id)[0]
            before_page = good_before.id
        username = User.objects.get(id=good.user_id).username
        context = {'good': good,'user':user,'next_page':next_page,'before_page':before_page,"type_id":type_id,'username':username,'xl':xl,'yl':yl,'xr':xr,'yr':yr}
        return render(request,'detail_more_check.html',context)
