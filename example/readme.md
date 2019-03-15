# IoT Node Framework
This code provides a framework for running embedded code with multiple modular sources of data input/output.

## Hardware
Intended to run on a tinkerforge redbrick and Raspberry Pi but can run on any system with the required python dependencies installed.

## Installation
Requirements for Debian based systems:
```
sudo apt-get install libusb-1.0-0 libudev0 pm-utils
wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
sudo dpkg -i brickd_linux_latest_armhf.deb
apt install python-dev python-setuptools libjpeg-dev python-cryptography 
pip install -r requirements.txt
```


Testing mode:
```
./python controller.py
```

Installation on Redbrick / Debian Jessie:
```
sudo cp deskcontrol /etc/init.d/deskcontrol
sudo update-rc.d deskcontrol defaults
sudo service deskcontrol start
```

## Contributors
Ben Hussey (<a href="mailto:ben@blip2.net">ben@blip2.net</a>)
