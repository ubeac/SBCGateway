#!/usr/bin/python3
import WiFiHelper
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
interface = config['scannerConfiguration']['interface']
# shared list used to exchange Beacon scans with post thread
returnedList =[]

ScanThreat = WiFiHelper.WiFiHelper(returnedList, interface)
HttpPostThreat = HTTPPostHelper.HTTPPostHelper(id, name, postAddress)

def scanProcess():
    ScanThreat.scan()

def postProcess():
    while True:
        #temporary list used for exchange
        templist = returnedList.copy()
        returnedList.clear()
        try:
            HttpPostThreat.startPosting(templist)
        except:
            print('couldnt post data')
        time.sleep(postInterval)


try:
   _thread.start_new_thread(scanProcess, ())
   _thread.start_new_thread(postProcess, ())
except Exception as e:
   print("Error: unable to start thread")
   print(e)
   sys.exit(1)

while True:
    """keep the program running"""
   pass
