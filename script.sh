#!/bin/bash

sudo pkill --signal 9 python3
sleep 4
sudo python3 main.py
sleep 3

exit 0
