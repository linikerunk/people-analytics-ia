from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic import View


# @method_decorator(login_required, name='dispatch')
class UserProfileView(View):

    template_name = ''

    def get(self, request, *args, **kwargs):
        return HttpResponse("I'm on the UserProfile")
