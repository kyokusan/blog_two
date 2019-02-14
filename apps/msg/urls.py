from django.conf.urls import url

from msg.views import comment

urlpatterns = [
    url(r'^comment/',comment, name="评论"),
]