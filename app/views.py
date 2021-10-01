from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json

def index(req):
  return HttpResponse('Hello World')

def floor(request, pk):
  floor = pk
  waiting_up = -1
  waiting_down = -1
  up_persons = -1
  down_persons = -1
  params = {
    'floor':floor,
    'waiting_up':waiting_up,
    'waiting_down':waiting_down,
    'up_persons':up_persons,
    'down_persons':down_persons,
  }
    
  json_str = json.dumps(params, ensure_ascii=False, indent=2) 
  return HttpResponse(json_str)
