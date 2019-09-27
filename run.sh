#!/bin/sh

cd ~/InstantThermalPrint

while true; do
    sudo pkill -f gvfs
    python print_manager.py
    sleep 5
done