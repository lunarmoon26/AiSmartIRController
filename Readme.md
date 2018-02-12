# RaspberryPi HTTP IR Controller

![video tutorial](https://youtu.be/l8nb9gdubtA "video- tutorial")

## Build the circuit

![circuit schema](https "circuit schema")

![circuit image](https "circuit image")

## Test the circuit

1. Connect the circuit to GPIO pins of your choice
1. Code or download python/led.py to test your circuit
    ```python
    import RPi.GPIO as GPIO
    import time

    pin_out = 17

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_out, GPIO.OUT)

    n = 0
    while n < 1000:
        GPIO.output(pin_out, True)
        time.sleep(1)
        GPIO.output(pin_out, False)
        time.sleep(1)
        n += 1
    ```
1. View the IR led from a camera

## Configure LIRC package on your RaspberryPi

Official Guide: http://www.lirc.org/html/configuration-guide.html

Upgrade and get LIRC

    sudo apt-get update
    sudo apt-get install lirc

You need to manualy upgrade LIRC 0.9.4 by running following command. Here is the [discussion](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=192891#p1212574)

    sudo /usr/share/lirc/lirc-old2new

Append I/O and device information to /etc/module

    sudo echo 'lirc_dev' >> /etc/modules
    sudo echo 'lirc_rpi gpio_in_pin=26 gpio_out_pin=17' >> /etc/modules

and same I/O config to raspian booting script

    sudo echo 'dtoverlay=lirc-rpi,gpio_in_pin=26,gpio_out_pin=17' >> /boot/config.txt

Create a hardware.conf file in /etc/lirc

    sudo nano /etc/lirc/hardware.conf

Copy and paste the following content, or `wget` to grab from lirc/hardware.conf in the repo. [LIRC configuration file reference](https://www.mythtv.org/wiki/Ubuntu_lirc_configuration_files)

    LIRCD_ARGS="--uinput"
    LOAD_MODULES=true
    DRIVER="default"
    DEVICE="/dev/lirc0"
    MODULES="lirc_rpi"
    LIRCD_CONF=""
    LIRCMD_CONF=""

Create a virtual remote controller by creating a lircd.conf, or grab for example,  lirc/xbox-one.lircd.conf and rename it as lircd.conf

    sudo nano /etc/lirc/lircd.conf

Reboot the system and place the IR led close to your xbox, run

    irsend SEND_ONCE XBOX-ONE BUTTON_ON

Xbox is expected to be turned on. 

More remote presets are available at http://lirc.sourceforge.net/remotes/

## Setup a webservice

1. Install Flask on RaspberryPi, official guide available at:

    https://projects.raspberrypi.org/en/projects/python-web-server-with-flask


1. Code or download a simple server script from python/app.py and run it!
1. Setup the port forwarding on your router, so your Flask server can be visited from public internet
1. Setup some IFTTT Applets on ifttt.com to receive simple phrases and trigger the web API you've just created. You need to enable [Webhooks](https://ifttt.com/maker_webhooks) service.
