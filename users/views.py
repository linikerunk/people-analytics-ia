from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Employee
from .serializers import *


@api_view(['GET', 'POST'])
def employee_list(request):

    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        employee = Employee.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(employee, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = EmployeeSerializer(
            data, context={'request': request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data, 'count': paginator.count,
                       'numpages': paginator.num_pages,
                       'nextlink': '/api/employees/?page=' + str(nextPage),
                       'prevlink': '/api/employees/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):

    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(
            employee, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def costcenter_list(request):

    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        costcenter = CostCenter.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(costcenter, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = CostCenterSerializer(
            data, context={'request': request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data, 'count': paginator.count,
                         'numpages': paginator.num_pages,
                         'nextlink': '/api/costcenter/?page=' + str(nextPage),
                         'prevlink': '/api/costcenter/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = CostCenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def costcenter_detail(request, pk):
    try:
        costcenter = CostCenterSerializer.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CostCenterSerializer(costcenter,
                                          context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CostCenterSerializer(
            costcenter, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        costcenter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)