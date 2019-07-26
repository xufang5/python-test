from django.contrib import admin
from .models import Question

"""
用来将数据映射到admin后台
"""
# Register your models here.
admin.site.register(Question)
