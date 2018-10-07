Here are the build 
write raspbian stretch lite version 4.14 to a 8gb microsd.

creat ssh file on sdcard's boot partition.
 $ sudo touch ssh

-insert sdcard in raspberry pi.connect it to power supply and network cable

update default password 
 $ passwd 

add static ip to /etc/dhcpcd.conf as below

 $ echo "interface eth0" >> /etc/dhcpcd.conf 
 $ echo "static ip_address=192.168.0.70/24" >> /etc/dhcpcd.conf 
 $ echo "static routers=192.168.0.1" >> /etc/dhcpcd.conf
 $ echo "static  domain_name_servers=192.168.0.1 8.8.8.8" >> /etc/dhcpcd.conf
 $ sudo reboot

// check the new ip address 
 $ ifconfig
// see if the ip address is correct

expand root partition 

 $ sudo raspi-config --expand-rootfs
 $ sudo reboot

// check partition sizes with 
 $ df -h
// look for root partition size.

raspberry pi date is set to update automaticly throuth ntp and there is no configuration needed

// check system date with 
 $ date
// see if its set to utc and is a correct date and time

install bluez library
 $sudo apt-get install python3-bluez

sudo apt-get install libbluetooth-dev
sudo apt-get install python3-dev
sudo pip3 install PyBluez

sudo pip3 install requests

copy blescan.py - bstest.py - jsonposter.py to a folder on rpi
run bstest.py as root
$sudo python3 BSTest.py

