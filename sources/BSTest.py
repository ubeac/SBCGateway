import blescan
import JsonPoster
import datetime
import time
import _thread


postAddress = 'http://hook.ubeac.io/B9CRRQmc'
id='aslan'
name='Rpi1'
interval =1


returnedList =[]

scanner = blescan.bs(0)
poster = JsonPoster.jp(id,name,postAddress)

def scanProcess():
    while True:
        returnedList.extend(scanner.doscan(1))

def postProcess():
    while True:
        templist = returnedList.copy()
        returnedList.clear()
        poster.startPosting(templist)
        time.sleep(interval)


try:
   _thread.start_new_thread( scanProcess, () )
   _thread.start_new_thread( postProcess, () )
except:
   print ("Error: unable to start thread")

while 1:
   pass
