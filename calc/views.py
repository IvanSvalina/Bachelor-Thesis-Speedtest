# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html',{'name':'Navin'})

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,"result.html",{"result":res})
# Create your views here.
