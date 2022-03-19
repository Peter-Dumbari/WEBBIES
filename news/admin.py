from django.contrib import admin
from news.models import *


# Register your models here.

class Blog(admin.ModelAdmin):
    list_display = ["topic", "datecreated", "article"]


admin.site.register(BlogNews, Blog)


class Comp(admin.ModelAdmin):
    list_display = ["topic", "datecreated", "article"]


admin.site.register(Complain, Comp)