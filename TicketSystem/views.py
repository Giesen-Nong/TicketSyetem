from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from TicketSystem import models

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
        return render(request,"book.html",{"n_list":n_list})
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
