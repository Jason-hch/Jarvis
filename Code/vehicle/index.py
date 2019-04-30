#!/usr/bin/python3
#coding: utf8

from bottle import get,post,run,request,template
from motor import MotorClass
import threading
import time

import os

# 保证其他地方调用是路径正确
os.chdir('/home/pi/vehicle/')
motor = MotorClass( )


@get("/")
def index():
    return template("index")
####客户端请求，服务器端就发一个index.html 控制界面给客户端

@post("/cmd")
def cmd():
    adss = request.body.read().decode()    ####接收到客户端发来的数据
    print( "web press:" + adss )
    vehicle_control(adss)         ##传值到主函数 实现对应功能
    return "OK"

def vehicle_control( move ):
    if move == "front":
        motor.forward()
        time.sleep (0.5)
    elif move == "rear":
        motor.reverse()
        time.sleep (0.5)
    elif move == "left":
        motor.left()
        time.sleep (0.1)
    elif move == "right":
        motor.right()
        time.sleep (0.1)
    motor.stop()

if __name__ == '__main__':
   #print(os.getcwd() )
    run(host="0.0.0.0")     ##开启服务器端
    
    
