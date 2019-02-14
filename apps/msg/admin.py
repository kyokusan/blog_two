from django.contrib import admin

# Register your models here.
from msg.models import Comment

admin.site.register(Comment)