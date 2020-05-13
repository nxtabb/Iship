from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
import xlrd
import re
import os
from django.http import JsonResponse
from django.http import HttpResponse
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from user.models import User
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from utils.mixin import LoginRequiredMixin
from django.core.paginator import Paginator
from django_redis import get_redis_connection
import os
from goods.models import Goods
class RegisterView(View):
    def get(self,request):
        # 显示注册界面
        return render(request, 'register.html')

    def post(self,request):
        # 进行注册处理
        # 接受数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        # 进行数据校验
        if not all([username, password, email]):
            # 如果数据不完整
            return render(request, 'register.html', {'errmsg': '数据不完整'})
        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱不合法'})
        # 校验协议
        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})
        #检验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user:
            return render(request,'register.html',{'errmsg': '用户名已存在'})
        # 进行业务处理:注册
        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()
        # 返回应答,跳入
        return redirect(reverse('goods:index'))



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self,request):
        #登录校验
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        if not all([username, password]):           
            return render(request, 'login.html', {'errmsg': '数据不完整'})#接受数据
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request,'login.html',{'errmsg':'无此用户'})
        pwd = user.password
        if check_password(password, pwd):
            if user.is_active:
                #记录用户登录状态
                login(request, user)
                #获取登录后所要跳转到的地址
                #默认跳转到首页
                next_url = request.GET.get('next', reverse('goods:index'))
                response = redirect(next_url)
                return response
            else:
                return render(request, 'login.html', {'errmsg': '用户未激活'})
        else:
            return render(request, 'login.html', {'errmsg': '用户名密码错误'})#校验数据业务处理


class UserInfoView(LoginRequiredMixin, View):
    def get(self, request):
        #page='/user'
        #request.user.is_authenticated()
        #如果用户登录，则为User类的实例，
        #不然为Anony_mouse_User的实例，
        #调用.is_au...方法，返回true或false
        #获取用户的个人信息
        #获取默认信息
        user = request.user
        #获取user的身份
        authority = user.authority
        imageyes_count = int(Goods.objects.filter(user_id=user.id,status=1).count())
        imageno_count = int(Goods.objects.filter(user_id=user.id, status=2).count())
        imageyet_count = int(Goods.objects.filter(user_id=user.id, status=0).count())
        image_count = imageno_count+imageyes_count+imageyet_count
        image_checkyet_count = int(Goods.objects.filter(status=0).count())
        #获取用户的历史浏览记
        #from redis import StrictRedis
        #sr = StrictRedis(host='127.0.0.1', port='6379', db='9')
        context = {'page': 'user','image_count': image_count,'imageyes_count': imageyes_count,'imageno_count': imageno_count,'imageyet_count': imageyet_count,'image_checkyet_count':image_checkyet_count}
        return render(request, 'user_center_info.html', context)
class LogoutView(View):
    def get(self,request):
        #清除用户session
        logout(request)
        return redirect(reverse('goods:index'))
class ChangeView(View):
    def get(self,request):
        user = request.user
        if not user.is_authenticated:
            return render(request, 'login.html')
        context = {'user':user,'page':'change'}
        return render(request, 'user_center_info_change.html', context)
    def post(self,request):
        user=request.user
        orcode = request.POST.get('orcode')
        code = request.POST.get('code')
        code1 = request.POST.get('code1')
        email = request.POST.get('email')
        if not user.is_authenticated:
            return render(request,'login.html')
        if not check_password(orcode,user.password):
            return render(request,'user_center_info_change.html',{'errmsg':'原密码不正确'})
        if not all([code,code1,email]):
            return render(request, 'user_center_info_change.html', {'errmsg’:‘数据不完整'})#接受数据
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'user_center_info_change.html', {'errmsg': '邮箱不合法'})

        if check_password(code,user.password) and email == user.email:
            return render(request, 'user_center_info_change.html', {'errmsg': '密码和邮箱都与之前相同'})
        if code ==code1 and len(code) >=8 and len(code)<=20:
            user.set_password(code)
            user.email=email
            user.save()
        else:
            return render(request,'user_center_info_change.html',{'errmsg':'密码不符合规定或两次输入不相同'})
        return redirect(reverse('user:logout'))


