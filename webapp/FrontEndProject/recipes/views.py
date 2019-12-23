import json

from django.http import HttpResponse, JsonResponse
from prometheus_client import generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST, Summary
import prometheus_client
from django.views.decorators.csrf import csrf_exempt
from prometheus_client import multiprocess

# Create your views here.
from django.shortcuts import render
import requests
import os
import time

BACKEND_HOST = os.environ['BACKEND_HOST']
BACKEND_PORT = os.environ['BACKEND_PORT']
BACKEND_API = os.environ['BACKEND_API']


# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('frontend_request_processing_seconds', 'Time spent processing request frontend')

# Decorate function with metric.

def indexView(request):
    data = {}

    try:
      r = makeRequestToBackend()
      json = r.json()
      if r.status_code == 200:
        data['mock'] = json
        data['status_code'] = "200"
      elif r.status_code == 204:
        data['mock'] = {}
        data['status_code'] = "204"
      else:
        data['status_code'] = "Error"
        data['mock'] = {}
      print('data ' + str(data))
      return render(request, 'ShowRecipeTemplate.html', data)
    except Exception as e:
      return render(request, 'ShowRecipeTemplate.html')

@REQUEST_TIME.time()
def makeRequestToBackend():
  return requests.get('http://' + BACKEND_HOST + ':' + BACKEND_PORT + BACKEND_API)

@csrf_exempt
def metrics(request):
	registry = CollectorRegistry()
	multiprocess.MultiProcessCollector(registry)
	data = generate_latest(registry)
	return HttpResponse(
		data,
		content_type=CONTENT_TYPE_LATEST)