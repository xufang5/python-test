from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest


def index(request):
    return render(request, "index.html")


def login(request):
    """
    实现登录功能
    """
    if request.method == "GET":
        # 返回登录页面
        return render(request, 'login.html')
        # return HttpResponse("Hello, world. You're at the polls index.")
    else:
        # 处理登录请求
        my_username = request.POST.get("username")
        my_password = request.POST.get("password")
        if my_username == "" or  my_password == "":
            return render(request, "login.html", {"hint":"username or pasword miss"})
        # 验证数据库中是否有传回来的用户
        user = auth.authenticate(username=my_username, password=my_password)

        # if username == "admin" and password == "123":
        #     return HttpResponse('login success')
        # else:
        #     return render(request, "login.html", {"hint":"username or password error"})

        if user is not None:
            # 验证用户成功后保存到session中
            auth.login(request, user)
            # 添加cookie到浏览器
            response = HttpResponseRedirect("/sign/manage")
            # response.set_cookie("user", my_username, 3600)
            request.session['user'] = my_username #添加session到浏览器
            return response
            # # 重定向url到对应的页面
            # return HttpResponseRedirect("/sign/manage")
        else:
            return render(request, "login.html", {"hint":"username or password incorrect"})

def logout(request):
    """
    退出登录
    """
    # 退出登录时清除session
    auth.logout(request)
    return render(request, "login.html")


@login_required # 校验用户是否登录
def manage(request):
    """
    发布会管理页面
    """
    # 获取cookie中的用户名
    # cookie_user = request.COOKIES.get('user')
    cookie_user = request.session.get('user',)
    event_list = Event.objects.all()
    return render(request, "manage.html",{"welcome_user":cookie_user, "events":event_list})



@login_required # 校验用户是否登录
def search_event(request):
    """
    搜索发布会
    """
    # 获取cookie中的用户名
    # cookie_user = request.COOKIES.get('user')
    cookie_user = request.session.get('user',)

    if request.method == "GET":
        event_name = request.GET.get("searchEvent","")
        event_list = Event.objects.filter(name__contains=event_name)
        return render(request, "manage.html",{"welcome_user":cookie_user, "events":event_list})
    else:
        response = HttpResponseRedirect("/sign/manage")
        return response




@login_required # 校验用户是否登录
def qiandao(request,event_id):
    """
    签到
    """
    # 获取cookie中的用户名
    # cookie_user = request.COOKIES.get('user')
    event = get_object_or_404(Event, id=event_id)
    guest_list = Guest.objects.filter(event_id=event_id)#获取发布会嘉宾人数
    sign_list = Guest.objects.filter(sign="1", event_id=event_id)#获取签到人数
    guest_data = str(len(guest_list))
    sign_data = str(len(sign_list))
    #展示签到人数和嘉宾人数
    return render(request,"qiandao.html", {"event":event, "guest_data":guest_data, "sign_data":sign_data})


@login_required # 校验用户是否登录
def qiandao_action(request,event_id):
    """
    签到action
    """
    event = get_object_or_404(Event, id=event_id)
    guest_list = Guest.objects.filter(event_id=event_id)
    guest_data =str(len(guest_list))
    sign_data = 0
    for i in guest_list:
        if i.sign == 1:
            sign_data += 1
    if request.method == "GET":
        return render(request, "qiandao.html",{"event":event})
    else:

        guest_phone = request.POST.get("phone","")
        guest = Guest.objects.filter(phone=guest_phone)
        if len(guest) ==0:
            return render(request,"qiandao.html", {"event":event, "hint":"手机号不存在", "guest_data":guest_data, "sign_data":sign_data})
        guest = Guest.objects.filter(event_id=event_id,phone=guest_phone)
        if len(guest) ==0:
            return render(request,"qiandao.html", {"event":event, "hint":"手机号未参加本次发布会", "guest_data":guest_data, "sign_data":sign_data})
        guest = Guest.objects.get(event_id=event_id,phone=guest_phone)
        if guest.sign == 0:
            guest.sign = 1
            guest.save()
            return render(request,"qiandao.html", {"event":event, "hint":"签到成功", "guest_data":guest_data, "sign_data":str(int(sign_data)+1)})
        else:
            return render(request,"qiandao.html", {"event":event, "hint":"手机号已签到", "guest_data":guest_data, "sign_data":sign_data})









@login_required # 校验用户是否登录
def guest(request):
    """
    嘉宾管理页面
    """
    # 获取cookie中的用户名
    # cookie_user = request.COOKIES.get('user')
    cookie_user = request.session.get('user',)
    guest_list = Guest.objects.all()
    print(guest_list)
    return render(request, "guest_manage.html",{"welcome_user":cookie_user, "guests":guest_list})





@login_required # 校验用户是否登录
def search_guest(request):
    """
    搜索嘉宾手机号
    """
    # 获取cookie中的用户名
    # cookie_user = request.COOKIES.get('user')
    cookie_user = request.session.get('user',)

    if request.method == "GET":
        guest_phone = request.GET.get("searchGuest","")
        guest_list = Guest.objects.filter(phone__contains=guest_phone)
        return render(request, "guest_manage.html",{"welcome_user":cookie_user, "guests":guest_list})
    else:
        response = HttpResponseRedirect("/sign/guest_manage")
        return response
