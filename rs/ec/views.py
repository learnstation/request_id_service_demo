#! /usr/bin/env python
# coding=utf-8
# author: jack-zh

import requests
import random

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import RequestRecord


def response_func(result=None, status=2000, message="", module="meari"):
    return Response({
        "status": status,
        "module": module,
        "message": message,
        "result": result
    })


@api_view(['POST'])
@renderer_classes((JSONRenderer, ))
def record_view(request):
    req_data = request.data
    print req_data
    obj_data = req_data
    obj_id = RequestRecord.create_obj(**obj_data)
    return response_func(result={"id": obj_id})


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
def test1_view(request):
    req_data = request.query_params.dict()
    a("test2", req_data)
    a("test3", req_data)
    a("test4", req_data)
    return response_func(result=req_data)


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
def test2_view(request):
    req_data = request.query_params.dict()
    a("test3", req_data)
    a("test4", req_data)
    return response_func(result=req_data)


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
def test3_view(request):
    req_data = request.query_params.dict()
    a("test4", req_data)
    return response_func(result=req_data)


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
def test4_view(request):
    req_data = request.query_params.dict()
    return response_func(result=req_data)


def a(path, data):
    url = "http://127.0.0.1:8000/api/nuri/aere/" + path + "/"
    data.update({
        'path': path,
        'random': random.randint(0, 99)
    })
    requests.get(url, params=data)
