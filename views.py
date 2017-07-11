# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import *
from onlineapp.serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from classproject import settings
from onlineapp.models import *
from django.db.models import *
from django.template import loader
from django.shortcuts import render
from fusioncharts import FusionCharts
from django.core.mail import send_mail,get_connection
from django.template.loader import render_to_string


# Create your views here.

#Serialser Views
@csrf_exempt
def college_list(request):

    if request.method == 'GET':
        colleges = College.objects.all()
        serialiser = CollegeSerializer(colleges,many = True)
        return JsonResponse(serialiser.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serialiser = CollegeSerializer(data = data)
        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data,status = 201)
        return JsonResponse(serialiser.errors,status=400)

def college_detail(request,pk):
    try:
        college = College.objects.get(pk = pk)
    except College.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serialiser = CollegeSerializer(college)
        return JsonResponse(serialiser.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serialiser = CollegeSerializer(college,data = data)
        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data)
        return JsonResponse(serialiser.errors,status=400)
    elif request.method == 'DELETE':
        college.delete()
        return HttpResponse(status=204)

@csrf_exempt
def student_list(request):

    if request.method == 'GET':
        students = Student.objects.all()
        serialiser = StudentSerializer(students,many = True)
        return JsonResponse(serialiser.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serialiser = StudentSerializer(data = data)
        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data,status = 201)
        return JsonResponse(serialiser.errors,status=400)

def student_detail(request,pk):
    try:
        student= Student.objects.get(pk = pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serialiser = StudentSerializer(student)
        return JsonResponse(serialiser.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serialiser = StudentSerializer(student,data = data)
        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data)
        return JsonResponse(serialiser.errors,status=400)
    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)

def college_student_list(request,pk):
        try:
            college = College.objects.get(pk=pk)
            students = college.student_set.all()
        except College.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serialiser = StudentSerializer(students,many=True)
            return JsonResponse(serialiser.data,safe=False)

        # elif request.method == 'PUT':
        #     data = JSONParser().parse(request)
        #     serialiser = CollegeSerializer(college, data=data)
        #     if serialiser.is_valid():
        #         serialiser.save()
        #         return JsonResponse(serialiser.data)
        #     return JsonResponse(serialiser.errors, status=400)
        # elif request.method == 'DELETE':
        #     college.delete()
        #     return HttpResponse(status=204)

def colleges(request):
    colleges_list = College.objects.all()
    template = loader.get_template('onlineapp/colleges.html')
    context = {
        'colleges_list': colleges_list,
    }
    return HttpResponse(template.render(context, request))
