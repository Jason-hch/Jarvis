#!/usr/bin/python
#coding: utf8

import motor
import define
import time


if __name__ == '__main__':
    motor = MoterClass( )
    motor.forward()
    sleep(3)
    motor.reverse()
    sleep(3)
    motor.left()
    sleep(3)
    motor.right()
    sleep(3)
    motor.stop()
    sleep(3)
