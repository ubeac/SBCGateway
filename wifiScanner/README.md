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
