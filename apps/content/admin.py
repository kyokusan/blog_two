from django.contrib import admin

# Register your models here.
from content.models import Category, ContentModle, Docket

admin.site.register(Category)
admin.site.register(ContentModle)
admin.site.register(Docket)
