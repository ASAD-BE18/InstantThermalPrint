#!/bin/sh

#cd ~/InstantThermalPrint
sudo pkill -f gvfs  # Kill the gvfs processes...
python main.py
