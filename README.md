![Logo of the project](http://ui.ubeac.io/static/img/logo.svg)

# SBCGateway
Python gateway for ubeac service.

This is a project to provide a gateway for bluetooth beacons to work with [uBeac](http://ui.ubeac.io) .At present it runs on linux only. I've mostly developed it using Raspberry pi. however, it will also run on other linux based systems.

The scanner code is based on [Reliable Bluetooth LE (iBeacon) scanner](https://github.com/ashokgelal/iBeacon-Scanner). I've rewrite the project on python 3 and then tested it on Raspberry pi 3 B.

This project is designed to read iBeacon advertisments using a Bluetooth 4.0 dongle and sends read data to [uBeac servers](http://ui.ubeac.io).

*Be aware that this project is in its early stages of development!*
## Getting Started
These instructions will help you build a gateway from ground up.

For this project you can use raspberry pi 3 model B or B+. You can also use raspberry pi zero w or any other linux based pc or oneboard pc with network capabilities and bluetooth ver 4.

For this project you will need:
* oneboard Pc or a pc capable of Internet Connectivity and bluetooth ver 4. I am using [Raspberry PI 3 model b](https://www.raspberrypi.org/products/)
* Linux based operating system. I am using [raspbian lite](https://www.raspberrypi.org/downloads/raspbian/). current version is 4.14 June 2018
* [python 3](https://www.python.org/). I am using python version 3.5.3.
* [BlueZ api](http://www.bluez.org/). current version is 5.43.

You can run this project on your own chosen environment.I am going to give instructions for preparing a Raspberry pi to run this project on it. If you are using your own environment you can skip this part.

### Preparing raspberry pi
After you get your Raspberry pi you will need a micro sd card with at least 4Gb free space.
We are going to download the latest raspbian image and write it to the sdcard to get started with owr project.

At First you have to download raspbian lite from the official site.
[Here's the raspbian lite download page](https://www.raspberrypi.org/downloads/raspbian/).
The version I downloaded is [RASPBIAN STRETCH LITE](https://downloads.raspberrypi.org/raspbian_lite_latest) version June 2018.

After your download is complete Unzip the disk image and restore it to a microsd for raspberry pi.
I used disks program on ubuntu to restore the disk image.

Before inserting the micro sd to your raspberry there is one more thing to do.

you need to create a ssh file on sdcard's boot partition for headless raspberry pi.
I think it's more convenient than connecting it to a monitor and a keyboard.
you can open a terminal and go to the Boot partition on sdcard and use the following command  to creat the file.
```
 $ sudo touch ssh
```

Insert the sdcard into raspberry pi. connect it to the power supply and network cable and wait for it to boot.
You can find your raspberry pi's network address from your routers address list. When you find the network address make a ssh connection to it with putty or any other tools you are comftable with.

default user for raspberry fresh images is: pi
default password is: raspberry

After connecting to your raspberry pi update the default password and set a static ip for it so you wouldn't need to search for your raspberry pi's ip address later.

For updating the default password, type the following command, input the default password and then set a new one. After that you can use your new password for logins.
```
$ passwd 
```
Add a static ip to /etc/dhcpcd.conf as explained below and then you can restart your raspberry pi.
```
$ echo "interface eth0" >> /etc/dhcpcd.conf 
$ echo "static ip_address=192.168.0.70/24" >> /etc/dhcpcd.conf 
$ echo "static routers=192.168.0.1" >> /etc/dhcpcd.conf
$ echo "static  domain_name_servers=192.168.0.1 8.8.8.8" >> /etc/dhcpcd.conf
$ sudo reboot
```
You can configure your Raspberry pi to work with wifi.
Here are some good instructions on how to do so.
[adafruit Setting up Wifi with the Command Line](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-occidentalis)
[Raspberry pi Documentation](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)

After it boots up check your new ip with ifconfig
```
$ ifconfig
```

check if you have internet connectivity by pinging some ip.
```
$ ping 8.8.8.8
```

When you restore fresh disk image it doesn't expand to your hole sdcard and for being able to use it, all you need to do is to expand the root partition.
```
$ sudo raspi-config --expand-rootfs
$ sudo reboot
```

check partition sizes with 
```
$ df -h
```
It will have output like the following. look for the root partition size.
```
Filesystem      Size  Used Avail Use% Mounted on
*/dev/root       7.2G  1.2G  5.8G  17% /*
devtmpfs        460M     0  460M   0% /dev
tmpfs           464M     0  464M   0% /dev/shm
tmpfs           464M   12M  452M   3% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           464M     0  464M   0% /sys/fs/cgroup
/dev/mmcblk0p1   43M   22M   21M  51% /boot
tmpfs            93M     0   93M   0% /run/user/0
```
raspberry pi date is set to update automaticly through ntp and there is no configurations needed. you can check it with the following command.
```
$ date
```
It will have output like the following. see if it's set to UTC and has the correct date and time
```
Wed 10 Oct 08:14:55 UTC 2018
```

## Preparing Working environment

For running this project you just need [bluez](http://www.bluez.org/) and its python wraper [pybluez](https://github.com/pybluez/pybluez). you also need [requests](http://docs.python-requests.org/en/master/) for posting the data to the ubeac server.
You can install the needed libraries with the following commands or by using the instructions given in their documentation.
```
$ sudo apt-get install python3-bluez
$ sudo apt-get install libbluetooth-dev
$ sudo apt-get install python3-dev
$ sudo pip3 install PyBluez
$ sudo pip3 install requests
```
Before going any further lets check if your device is scanning for beacons. Run the following command.
```
$ sudo hcitool lescan
```
It must show you a list of availeble bluetooth devices like the following.
```
LE Scan ...
24:4B:03:EA:64:E5 (unknown)
24:4B:03:EA:64:E5 [TV] SAMSUNG TV
```
### Installing project
After installation is complete you can download the code for this project from git repository.
```
$ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/BSTest.py
$ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/JsonPoster.py
$ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/blescan.py
$ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/config.ini
```
You can use git clone to clone the repository to your project but it will need you to install git on your Raspberry pi.

## Config.ini
postAddress is the link to the listener provided from [ubeac](http://ui.ubeac.io) or for debuging you can use [HookServer](http://hook.ubeac.io).

Set the id and name as you wish.

postInterval is the time gaps between posts to the ubeac server. It's in seconds and you can set it to less than a second by providing a decimal.

scanBuffer is the amount of scans beacon scanner does before sending data to post thread. The minimum number is 1 and you can set it to 100 if you are posting data to server slowly.

If the scanBuffer is too much higher than postIntervals you will end up with some empty posts.

# Running The project

After configuring your device and editing config.ini you can run the project by running bstest.py as root
```
$ sudo python3 BSTest.py
```

you can run BSTest.py as startup script so anytime you turn on your device it will start scanning and sending data to ubeacserver.I will leave a link for structions to do so.

[Five Ways To Run a Program On Your Raspberry Pi At Startup](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)
