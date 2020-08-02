from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Training, Entity, Instructor, Event
from .serializers import *


@api_view('GET', 'POST')
def training_list(request):
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view('GET', 'POST')
def training_detail(request):
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view('GET', 'POST')
def entity_list(request):
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view('GET', 'POST')
def entity_detail(request):
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view('GET', 'POST')
def instructor_list(request):
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view('GET', 'POST')
def instructor_detail(request):
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view('GET', 'POST')
def event_list(request):
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view('GET', 'POST')
def event_detail(request):
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
