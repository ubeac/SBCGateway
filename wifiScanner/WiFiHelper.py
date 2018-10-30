#!/usr/bin/python3
# sniff wifi packets and filter out probe requests
# for this code to work you need to set you wifi in monitor mode first

from scapy.all import *
import datetime

class WiFiHelper:
    def __init__(self, result=[], interface='wlan0'):
        self.results = result
        self.interface = interface

    #this function will be called every time a packet recived
    def PacketHandler(self,pkt):
        if pkt.type==0 and pkt.subtype==4:
            self.results.append({"mac": str(pkt.addr2), "channel": str(pkt.Channel), "signal": str(pkt.dBm_AntSignal), "ts": str(datetime.datetime.utcnow())})

    def scan(self):
        sniff(iface=self.interface, prn=self.PacketHandler, store=0)

# testing wifi helper by writing results to probes.txt
if __name__ == '__main__':
    f = open("probes.txt", "w")
    f.write('sender MAC;Channel MHz;signal;time stamp UTC\r\n')
    f.close()
    resultList = []
    tempResult = []
    wifiscanner = WiFiHelper(resultList)
    wifiscanner.scan()
    while True:
        tempResult = resultList.copy()
        resultList.clear()
        f = open("probes.txt", "a+")
        for probe in tempResult:
            f.write(probe["mac"] + ';' + probe["channel"] + ';' + probe["signal"] + ';' + probe["ts"] + '\r\n')
        f.close()
        time.sleep(1)
