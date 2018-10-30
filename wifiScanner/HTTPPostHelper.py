#!/usr/bin/python3
import json
import requests
import datetime
from uuid import getnode as get_mac

class HTTPPostHelper:
    def __init__(self, Id, Name,PostAddress):
        self.Id = Id
        self.Name = Name
        # getting mac address on fly so there would be less configurations
        self.mac = "".join(c + ":" if i % 2 else c for i, c in enumerate(hex(get_mac())[2:].zfill(12)))[:-1]
        self.PostAddress = PostAddress
        self.sended = False
        self.beaconData_ = []

    def postData(self):
        #generating needed json structure
        data = {
            'id': self.Id,
            'name': self.Name,
            'mac' : self.mac,
            'ts' : str(datetime.datetime.utcnow()),
            'data' : str(self.beaconData_)
        }
        #print(json.dumps(data))
        response = requests.post(self.PostAddress, json=json.dumps(data))
        if response.status_code == 200 :
            self.sended = True
        else:
            self.sended = False

    def startPosting(self,BeaconData):
        # check if the data is posted before flushing it
        # if data is not postet it will append new data to the list
        if self.sended:
        #    print('Posted')
            self.beaconData_.clear()
            self.beaconData_.extend(BeaconData)
        else:
            self.beaconData_.extend(BeaconData)

        self.postData()
