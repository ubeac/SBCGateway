![Logo of the project](http://ui.ubeac.io/static/img/logo.svg)

# BLE Scanner
This is a gateway for the ubeac project.
It will Scan for **[ble advertisements](https://en.wikipedia.org/wiki/Bluetooth_advertising)** and send them to **[ubeac](http://ui.ubeac.io)** servers.

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

*postinterval* is the time lapse between posts to the ubeac server. It's in **seconds** and you can set it to less than a second by providing a decimal.

*scanBuffer* is the amount of scans beacon scanner do before sending data to post thread minimum number is 1 and you can set it to 100 if you are posting data to server slowly.

If the *scanBuffer* is too much higher than *postInterval* you will end up with some empty posts.

### Running The project

After configuring your device and editing config.ini you can run it by running bleScanenr.py as **root**

```
$ sudo python3 bleScanner.py
```

For running the project locally you can run BleHelper.py as **root**. This will start scanner but instead of sending data to ubeac servers it will write scans to ble.txt.

```
$ sudo python3 BleHelper.py
```

For detailed instructions on how to config your raspberry pi and run this project read [readmeDetail.md](https://github.com/ubeac/SBCGateway/blob/master/bleScanner/readmeDetail.md)

