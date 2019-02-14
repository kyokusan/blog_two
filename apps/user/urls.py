from django.conf.urls import url

from user.views import login, reg, mine, send_msg

urlpatterns = [
    url(r'^login/',login,name="登录"),
    url(r'^reg/', reg, name="注册"),
    url(r'^mine/', mine, name="个人页面"),
    url(r'^send_msg/', send_msg, name="发送短信"),
]