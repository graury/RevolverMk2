#!/usr/bin/env python

from random import shuffle
import time 
from time import sleep
import RPi.GPIO as GPIO

turns=[33, 34, 33, 33, 34, 33]

PUL = 22
DIR = 27
PUSHER = 26
PUL2 = 6
DIR2 = 5
DOOR = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(PUSHER, GPIO.OUT)
GPIO.setup(PUL2, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(DOOR, GPIO.OUT)

delay = 0.001
delay2 = 0.1
delay3 = 1
delay4 = 0.005

shuffled_deck=[i for i in range(6)]
shuffle(shuffled_deck)
shuffled_deck.append(0)


for x in range (6): #repeat 6 times
    GPIO.output(DIR, GPIO.HIGH) #dealing the card
    for x in range(675):
    
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
    
    GPIO.output(PUSHER, GPIO.HIGH) #activating the card pusher
    sleep(delay2)
    GPIO.output(PUSHER, GPIO.LOW)

    GPIO.output(DIR, GPIO.LOW) #returning any loose cards
    for x in range(550):
    
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
    
    GPIO.output(DIR2, GPIO.LOW) #rotating the chamber 60 degrees
    
     x=0
      while current_position != card:
        x+=turns[current_position]
        current_position+=1
        current_position%=6
      print "Number of steps: {}".format(x)
      current_position=card
      
      for y in range(x,0,-1):
            GPIO.output(PUL2, GPIO.HIGH)
            sleep(delay4)
            GPIO.output(PUL2, GPIO.LOW)
            sleep (delay4)
        
        

for x in range (17): #30 degree turn to align for phase 2
    GPIO.output(PUL2, GPIO.HIGH)
    sleep(delay4)
    GPIO.output(PUL2, GPIO.LOW)
    sleep (delay4)        


current_position=0

for card in shuffled_deck: #rotate to random number and then release card 6 times

      print "Moving to card: {}".format(card+1)
      
      GPIO.output(DIR2, GPIO.LOW)
      
      x=0
      while current_position != card:
        x+=turns[current_position]
        current_position+=1
        current_position%=6
      print "Number of steps: {}".format(x)
      current_position=card
      
      for y in range(x,0,-1):
            GPIO.output(PUL2, GPIO.HIGH)
            sleep(delay4)
            GPIO.output(PUL2, GPIO.LOW)
            sleep (delay4)

      time.sleep(1)

    GPIO.output(DOOR, GPIO.HIGH) #opening the card release door
    sleep(delay3)
    GPIO.output(DOOR, GPIO.LOW)

    
GPIO.cleanup()