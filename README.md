![Logo of the project](http://ui.ubeac.io/static/img/logo.svg)


# SBCGateway

## Pre requirments
For this project you can use raspberry pi 3 model B or B+.You can use raspberry pi zero w or any linux based pc or oneboard pc with network capabilities and bluetooth ver 4.

## prepare raspberry pi
At First you have to download raspbian lite from the official site.
[Here's raspbian lite download page](https://www.raspberrypi.org/downloads/raspbian/)

Unzip the disk image and restore it to a microsd for raspberry pi.

Before inserting the micro sd to your raspberry there is one more thing to do.

you need to creat ssh file on sdcard's boot partition for headless raspberry pi.
I think it's more convenient than connecting it to monitor and keyboard.

 $ sudo touch ssh

Insert sdcard into raspberry pi.connect it to power supply and network cable and wait for it to boot.
You can find your raspberry pis network address from your routers address list.When you find the network address make a ssh connection to it with putty or any tool you are comftable with.

default user for raspberry fresh images are : pi
default password is : raspberry

After connecting to your raspberry pi update the default password and set a static ip for it so you wouldn't need to search for your raspberry pi's ip address later.

For updating default password type command blow and then input default password and then set a new one After that you can use your new password for logins.
 
 $ passwd 

Add a static ip to /etc/dhcpcd.conf as below and then you can restart your raspberry pi.

 $ echo "interface eth0" >> /etc/dhcpcd.conf 
 $ echo "static ip_address=192.168.0.70/24" >> /etc/dhcpcd.conf 
 $ echo "static routers=192.168.0.1" >> /etc/dhcpcd.conf
 $ echo "static  domain_name_servers=192.168.0.1 8.8.8.8" >> /etc/dhcpcd.conf
 $ sudo reboot

After it boots up check your new ip with ifconfig

 $ ifconfig

check if you have internet connectivity by pinging some ip.

 $ ping 8.8.8.8

When you restore fresh disk image it doesn't expand to your hole sdcard and for being able to use it all you need to expand root partition.

 $ sudo raspi-config --expand-rootfs
 $ sudo reboot

// check partition sizes with 
 $ df -h
// look for root partition size.

raspberry pi date is set to update automaticly throuth ntp and there is no configuration needed

// check system date with 
 $ date
// see if its set to utc and is a correct date and time

## Installing needed libraries
For running this project you just need bluez and its python wraper.you need requests for posting the data to ubeac server.
You can install needed libraries with commands below.

 $ sudo apt-get install python3-bluez
 $ sudo apt-get install libbluetooth-dev
 $ sudo apt-get install python3-dev
 $ sudo pip3 install PyBluez
 $ sudo pip3 install requests

After installation is complete you can download the code for this project from git repository build folder.

 $ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/builds/BSTest.py
 $ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/builds/JsonPoster.py
 $ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/builds/blescan.py
 $ wget https://raw.githubusercontent.com/ubeac/SBCGateway/master/builds/config.ini

## Config.ini file

postAddress is the link to the listener provided from [ubeac](http://ui.ubeac.io) or for debug you can use [HookServer](http://hook.ubeac.io).

Set the id and name as you want.

postInterval is the time laps between posts to the ubeac server.It's in seconds and you can set it to less than a second by providing a decimal.

scanBuffer is the amount of scans beacon scanner do before sending data to post thread minimum number is 1 and you can set it to 100 if you are posting data to server slowly.

If the scanBuffer is to much higher than postIntervals you will end up with empty posts.

After configuring your device you can run project by running bstest.py as root
$sudo python3 BSTest.py

you can run BSTest.py as startup script so anytime you turn on your device it will start scanning and sending data to ubeacserver