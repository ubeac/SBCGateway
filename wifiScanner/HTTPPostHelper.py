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

    def _cache_data(self, BeaconData){
        """Update cache."""
        # check if the data is posted before flushing the cache
        # if data is not postet it will append new data to the old data
        if self.sended:
            self.beaconData_.clear()
            self.beaconData_.extend(BeaconData)
        else:
            self.beaconData_.extend(BeaconData)
    }

    def _package_data(self)
        """make post package."""
        return {
            'id': self.Id,
            'name': self.Name,
            'mac' : self.mac,
            'ts' : str(datetime.datetime.utcnow()),
            'data' : str(self.beaconData_)
        }

    def _post_data(self):
        """send packaged data to server via http post."""
        data = _package_data()
        response = requests.post(self.PostAddress, json=json.dumps(data))
        if response.status_code == 200 :
            self.sended = True
        else:
            self.sended = False

    def start_posting(self,BeaconData):
        """cache and send scan data to server"""
        self._cache_data(BeaconData)
        self._post_data()
