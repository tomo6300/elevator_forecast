from django.shortcuts import render

import yaml
with open('app/config.yml', 'r') as yml:
    config = yaml.load(yml)

import sys
sys.path.append('..')

from elevator_forecast import backend

# Create your views here.
from django.http import HttpResponse
import json

def index(req):
  return HttpResponse('Hello World')

def floor(request, pk):
  hight = config['hight']
  time_to_move = config['time_to_move']
  time_to_stop = config['time_to_stop']
  max_number = config['max_number']
  eps = config['eps']
  distribution = config['distribution']
  
  #リアルタイムのデータ
  now = 7     #3階と4階の間
  sum_in_elevator = 3  #エレベーターに現在3人
  number_of_persons = [0, 1, 2, 1, 2, 3, 1] #各階で待っている人はそれぞれ1,2,1,2,3,1人
  direction = 1   #現在、上に移動中

  waiting_up_list, waiting_down_list, up_persons_list, down_persons_list = backend.main(sum_in_elevator, number_of_persons, distribution, now, direction, eps, max_number, hight, time_to_move, time_to_stop)

  floor = pk
  try:
    waiting_up = waiting_up_list[floor-1]
    waiting_down = waiting_down_list[floor-1]
    up_persons = up_persons_list[floor-1]
    down_persons = down_persons_list[floor-1]
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
