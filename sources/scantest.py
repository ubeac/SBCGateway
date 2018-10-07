# test BLE Scanning software
# jcs 6/8/2014

import blescan
returnedList =[]

scanner = blescan.bs(0)

while True:
	returnedList.extend(scanner.doscan(1))
	print("----------")
	for beacon in returnedList:
		print(beacon)
	returnedList.clear()

