#!/usr/bin/python3
#perform ble advertisment scan
import os
import sys
import struct
import bluetooth._bluetooth as bluez
import datetime

class BleHelper:
    def __init__(self,dev_id = 0):
        # bt parameter codes
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
        #try to start scanner
        self._run_ble_scanner()
        self._hci_le_set_scan_parameters(self.sock)
        self._hci_enable_le_scan(self.sock)

    def _run_ble_scanner(self):
        try:
            self.sock = bluez.hci_open_dev(dev_id)
            print("ble thread started")

        except Exception as e:
            print("error accessing bluetooth device...")
            print(e)
            sys.exit(1)


    def _hci_enable_le_scan(self, sock):
        """enable bt device ble scan"""
        self._hci_toggle_le_scan(sock, 0x01)


    def _hci_disable_le_scan(self, sock):
        """disable bt device ble scan"""
        self._hci_toggle_le_scan(sock, 0x00)


    def _hci_toggle_le_scan(self, sock, enable):
        """set ble scanner state"""
        cmd_pkt = struct.pack("<BB", enable, 0x00)
        bluez.hci_send_cmd(sock, self.OGF_LE_CTL, self.OCF_LE_SET_SCAN_ENABLE, cmd_pkt)


    def _hci_le_set_scan_parameters(self, sock):
        """set ble scanner parameters"""
        old_filter = sock.getsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, 14)
        SCAN_RANDOM = 0x01
        OWN_TYPE = SCAN_RANDOM
        SCAN_TYPE = 0x01


    def _parse_events(self, sock, loop_count=100):
        """parse ble device output, filter and return ble advertisments"""
        old_filter = sock.getsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, 14)
        # perform a device inquiry on bluetooth device #0
        # The inquiry should last 8 * 1.28 = 10.24 seconds
        # before the inquiry is performed, bluez should flush its cache of
        # previously discovered devices
        flt = bluez.hci_filter_new()
        bluez.hci_filter_all_events(flt)
        bluez.hci_filter_set_ptype(flt, bluez.HCI_EVENT_PKT)
        sock.setsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, flt)
        results = []
        for i in range(0, loop_count):
            pkt = sock.recv(255)
            ptype, event, plen = struct.unpack("BBB", pkt[:3])
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
                    num_reports =  pkt[0]
                    report_pkt_offset = 0
                    for i in range(0, num_reports):
                        results.append({"data": pkt.hex(), "ts": str(datetime.datetime.utcnow())})
        sock.setsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, old_filter)
        return results


    def scan(self,numberOfScannes=1):
        """scan ble advertisment and return selected number of them"""
        return self._parse_events(self.sock, numberOfScannes)

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

