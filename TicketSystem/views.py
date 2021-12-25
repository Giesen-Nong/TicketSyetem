from django.shortcuts import render
from django.template import RequestContext
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from TicketSystem import models
import numpy as np
import datetime

# Create your views here.
# def index(request):
#     if request.session.get('is_login',None):
#         return redirect('/book/')
#     name ="机票预订系统"
#     return render(request,"index.html",{"name":name})

def index(request):
    if request.session.get('is_login',None):
        name ="机票预订系统"
        return render(request,"index.html")
    else:
        return redirect('/login/')

def book(request):
    if request.session.get('is_login',None):
        name ="机票预订系统"
        n_list = models.FlightInfo.objects.all()
        user = models.UserInfo.objects.get(U_Name = request.session.get('user_name'))
        get_order = models.FlightInfo.objects.filter()
        now_time = datetime.datetime.now()
        for i in get_order:
            if now_time > i.StartTime:
                i.delete()
        return render(request,"book.html",{"n_list":n_list,"user":user})
    else:
        return redirect('/login/')

def admin_login(request):
    name ="机票预订系统"
    return render(request,"admin_login.html",{"name":name})

def login(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            try:
                user = models.UserInfo.objects.get(U_Id=username)
                if user.U_password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.U_Id
                    request.session['user_name'] = user.U_Name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
            return render(request, 'login.html', {"message": message})
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('/login/')
def register(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == "POST":
        message = "请检查填写的内容！"
        Id = request.POST['U_Id']
        Name = request.POST['U_Name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if Id and Name and password1 and password2:  # 获取数据
            if len(Id)!=18:
                message = "请输入正确的身份证号！"
                return render(request, 'login.html', locals())
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login.html', locals())
            if len(password1)<6:
                message = "密码长度需要大于6个字符"
                return render(request, 'login.html', locals())
            else:
                same_name_user = models.UserInfo.objects.filter(U_Id=Id)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login.html', locals())
 
                # 当一切都OK的情况下，创建新用户
                new_user = models.UserInfo.objects.create(U_Id=Id,U_Name = Name,U_password = password1)
                message = '注册成功！'
                return render(request, 'login.html', locals())  # 自动跳转到登录页面
    return render(request, 'login.html', locals())

def buy(request):
    while(1):
        a = np.random.randint(0,9,10)
        O_id = ''.join([str(x) for x in a])
        same_Oid = models.order.objects.filter(O_Id=O_id)
        if same_Oid:
            continue
        break
    while(1):
        Seat = np.random.randint(1,150,1)
        same_seat = models.order.objects.filter(seat=Seat)
        if same_seat:
            continue
        break
    U_id = request.POST['U_Id']
    F_id = request.POST['F_Id']
    F_status = request.POST['status']
    if F_status == '1':
        Status = True
    else:
        Status = False
    U = models.UserInfo.objects.get(U_Id = U_id)
    F = models.FlightInfo.objects.get(F_ID = F_id)
    F.num_a -= 1
    F.save()
    new_order = models.order.objects.create(O_Id = O_id,U_Id = U,F_Id = F,status = Status,seat = Seat)
    return redirect('/book/')

def buy_check(request):
    dic = {'status':None,'msg':None}
    if request.is_ajax():
        fid = request.POST.get('fid')
        o_info = models.order.objects.filter(U_Id = request.session.get('user_id'),F_Id = fid)
        if o_info:
            dic['status'] = 201
            dic['msg'] = '不能重复购买同一张机票！'
        else:
            dic['status'] = 200
        return JsonResponse(dic)
    return redirect('/book/')

def order(request):
    n_list = models.orderinfo.objects.all()
    user = models.UserInfo.objects.get(U_Name = request.session.get('user_name'))
    return render(request, 'order.html',{"n_list":n_list,"user":user})

def ticketpay(request):
    dic = {'status':None,'msg':None}  # 设置dic保存状态码及登入状态信息
    # 如果是ajax请求
    if request.is_ajax():
        name = request.POST.get('name')  # 获取用户名
        pwd = request.POST.get('pwd')
        oid = request.POST.get('oid')
        user_obj = models.UserInfo.objects.filter(U_Name=name,U_password=pwd).first()  # 拿到对象
        if user_obj:
            dic['status'] = 200  # 存在状态码设置成200
            new_order = models.order.objects.get(U_Id=user_obj.U_Id,O_Id = oid)
            new_order.status = True
            new_order.save()
        else:
            dic['status'] = 201
            dic['msg'] = '密码错误,请重新输入'
        # 方式一 : 直接使用JsonResponse
        return JsonResponse(dic)  # 将登入状态dic返回给前端ajax
        # 方式二 : 手动转json格式
        # import json
        # return HttpResponse(json.dumps(dic))
    return redirect('/order/')

def delete_api(request):
    # 如果是ajax请求
    if request.is_ajax():
        oid = request.POST.get('oid')
        new_order = models.order.objects.filter(O_Id=oid).first()
        F = models.FlightInfo.objects.get(F_ID = new_order.F_Id.F_ID)
        F.num_a += 1
        F.save()
        new_order.delete()
    return redirect('/order/')

def time_check(request):
    dic = {'status':None,'msg':None}
    if request.is_ajax():
        oid = request.POST.get('oid')
        new_order = models.order.objects.filter(O_Id=oid).first()
        F = models.FlightInfo.objects.get(F_ID = new_order.F_Id.F_ID)
        s_time = F.StartTime
        get_time = s_time+datetime.timedelta(days=-1)
        now_time = datetime.datetime.now()
        if now_time > get_time and now_time < s_time:
            dic['status'] = 200
        else:
            dic['status'] = 201
            dic['msg'] = '请在飞机起飞前一天与飞机起飞前之间取票'
        return JsonResponse(dic)
    return redirect('/order/')