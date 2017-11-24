#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
play=(
	('p','play'),
	('n','not play'),
)

class Stream(models.Model):
	name=models.CharField(max_length=100)
	head_imag=models.FileField(upload_to='./upload/',default='null')
	price=models.IntegerField(default=1)
	play=models.CharField(max_length=1, choices=play, default='n')