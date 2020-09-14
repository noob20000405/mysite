from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
import os

from .models import Heading, Content

@require_http_methods(["GET"])
def show_headings(request):
    response = {}
    try:
        headings = Heading.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", headings))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_contents(request, pk):
    response = {}
    try:
        contents = Content.objects.filter(id=pk)
        response['list'] = json.loads(serializers.serialize("json", contents))
        for item in response['list']:
            item['fields']['content_text'] = read_file(item['fields']['content_text'])
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def read_file(path):
    if not os.path.isfile(path):
        raise TypeError(path + " does not exist")
    text = open(path).read()
    text = repr(text)
    return text.strip("'")