class Update_oneView(View):
    def get(self,request):
        user = request.user
        if not user.is_authenticated:
            return render(request,'login.html')
        if user.authority==3:
            return redirect(reverse('user:login'))
        context = {'user': user, 'page': 'update_one'}
        return render(request, 'user_update_one.html', context)

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return render(request,'login.html')
        spu1 = request.POST.get('spu1')
        ename = request.POST.get('ename')
        xl = request.POST.get('xl')
        yl = request.POST.get('yl')
        xr = request.POST.get('xr')
        yr = request.POST.get('yr')
        imagefrom = request.POST.get('imagefrom')
        imageunite = request.POST.get('imageunite')
        imagetime = request.POST.get('imagetime')
        imagesite = request.POST.get('imagesite')
        imageweather = request.POST.get('imageweather')
        imageocean = request.POST.get('imageocean')
        imagedistance = request.POST.get('imagedistance')
        toais = request.POST.get('toais')
        fromais = request.POST.get('fromais')
        imgs = request.FILES.getlist('photo')  # 通过  FILES.get 获取 图片形式数据
        for img in imgs:
            if not img:
                return render(request, 'user_update_one.html', {'error': '参数不全'})
            fix = datetime.now().strftime('%Y%m%d%H%M%S%f') + '1'
            img_path = os.path.join(settings.UPLOADFILES_DIRS,
                                    spu1 + '/' + fix + img.name)
            img_path = img_path.replace(' ', '')
            f = open(img_path, 'wb')
            for i in img.chunks():
                f.write(i)
            f.close()
            a = len(settings.UPLOADFILES_DIRS)
            img_path = img_path[a-6:]
            try:
                Goods.objects.create(spu1=spu1, ename=ename, iname=img.name, xl=xl, yl=yl, xr=xr, yr=yr,imagefrom=imagefrom,
                                     imageunite=imageunite, imagetime=imagetime, imagesite=imagesite,imageweather=imageweather,
                                     imageocean=imageocean, imagedistance=imagedistance, toais=toais, fromais=fromais,
                                     image=img_path, status=0, user_id=user.id)
                user.total_count += 1
                user.save()
            except Exception as e:
                context = {'errmsg':'输入数据格式有误，上传失败，请重试'}
                render(request,'user_update_one.html',context)
        return redirect(reverse('user:user'))


class Update_muchView(View):
    def get(self,request):
        user=request.user
        if not user.is_authenticated:
            return redirect(reverse('user:login'))
        if user.authority==3:
            return redirect(reverse('user:login'))
        context = {'user': user, 'page': 'update_much'}
        return render(request,'user_update_much.html',context)

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return render(request,'login.html')
        excel = request.FILES.get('xls')
        fix = datetime.now().strftime('%Y%m%d%H%M%S%f') + '1'
        imgs = request.FILES.getlist('photo')  # 通过  FILES.get 获取 图片形式数据
        excel_path= os.path.join(settings.UPLOADFILES_DIRS+'/' +'xls/' + fix+ excel.name)
        f = open(excel_path, 'wb')
        for i in excel.chunks():
            f.write(i)
        f.close()
        excel = xlrd.open_workbook(excel_path)
        sheet = excel.sheet_by_index(0)
        rows = sheet.nrows
        for img in imgs:
            if not img:
                return render(request, 'user_update_one.html', {'error': '参数不全'})
            for i in range(rows):
                a=0
                if img.name == sheet.cell(i,0).value:
                    spu1 = sheet.cell(i, 1).value
                    ename = sheet.cell(i, 2).value
                    xl = sheet.cell(i, 3).value
                    yl = sheet.cell(i, 4).value
                    xr = sheet.cell(i, 5).value
                    yr = sheet.cell(i, 6).value
                    imagefrom = sheet.cell(i, 7).value
                    imageunite = sheet.cell(i, 8).value
                    imagetime = sheet.cell(i, 9).value
                    imagesite = sheet.cell(i, 10).value
                    imageweather = sheet.cell(i, 11).value
                    imageocean = sheet.cell(i, 12).value
                    imagedistance = sheet.cell(i, 13).value
                    toais = sheet.cell(i, 14).value
                    fromais = sheet.cell(i, 15).value
                    fix = datetime.now().strftime('%Y%m%d%H%M%S%f') + '1'
                    img_path = os.path.join(settings.UPLOADFILES_DIRS,
                                            spu1 + '/' + fix + img.name)
                    img_path = img_path.replace(' ', '')
                    f = open(img_path, 'wb')
                    for i in img.chunks():
                        f.write(i)
                    f.close()
                    a = len(settings.UPLOADFILES_DIRS)
                    img_path = img_path[a - 6:]
                    try:
                        Goods.objects.create(spu1=spu1, ename=ename, iname=img.name, xl=xl, yl=yl, xr=xr, yr=yr,
                                             imagefrom=imagefrom,
                                             imageunite=imageunite, imagetime=imagetime, imagesite=imagesite,
                                             imageweather=imageweather,
                                             imageocean=imageocean, imagedistance=imagedistance, toais=toais,
                                             fromais=fromais,
                                             image=img_path, status=0, user_id=user.id)
                        user.total_count += 1
                        user.save()
                    except Exception as e:
                        context = {'errmsg': '输入数据格式有误，上传失败，请重试'}
                        render(request, 'user_update_one.html', context)
                else:
                    a=a+1
                if(a==rows):
                    break
        return redirect(reverse('user:user'))


