from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
import mimetypes
import os

def index(request):
    return render(request,'index.html',{})


