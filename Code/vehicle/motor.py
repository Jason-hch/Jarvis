#!/usr/bin/python
#coding: utf8

import define as DEF
import RPi.GPIO as GPIO
import thread
import time

class MotorClass:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup( DEF.GPIO_MOTOR_LEFT_A, GPIO.OUT )
        GPIO.setup( DEF.GPIO_MOTOR_LEFT_B, GPIO.OUT )
        GPIO.setup( DEF.GPIO_MOTOR_RIGHT_A, GPIO.OUT )
        GPIO.setup( DEF.GPIO_MOTOR_RIGHT_B, GPIO.OUT )
        
    def __del__(self):
        GPIO.cleanup()
        
    # 前进
    def forward(self):
        GPIO.output( DEF.GPIO_MOTOR_LEFT_A, GPIO.HIGH )
        GPIO.output( DEF.GPIO_MOTOR_LEFT_B, GPIO.LOW )
        GPIO.output( DEF.GPIO_MOTOR_RIGHT_A, GPIO.HIGH )
        GPIO.output( DEF.GPIO_MOTOR_RIGHT_B, GPIO.LOW )

    # 后退
    def reverse(self):
        GPIO.output( DEF.GPIO_MOTOR_LEFT_A, GPIO.LOW )
        GPIO.output( DEF.GPIO_MOTOR_LEFT_B, GPIO.HIGH )
        GPIO.output( DEF.GPIO_MOTOR_RIGHT_A, GPIO.LOW )
        GPIO.output( DEF.GPIO_MOTOR_RIGHT_B, GPIO.HIGH )

    # 原地左转
    def left(self):
        GPIO.output( DEF.GPIO_MOTOR_LEFT_A, GPIO.HIGH )
        GPIO.output( DEF.GPIO_MOTOR_LEFT_B, GPIO.LOW )
        GPIO.output( DEF.GPIO_MOTOR_RIGHT_A, GPIO.LOW )
        GPIO.output( DEF.GPIO_MOTOR_RIGHT_B, GPIO.HIGH )
        
    # 原地右转
    def right(self):
        GPIO.output( DEF.GPIO_MOTOR_LEFT_A, GPIO.LOW )
        GPIO.output( DEF.GPIO_MOTOR_LEFT_B, GPIO.HIGH )
        GPIO.output( DEF.GPIO_MOTOR_RIGHT_A, GPIO.HIGH )
        GPIO.output( DEF.GPIO_MOTOR_RIGHT_B, GPIO.LOW )

     # 停止
    def stop(self):
        GPIO.output( DEF.GPIO_MOTOR_LEFT_A, GPIO.LOW )
        GPIO.output( DEF.GPIO_MOTOR_LEFT_B, GPIO.LOW )
        GPIO.output( DEF.GPIO_MOTOR_RIGHT_A, GPIO.LOW )
        GPIO.output( DEF.GPIO_MOTOR_RIGHT_B, GPIO.LOW )    


        
'''

    def waitToStop(self):
        time.sleep(1)
        MoterClass.stop()

# 左转弯
def left(tf):
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,GPIO.HIGH)
        GPIO.output(IN4,GPIO.LOW)

# 右转弯
def right(tf):
        GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,GPIO.LOW)
        GPIO.output(IN4,GPIO.LOW)

# 后左转弯
def pivot_left(tf):
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.HIGH)
        GPIO.output(IN3,GPIO.LOW)
        GPIO.output(IN4,GPIO.LOW)


# 后右转弯
def pivot_right(tf):
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,GPIO.LOW)
        GPIO.output(IN4,GPIO.HIGH)
        
#if __name__ == '__main__':

'''

        

                

        
