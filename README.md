# Video Doorbell
This project is based on a previous [Pi Stream Camera Project](https://github.com/EbenKouao/Pi-Smart-Doorbell) from [EbenKouao](https://github.com/EbenKouao).
It is modified to send Push Notifications and uses the [gpiozero](https://gpiozero.readthedocs.io/en/stable/) library.


# Parts of this project

- Raspberry Pi 4B
- Raspberry Pi Camera Module
- Relay Module DC 5V
- Power Supply DC 12V
- 24 IR Infrared LED Light 
- Electric Lock
- Pushover Message API
- Python 3


# Functions

After the doorbell's button is pressed, the Raspberry starts a camera live stream over the web via Flask.
In this case, a tablet gets notified by a Push Message from Pushover. From the tablet, you can open the live stream via the web(use a static IP for the Raspberry Pi) and unlock the door by clicking a button.
The [gpiozero](https://gpiozero.readthedocs.io/en/stable/) library controls the relay switches.
If there is no response from the tablet within 40 seconds, a Push Notification is sent to a handy, which can open the live stream and unlock the door again. Note that you have to configure port forwarding to connect to the Raspberry Pi from outside your network. Within your network, you can access the live stream via:
`raspberry_pi_ip:5000` 

At the end "script.sh" runs to end and restart the "main.py".

# Dependencies
```
sudo apt update 
sudo apt upgrade

sudo apt install libatlas-base-dev
sudo apt install libjasper-dev
sudo apt install libqtgui4 
sudo apt install libqt4-test
sudo apt install libhdf5-dev
sudo apt install python3-gpiozero

sudo pip3 install flask
sudo pip3 install numpy
sudo pip3 install opencv-contrib-python
sudo pip3 install imutils
sudo pip3 install opencv-python
```

