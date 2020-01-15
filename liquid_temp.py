#!/usr/bin/env python
import os
from datetime import datetime

def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20

def read(ds18b20):
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000 
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit

def loop(ds18b20):
    print("What liquid are we testing?")
    the_liquid = raw_input() 
    print("########################################################################################################################")
    print("#                                                                                                                      #")
    print("#       ___       ___  ________  ___  ___  ___  ________          _________   _______   _____ ______   ________        #")
    print("#      |\  \     |\  \|\   __  \|\  \|\  \|\  \|\   ___ \        |\___   ___\ \  ___ \ |\   _ \  _   \|\   __  \       #")
    print("#      \ \  \    \ \  \ \  \|\  \ \  \ \  \ \  \ \  \_|\ \       \|___ \  \_|  \   __/ \ \  \ \__\ \  \ \  \|\  \      #")
    print("#       \ \  \    \ \  \ \  \ \  \ \  \ \  \ \  \ \  \  \ \           \ \  \  \ \  \   _\ \  \|__|\ \  \ \   ____\     #")
    print("#        \ \  \____\ \  \ \  \ \  \ \  \ \  \ \  \ \  \__\ \           \ \  \  \ \  \_|\ \ \  \    \ \  \ \  \___|     #")
    print("#         \ \_______\ \__\ \_____  \ \_______\ \__\ \_______\           \ \__\  \ \_______\ \__\    \ \__\ \__\        #")
    print("#          \|_______|\|__|\|___| \__\|_______|\|__|\|_______|            \|__|   \|_______|\|__|     \|__|\|__|        #")
    print("#                                                                                                                      #")
    print("#                                                                                              By Cyrus Harrison       #")
    print("#                                                                                                                      #")
    print("########################################################################################################################")
    print(" ")
    print("Collecting data for the current temperature of " + the_liquid)
    now = datetime.now()
    # get date time in format dd/mm/YY H:M:S
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    print("App started at " + dt_string)
    while True:
        if read(ds18b20) != None:
            now = datetime.now()
            # get time for each change in temp
            dt_string = now.strftime("%H:%M:%S")
            print(dt_string)
            print "Current temperature of " + the_liquid + " is : %0.3f F" % read(ds18b20)[1]

def kill():
    quit()

if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum)
    except KeyboardInterrupt:
        kill()