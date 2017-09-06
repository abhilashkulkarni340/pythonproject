# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>This is my first site</h1>")

def index1(request):
    return HttpResponse("This is index 1 in abhilash_1 branch")

def index2(request):
    return render(request,'personal/home.html')