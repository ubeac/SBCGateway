![Logo of the project](http://ui.ubeac.io/static/img/logo.svg)

# WIFI Scanner
This is a gateway for the ubeac project.
It will Scan for [WiFi probe requests](https://mrncciew.com/2014/10/27/cwap-802-11-probe-requestresponse/) and send them to **[ubeac](http://ui.ubeac.io)** servers.

## Getting started
For running this project you will need a fresh installation of [raspbian lite](https://www.raspberrypi.org/downloads/raspbian/) on [RaspberryPi](https://www.raspberrypi.org/products/) with a wifi adapter in [monitor mode](https://medium.com/@aallan/adding-a-second-wireless-adaptor-to-a-raspberry-pi-for-network-monitoring-c37d7db7a9bd).

You need to have :
* [python 3](https://www.python.org/)
* [requests](http://docs.python-requests.org/en/master/).
* [scappy](https://scapy.net/)

You can get the project from our [Git Repository](https://github.com/ubeac/SBCGateway)

### Installation

For preparing RaspberryPi to run the project you can run the following commands.

```
$ sudo apt-get update
$ sudo apt-get upgrade

$ sudo apt-get install python3 python-pip python-dev ipython
$ sudo apt-get install bluetooth libbluetooth-dev
$ sudo pip install scapy

$ sudo pip install requests

```

For putting wifi in monitor mode you can use following commands.

```

$ sudo ifconfig wlan0 down
$ sudo iwconfig wlan0 mode monitor
$ sudo ifconfig wlan0 up
$ sudo iwconfig wlan0

```

Remember for the project to be able to run you must have a wifi adapter with monitor capabilities, not every wifi can do this. I leave some links to known ones.

[Buy the Best Wireless Network Adapter for Wi-Fi Hacking in 2018](https://null-byte.wonderhowto.com/how-to/buy-best-wireless-network-adapter-for-wi-fi-hacking-2018-0178550/).

[Best Compatible USB Wireless Adapter for BackTrack 5, Kali Linux and Aircrack-ng](https://www.raymond.cc/blog/best-compatible-usb-wireless-adapter-for-backtrack-5-and-aircrack-ng/)

[TP-link TL-WN722N](https://www.tp-link.com/us/products/details/cat-5520_TL-WN722N.html) is the one I am using. If you can get the v1.0 it will work out of the box but mine is v2.0 and it was really tricky to make it work and put it in monitor mode.

You can download this program with the following commands or you can clone the repository to your raspberry.

```
$ mkdir wifiscanner
$ cd wifiscanner

$ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/wifiScanner/HTTPPostHelper.py
$ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/wifiScanner/README.md
$ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/wifiScanner/WiFiHelper.py
$ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/wifiScanner/config.ini
$ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/wifiScanner/mon.sh
$ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/wifiScanner/wifiScanner.py
```

### Config.ini
*postAddress* is the link to the listener provided from [ubeac](http://ui.ubeac.io) or for debug you can use [HookServer](http://hook.ubeac.io).

Set the *id* and *name* as you want.

*postinterval* is the time lapse between posts to the ubeac server. It's in **seconds** and you can set it to less than a second by providing a decimal but as wifi sniff process return results every few seconds it's best to put it on at least 5 seconds.

### Running The project

After configuring your device and editing config.ini you can run it by running wifiScanner.py as **root**

```
$ sudo python3 wifiScanner.py
```

For running the project locally you can run WiFiHelper.py as **root**. This will start scanner but instead of sending data to ubeac servers it will write scans to probes.txt.

```
$ sudo python3 WiFiHelper.py
```
