def calculate_sum(sequence, start, end):
    Sum=0.0
    for i in range(start, end):
        Sum += sequence[i]
    return Sum

#小数なので閾値以下は0とする
def get_off_truncate(floor, getoff, eps):
    floor_ = int(floor/2)
    if (getoff[floor_]<eps):
        getoff[floor_]=0
    return 

#エレベーター内で各階で降りる人数を計算する関数
def calculate_getoff(sum_in_elevator, distribution, start, end, hight):
    getoff=[0]*(hight+1)
    Sum=calculate_sum(distribution, start, end)
    for i in range(start, end):
            getoff[i]=sum_in_elevator*distribution[i]/Sum
    return getoff

#リアルタイムで与えられた情報で各階で降りるであろう人数を初期化
def getoff_initialize(sum_in_elevator, distribution, now, direction, eps, hight):
    #nowが奇数の時も考慮
    now_=int(now/2)   
    if (direction==1):                   
        getoff = calculate_getoff(sum_in_elevator, distribution, now_+1, hight+1, hight)
    else:
        getoff = calculate_getoff(sum_in_elevator, distribution, 1, now_-1+(now%2), hight) 
    for floor in range(1, hight):
        get_off_truncate(floor, getoff, eps)
    return getoff

#エレベーター内の人数が定員以下かチェック
def is_clouded(sum_in_elevator, max_number):
    if (sum_in_elevator>max_number):
        sum_in_elevator=max_number
        return 1
    else:
        return 0

def clouded(getoff, distribution, max_number, start, end, hight):                   
    getoff = calculate_getoff(max_number, distribution, start, end, hight)
    return getoff

#各階でエレベーターに乗りたい人数を予測する
def ride_per_floor(number_on_floor, distribution, start, end, eps, hight):
    Sum = calculate_sum(distribution, start, end)
    All = calculate_sum(distribution, 1, hight+1)
    ride = Sum*number_on_floor/All
    if (ride<eps):
        ride = 0    
    return ride

def calculate_ride_up(number_of_persons, distribution,eps, hight):
    ride_up = [0]*(hight+1)
    for floor in range(1, hight+1):
        ride_up[floor] = ride_per_floor(number_of_persons[floor], distribution, floor+1, hight+1, eps, hight)
    return ride_up

def calculate_ride_down(number_of_persons, distribution, eps, hight):
    ride_down = [0]*(hight+1)
    for floor in range(1, hight+1):
        ride_down[floor] = ride_per_floor(number_of_persons[floor], distribution, 1, floor-1, eps, hight)
    return ride_down

def should_stop(floor, ride, getoff, eps):
    floor_ = int(floor/2)
    if (ride[floor_]>eps or getoff[floor_]>eps):
        return 1
    else:
        return 0
    
def should_go(start, end, ride, getoff, eps, hight):
    if ((start==hight) or (end==1)):
        return 0
    else:
        return 1

def main(sum_in_elevator_, number_of_persons, distribution, now, direction_, eps, max_number, hight, time_to_move, time_to_stop):
    sum_in_elevator = sum_in_elevator_
    waiting_up, waiting_down = [0]*(hight+1), [0]*(hight+1)
    waiting_time = 0
    up_persons, down_persons=[0]*(hight+1), [0]*(hight+1)
    stop_time=[0]*(hight+1) #各階に止まった回数。0~2の間を動く。
    #各階に止まった回数の和
    stop_time_sum=0
    direction = direction_
    getoff = getoff_initialize(sum_in_elevator, distribution, now, direction, eps, hight)
    ride_up = calculate_ride_up(number_of_persons, distribution,eps, hight)
    ride_down = calculate_ride_down(number_of_persons, distribution,eps, hight)
    floor=now
    floor_ = int(floor/2)
    #全ての階に2回止まるまで、あるいはエレベータの内と外に人がいる間繰り返す
    while (stop_time_sum != 2*hight and (should_go(floor+1, hight+1, ride_up, getoff, eps, hight)==1) or (should_go(1, floor_+floor%2, ride_up, getoff, eps, hight)==1)):
        #上に向かっている時
        while (direction==1):
            if (floor%2==0):    #floor階に到着したら
                floor_ = int(floor/2)
                stop_time[floor_]+=1           
                stop_time_sum+=1
                waiting_up[floor_] = waiting_time
                #floor階に止まるべきなら、乗り降りの処理
                if (should_stop(floor+1, ride_up, getoff, eps)):
                    waiting_time += time_to_stop
                    sum_in_elevator = sum_in_elevator +  ride_up[floor_] - getoff[floor_]
                    getoff[floor_]=0
                    #定員オーバーしていないかチェック
                    if (is_clouded(sum_in_elevator, max_number)):
                        sum_in_elevator = max_number   
                    up_persons[floor_]=sum_in_elevator
                    #エレベーター内の各階で降りる人数を更新
                    getoff = calculate_getoff(sum_in_elevator, distribution, floor_+1, hight+1, hight)
                else:
                    up_persons[floor_]=sum_in_elevator
                if (stop_time_sum==2*hight):
                    break
            #上の階で降りたい人、上の階で乗りたい人がいなければ方向転換してもう一つのループへ移行
            if (not should_go(floor_, hight+1, ride_up, getoff, eps, hight)):
                direction = -1
                break
            floor+=1
            waiting_time += int(time_to_move/2)
        if (stop_time_sum==2*hight):
            break
        #下に向かっている時
        while (direction==-1):
            if (floor%2==0):                    #floor階に到着したら
                floor_ = int(floor/2)
                stop_time[floor_]+=1           
                stop_time_sum+=1
                waiting_down[floor_] = waiting_time
                #floor階に止まるべきなら、乗り降りの処理
                if (should_stop(floor, ride_down, getoff, eps)):
                    waiting_time += time_to_stop
                    sum_in_elevator = sum_in_elevator +  ride_down[floor_] - getoff[floor_]
                    getoff[floor_]=0
                    #定員オーバーしていないかチェック
                    if (is_clouded(sum_in_elevator, max_number)):
                        sum_in_elevator = max_number   
                    down_persons[floor_]=sum_in_elevator
                    #エレベーター内の各階で降りる人数を更新
                    getoff = calculate_getoff(sum_in_elevator, distribution, 1, floor_-1, hight)
                else:
                    down_persons[floor_]=sum_in_elevator
                if (stop_time_sum==2*hight):
                    break
            #下の階で降りたい人、下の階で乗りたい人がいなければ方向転換して、もう一つのループへ移行
            if (not should_go(1, floor_, ride_down, getoff, eps, hight)):
                direction = 1
                break
            floor-=1
            waiting_time += int(time_to_move/2)
        if (stop_time_sum==2*hight):
            break
    return waiting_up, waiting_down, up_persons, down_persons

import random
import time

#max_per_floorは各階で待っている人数の最大値、intervalは計算を実行する時間間隔。グローバル変数を絶えず更新するのでフロント側でグローバル変数用意してください
def simulate(distribution, eps, max_number, hight, time_to_move, time_to_stop, interval, max_per_floor):
    while (True):
        sum_in_elevator = random.randint(0, max_number)
        number_of_persons = [0]*(hight+1)
        for i in range(1, hight+1):
            number_of_persons[i] = random.randint(0, max_per_floor)
        now = random.randint(2, hight*2)
        direction=random.randint(0, 1)*2-1
        waiting_up, waiting_down, up_persons, down_persons = main(sum_in_elevator, number_of_persons, distribution, now, direction, eps, max_number, hight, time_to_move, time_to_stop)
        time.sleep(interval)