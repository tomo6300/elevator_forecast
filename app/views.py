from django.shortcuts import render

import yaml
with open('app/config.yml', 'r') as yml:
    config = yaml.load(yml, Loader=yaml.SafeLoader)

import threading

import sys
sys.path.append('..')

from elevator_forecast import backend

hight = config['hight']
time_to_move = config['time_to_move']
time_to_stop = config['time_to_stop']
max_number = config['max_number']
eps = config['eps']
distribution = config['distribution']
interval = config['interval']
max_per_floor = config['max_per_floor']

backend.set_config(distribution, eps, max_number, hight, time_to_move, time_to_stop, interval, max_per_floor)
t = threading.Thread(name='simulate', target=backend.simulate)
t.start()

# Create your views here.
from django.http import HttpResponse
import json

def index(req):
  return HttpResponse('Hello World')

def configs():
  hight = config['hight']
  time_to_move = config['time_to_move']
  time_to_stop = config['time_to_stop']
  max_number = config['max_number']
  eps = config['eps']
  distribution = config['distribution']
  interval = config['interval']
  max_per_floor = config['max_per_floor']

  params = {
    'hight':hight,
    'time_to_move':time_to_move,
    'time_to_stop':time_to_stop,
    'max_number':max_number,
    'eps':eps,
    'distribution':distribution,
    'interval':interval,
    'max_per_floor':max_per_floor,
  }
    
  json_str = json.dumps(params, ensure_ascii=False, indent=2) 
  return HttpResponse(json_str)

def floor(request, pk):
  waiting_up_list, waiting_down_list, up_persons_list, down_persons_list = backend.waiting_up, backend.waiting_down, backend.up_persons, backend.down_persons

  floor = pk
  try:
    waiting_up = waiting_up_list[floor-1]
    waiting_down = waiting_down_list[floor-1]
    up_persons = int(up_persons_list[floor-1])
    down_persons = int(down_persons_list[floor-1])
  except IndexError:
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
