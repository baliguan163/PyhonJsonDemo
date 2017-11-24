# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
from .models import Stream
from django.core import serializers
from django.http import  HttpResponse,JsonResponse

def get_data(request):
	data=Stream.objects.filter(play='p')

	response_data={}
	try:
		if(data):
			response_data['result'] = '1'
			response_data['desc'] = 'success'
			response_data['data'] = serializers.serialize('json',data)
		else:
			response_data['result'] = '0'
			response_data['desc'] = 'error'
			response_data['data'] = serializers.serialize('json',data)
	except:
		response_data['result'] = '0'
		response_data['desc'] = 'exception'
		response_data['data'] ='exception'
	return  HttpResponse(JsonResponse(response_data), content_type='application/json')