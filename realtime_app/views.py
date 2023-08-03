from django.http import JsonResponse
from django.shortcuts import render
from .models import Data

def index(request):
    data_list = Data.objects.all()
    return render(request, 'realtime_app/index.html', {'data_list': data_list})

def data_api(request):
    data = [
        {'id': 1, 'name': 'Data 1'},
        {'id': 2, 'name': 'Data 2'},
        {'id': 3, 'name': 'Data 3'},
    ]
    return JsonResponse(data, safe=False)

def data_detail_api(request, id):
    data = {'id': id, 'name': f'Data {id}'}
    return JsonResponse(data)

def realtime_page(request): 
    if request.method == 'GET':
        data = {
            'message': 'Halaman Realtime',
            'status': 'success',
            'data': []
        }
        return render(request, 'realtime_app/realtime.html', context=data)

def celery_demo(request): 
    if request.method == 'GET':
        data = {
            'message': 'Demo Celery',
            'status': 'success'
        }
        return render(request, 'realtime_app/celery_demo.html', context=data)