class AgreeView(View):
    def post(self,request):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res':0,'errmsg':'请登录 '})
        image_id = request.POST.get('image_id')
        try:
            Goods.objects.filter(id=image_id)
        except Goods.DoesNotExist:
            return JsonResponse({'res':1,'errmsg':'图片不存在'})
        Goods.objects.filter(id=image_id).update(status=1)
        total_check = User.objects.get(id=user.id).total_check
        total_check = int(total_check)+1
        User.objects.filter(id=user.id).update(total_check=total_check)
        return JsonResponse({'res':2,'message':'审核成功'})


class DisAgreeView(View):
    def post(self,request):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res':0,'errmsg':'请登录 '})
        image_id = request.POST.get('image_id')
        try:
            Goods.objects.filter(id=image_id)
        except Goods.DoesNotExist:
            return JsonResponse({'res':1,'errmsg':'图片不存在'})
        Goods.objects.filter(id=image_id).update(status=2)
        return JsonResponse({'res':2,'message':'驳回成功'})


class DeleteView(View):
    def post(self,request):
        image_id = request.POST.get('image_id')
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res':0,'errmsg':'未登录'})
        image = Goods.objects.get(id=image_id)
        path = image.image
        path=str(path)
        path1 = str(path[6:])
        image_path  = os.path.join(settings.UPLOADFILES_DIRS + path1)
        try:
            Goods.objects.filter(id=image_id).delete()
            os.remove(image_path)
        except Goods.DoesNotExist:
            return JsonResponse({'res':1,'errmsg':'数据有误1'})
        try:
            a = User.objects.get(id=user.id)
            total_count = a.total_count
            total_count = int(total_count) - 1
            User.objects.filter(id=user.id).update(total_count=total_count)
        except Exception as e:
            return JsonResponse({'res': 2, 'errmsg': '数据有误2'})

        return JsonResponse({'res': 3, 'message':'删除成功'})

class ImgInfoView(View):
    def get(self,request):
        user = request.user
        if not user.is_authenticated:
            redirect(reverse('user:login'))
        user3 = User.objects.get(id=5)
        user3.image_count = int(Goods.objects.filter(user_id=user3.id).count())
        user3.imageyes_count = int(Goods.objects.filter(user_id=user3.id,status=1).count())
        user3.imageno_count = int(Goods.objects.filter(user_id=user3.id, status=2).count())
        user3.imageyet_count = int(Goods.objects.filter(user_id=user3.id, status=0).count())


        user4 = User.objects.get(id=6)
        user4.image_count = int(Goods.objects.filter(user_id=user4.id).count())
        user4.imageyes_count = int(Goods.objects.filter(user_id=user4.id, status=1).count())
        user4.imageno_count = int(Goods.objects.filter(user_id=user4.id, status=2).count())
        user4.imageyet_count = int(Goods.objects.filter(user_id=user4.id, status=0).count())

        user5 = User.objects.get(id=7)
        user5.image_count = int(Goods.objects.filter(user_id=user5.id).count())
        user5.imageyes_count = int(Goods.objects.filter(user_id=user5.id, status=1).count())
        user5.imageno_count = int(Goods.objects.filter(user_id=user5.id, status=2).count())
        user5.imageyet_count = int(Goods.objects.filter(user_id=user5.id, status=0).count())

        user6 = User.objects.get(id=8)
        user6.image_count = int(Goods.objects.filter(user_id=user6.id).count())
        user6.imageyes_count = int(Goods.objects.filter(user_id=user6.id, status=1).count())
        user6.imageno_count = int(Goods.objects.filter(user_id=user6.id, status=2).count())
        user6.imageyet_count = int(Goods.objects.filter(user_id=user6.id, status=0).count())

        user7 = User.objects.get(id=9)
        user7.image_count = int(Goods.objects.filter(user_id=user7.id).count())
        user7.imageyes_count = int(Goods.objects.filter(user_id=user7.id, status=1).count())
        user7.imageno_count = int(Goods.objects.filter(user_id=user7.id, status=2).count())
        user7.imageyet_count = int(Goods.objects.filter(user_id=user7.id, status=0).count())

        user8 = User.objects.get(id=10)
        user8.image_count = int(Goods.objects.filter(user_id=user8.id).count())
        user8.imageyes_count = int(Goods.objects.filter(user_id=user8.id, status=1).count())
        user8.imageno_count = int(Goods.objects.filter(user_id=user8.id, status=2).count())
        user8.imageyet_count = int(Goods.objects.filter(user_id=user8.id, status=0).count())
        context = {'user3':user3,'user4':user4,'user5':user5,'user6':user6,'user7':user7,'user8':user8,'page':'img_info'}
        return render(request,'image_info.html',context)

