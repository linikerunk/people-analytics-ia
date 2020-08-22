from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions, status
from rest_framework.views import APIView
from .serializers import *
from django.http import JsonResponse
import requests


class DoctorCetification(APIView):

    def get(self, request, *args, **kwargs):
        data = requests.get('https://www.consultacrm.com.br/api/index.php?tipo=crm&uf=&q=&chave=3134259764&destino=json')
        return HttpResponse(data)


