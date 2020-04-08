# -*- coding: utf-8 -*-
from django.http import HttpResponse

def test(request):
    return HttpResponse("Test OK")
def view(request):
    return HttpResponse("Main page of my site")
