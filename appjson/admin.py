# -*- coding: utf-8 -*-
from .models import  *
from django.contrib import admin


class StreamAmdin(admin.ModelAdmin):
	list_display = ('name','head_imag','price','play')
	list_editable = ('head_imag','price','play')


# Register your models here.
admin.site.register(Stream,StreamAmdin)