#!/usr/bin/python3
import blescan
import JsonPoster
import datetime
import time
import _thread
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

#needed configurations read from config file
postAddress = config['serverConfigurations']['postAddress']
id = config['GatewayConfiguration']['id']
name = config['GatewayConfiguration']['name']
interval =config['GatewayConfiguration']['PostInterval']
numScans = config['scannerConfiguration']['scanBuffer']
# shared list used to exchange Beacon scans with post thread
returnedList =[]

scanner = blescan.bs(0)
poster = JsonPoster.jp(id, name,postAddress)

def scanProcess():
    while True:
        returnedList.extend(scanner.doscan(numScans))

def postProcess():
    while True:
        #temporary list used for exchange
        templist = returnedList.copy()
        returnedList.clear()
        poster.startPosting(templist)
        time.sleep(interval)


try:
   _thread.start_new_thread( scanProcess, () )
   _thread.start_new_thread( postProcess, () )
except:
   print ("Error: unable to start thread")

while True:
   pass
