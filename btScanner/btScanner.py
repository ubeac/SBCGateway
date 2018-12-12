#!/usr/bin/python3
import InqueryHelper
import HTTPPostHelper
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
postInterval = int(config['GatewayConfiguration']['PostInterval'])

# shared list used to exchange Beacon scans with post thread
returnedList =[]

ScanThreat = InqueryHelper.InqueryHelper(0)
HttpPostThreat = HTTPPostHelper.HTTPPostHelper(id, name,postAddress)

def scan_process():
    while True:
        returnedList.extend(ScanThreat.scan())

def post_process():
    while True:
        #temporary list used for exchange
        templist = returnedList.copy()
        returnedList.clear()
        try:
            HttpPostThreat.start_posting(templist)
        except:
            print("couldn't post data")
        time.sleep(postInterval)


try:
   _thread.start_new_thread(scan_process, ())
   _thread.start_new_thread(post_process, ())
except Exception as e:
   print("Error: unable to start thread")
   print(e)
   sys.exit(1)


while True:
    """keep the program running"""
   pass
