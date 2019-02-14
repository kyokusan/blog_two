import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from user import set_password
from user.forms import RegformModel, LoginformModel
from user.models import User
import re
from django_redis import get_redis_connection


def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    else:
        data = request.POST
        form = LoginformModel(data)
        if form.is_valid():
            user = form.cleaned_data.get("user")
            request.session["id"] = user.pk
            request.session["tel"] = user.tel
            request.session["head"] = user.head
            request.session["status"] = user.status
            request.session.set_expiry(0)#关闭浏览器就消失
            return redirect(reverse("content:主页"))
        else:
            context={"errors":form.errors}
            return render(request,"login.html",context=context)

def reg(request):
    if request.method=="GET":
        return render(request,"reg.html")
    else:
        data = request.POST#获取数据
        Reg_form = RegformModel(data)#验证表单合法性
        if Reg_form.is_valid():#如果合法
            clean_data = Reg_form.cleaned_data
            user = User()
            user.tel = clean_data.get("tel")
            user.password = set_password(clean_data.get("password"))
            user.save()
            return redirect("user:登录")
        else:
            context = {"errors":Reg_form.errors}
            return render(request,"reg.html",context=context)

def mine(request):

    if request.session.get("id") is None:
        return redirect("user:登录")
    if request.method=="GET":
        id = request.session.get("id")
        user = User.objects.get(pk=id)
        context = {"user":user}
        return render(request,"mine.html",context=context)


def send_msg(request):
    if request.method=="GET":
        pass
    else:
        tel = request.POST.get("tel")
        rs = re.search("^1[3-9]\d{9}$",tel)
        if rs is None:
            return JsonResponse({"errrors":1,"errmsg":"手机号码错误"})
        random_code = "".join([str(random.randint(0,9)) for _ in range(4)])
        print("========验证码为{}======".format(random_code))
        #获取redis连接
        r = get_redis_connection()
        # 保存验证码
        r.set(tel,random_code)
        #验证码60S后过期
        r.expire(tel,60)
        #创建次数变量
        key_time = "{}_times".format(tel)
        #获取当前次数
        now_time = r.get(key_time)
        if now_time is None or int(now_time) <= 10:
            r.incr(key_time)
            r.expire(key_time,3600)
        else:
            return JsonResponse({"errors":1,"errmsg":"发送次数过多，稍后再试"})

        return JsonResponse({"errors":0})