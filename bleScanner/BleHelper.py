#!/usr/bin/python3
import os
import sys
import struct
import bluetooth._bluetooth as bluez
import datetime

class BleHelper:
    def __init__(self,dev_id = 0):

        self.LE_META_EVENT = 0x3e
        self.LE_PUBLIC_ADDRESS = 0x00
        self.LE_RANDOM_ADDRESS = 0x01
        self.LE_SET_SCAN_PARAMETERS_CP_SIZE = 7
        self.OGF_LE_CTL = 0x08
        self.OCF_LE_SET_SCAN_PARAMETERS = 0x000B
        self.OCF_LE_SET_SCAN_ENABLE = 0x000C
        self.OCF_LE_CREATE_CONN = 0x000D

        self.LE_ROLE_MASTER = 0x00
        self.LE_ROLE_SLAVE = 0x01

        # these are actually subevents of LE_META_EVENT
        self.EVT_LE_CONN_COMPLETE = 0x01
        self.EVT_LE_ADVERTISING_REPORT = 0x02
        self.EVT_LE_CONN_UPDATE_COMPLETE = 0x03
        self.EVT_LE_READ_REMOTE_USED_FEATURES_COMPLETE = 0x04

        # Advertisment event types
        self.ADV_IND = 0x00
        self.ADV_DIRECT_IND = 0x01
        self.ADV_SCAN_IND = 0x02
        self.ADV_NONCONN_IND = 0x03
        self.ADV_SCAN_RSP = 0x04
        try:
            self.sock = bluez.hci_open_dev(dev_id)
            print("ble thread started")

        except:
            print("error accessing bluetooth device...")
            sys.exit(1)

        self.hci_le_set_scan_parameters(self.sock)
        self.hci_enable_le_scan(self.sock)


    def returnnumberpacket(self, pkt):
        myInteger = 0
        multiple = 256
        for c in pkt:
            myInteger += struct.unpack("B", c)[0] * multiple
            multiple = 1
        return myInteger


    def returnstringpacket(self,pkt):
        myString = ""
        for c in pkt:
            myString += "%02x" % struct.unpack("B", c)[0]
        return myString


    def get_packed_bdaddr(self, bdaddr_string):
        packable_addr = []
        addr = bdaddr_string.split(':')
        addr.reverse()
        for b in addr:
            packable_addr.append(int(b, 16))
        return struct.pack("<BBBBBB", *packable_addr)


    def packed_bdaddr_to_string(self, bdaddr_packed):
        return ':'.join('%02x' % i for i in struct.unpack("<BBBBBB", bdaddr_packed[::-1]))


    def hci_enable_le_scan(self, sock):
        self.hci_toggle_le_scan(sock, 0x01)


    def hci_disable_le_scan(self, sock):
        self.hci_toggle_le_scan(sock, 0x00)


    def hci_toggle_le_scan(self, sock, enable):
        # hci_le_set_scan_enable(dd, 0x01, filter_dup, 1000);
        # memset(&scan_cp, 0, sizeof(scan_cp));
        # uint8_t         enable;
        #       uint8_t         filter_dup;
        #        scan_cp.enable = enable;
        #        scan_cp.filter_dup = filter_dup;
        #
        #        memset(&rq, 0, sizeof(rq));
        #        rq.ogf = OGF_LE_CTL;
        #        rq.ocf = OCF_LE_SET_SCAN_ENABLE;
        #        rq.cparam = &scan_cp;
        #        rq.clen = LE_SET_SCAN_ENABLE_CP_SIZE;
        #        rq.rparam = &status;
        #        rq.rlen = 1;

        #        if (hci_send_req(dd, &rq, to) < 0)
        #                return -1;
        cmd_pkt = struct.pack("<BB", enable, 0x00)
        bluez.hci_send_cmd(sock, self.OGF_LE_CTL, self.OCF_LE_SET_SCAN_ENABLE, cmd_pkt)


    def hci_le_set_scan_parameters(self, sock):
        old_filter = sock.getsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, 14)

        SCAN_RANDOM = 0x01
        OWN_TYPE = SCAN_RANDOM
        SCAN_TYPE = 0x01


    def parse_events(self, sock, loop_count=100):
        old_filter = sock.getsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, 14)

        # perform a device inquiry on bluetooth device #0
        # The inquiry should last 8 * 1.28 = 10.24 seconds
        # before the inquiry is performed, bluez should flush its cache of
        # previously discovered devices
        flt = bluez.hci_filter_new()
        bluez.hci_filter_all_events(flt)
        bluez.hci_filter_set_ptype(flt, bluez.HCI_EVENT_PKT)
        sock.setsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, flt)
        done = False
        results = []
        myFullList = []
        for i in range(0, loop_count):
            pkt = sock.recv(255)

            ptype, event, plen = struct.unpack("BBB", pkt[:3])
            # print( "--------------" )
            if event == bluez.EVT_INQUIRY_RESULT_WITH_RSSI:
                i = 0
            elif event == bluez.EVT_NUM_COMP_PKTS:
                i = 0
            elif event == bluez.EVT_DISCONN_COMPLETE:
                i = 0
            elif event == self.LE_META_EVENT:
                subevent = pkt[3]
                pkt = pkt[4:]
                if subevent == self.EVT_LE_CONN_COMPLETE:
                    self.le_handle_connection_complete(pkt)
                elif subevent == self.EVT_LE_ADVERTISING_REPORT:
                    # print( "advertising report")
                    num_reports =  pkt[0]
                    report_pkt_offset = 0
                    for i in range(0, num_reports):
                        myFullList.append({"data": pkt.hex(), "ts": str(datetime.datetime.utcnow())})

                    done = True
        sock.setsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, old_filter)
        #print(myFullList)
        return myFullList


    def scan(self,numberOfScannes=1):
        return self.parse_events(self.sock, numberOfScannes)

#testing the helper class and write results to ble.txt
if __name__ == '__main__':
    bleScanner = BleHelper()
    f = open("ble.txt","w")
    f.write('Data;time stamp UTC\r\n')
    f.close()

    while True:
        res = bleScanner.scan(1)
        f = open("ble.txt", "a+")
        for dev in res:
            f.write(str(dev["data"]) + ";" + str(dev["ts"])+"\r\n")
        f.close()

