![Logo of the project](http://ui.ubeac.io/static/img/logo.svg)

# BT Scanner
This is a gateway for the ubeac project.
It will Scan for discoverable Bluetooth devices and send them to **[ubeac](http://ui.ubeac.io)** servers.

## Getting started
For running this project you will need a fresh installation of [raspbian lite](https://www.raspberrypi.org/downloads/raspbian/) on Bluetooth enable [RaspberryPi](https://www.raspberrypi.org/products/).
You need to have [python 3](https://www.python.org/), [pybluez](https://github.com/pybluez/pybluez) and [requests](http://docs.python-requests.org/en/master/).

You can get the project from our [Git Repository](https://github.com/ubeac/SBCGateway)

### Installation

For preparing RaspberryPi to run the project you can run the following commands.

```
$ sudo apt-get update
$ sudo apt-get upgrade

$ sudo apt-get install python3 python-pip python-dev ipython
$ sudo apt-get install bluetooth libbluetooth-dev
$ sudo pip install pybluez

$ sudo pip install requests

```

### Config.ini
*postAddress* is the link to the listener provided from [ubeac](http://ui.ubeac.io) or for debug you can use [HookServer](http://hook.ubeac.io).

Set the *id* and *name* as you want.

*postinterval* is the time lapse between posts to the ubeac server. It's in **seconds** and you can set it to less than a second by providing a decimal but as Bluetooth inquiry at least takes 10 seconds to find all nearby devices it is better to set it at least 10.

### Running The project

After configuring your device and editing config.ini you can run it by running btScanenr.py as **root**

```
$ sudo python3 btScanner.py
```

For running the project locally you can run InqueryHelper.py as **root**. This will start scanner but instead of sending data to ubeac servers it will write scans to btinquery.txt.

```
$ sudo python3 InqueryHelper.py
```
