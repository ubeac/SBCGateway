![Logo of the project](http://ui.ubeac.io/static/img/logo.svg)

# SBCGateway

This is a gateway for the ubeac project.
This project contains these different scanner programs you can use together or separately.

* **[BLE scanner](https://github.com/ubeac/SBCGateway/tree/master/bleScanner)** which listens for **[ble advertisements](https://en.wikipedia.org/wiki/Bluetooth_advertising)** and send them to **[ubeac](http://ui.ubeac.io)** servers.
* **[BT scanner](https://github.com/ubeac/SBCGateway/tree/master/btScanner)** which scans for **[bluetooth inquiry](https://essay.utwente.nl/59681/1/MA_scriptie_A_Franssens.pdf)** and send them to **[ubeac](http://ui.ubeac.io)** servers.
* **[WIFI scanner](https://github.com/ubeac/SBCGateway/tree/master/wifiScanner)** which listens for **[wifi probe requests](https://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/Borderless_Networks/Unified_Access/CMX/CMX_802Fund.pdf)** and send them to **[ubeac](http://ui.ubeac.io)** servers.

## Getting started

For running this project you will need a fresh installation of [raspbian lite](https://www.raspberrypi.org/downloads/raspbian/) on a Bluetooth and WIFI enabled [RaspberryPi](https://www.raspberrypi.org/products/).

* You need to have [python 3](https://www.python.org/) and [requests](http://docs.python-requests.org/en/master/).
* For BT and BLE scanner you will need [pybluez](https://github.com/pybluez/pybluez).
* For WIFI scanner you will need [scappy](https://scapy.net/).

You can get projects from our [Git Repository](https://github.com/ubeac/SBCGateway)

For instructions on how to configure and run each project refer to the readme file in their own folder.