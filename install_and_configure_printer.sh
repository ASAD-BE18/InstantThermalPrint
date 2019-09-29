# Bash script to install prerequisits
echo "\n[:] Updating apt-get\n\n"
sudo apt-get update -yqq

echo "\n[:] Installing Pre-reqs\n\n"
sudo apt-get install gphoto2 git cups wiringpi build-essential libcups2-dev libcupsimage2-dev -yqq

echo "\n[:] Getting printer driver\n\n"
git clone https://github.com/adafruit/zj-58
cd zj-58
make
sudo ./install

echo "\n[:] Setting printer parameters\n\n"
# ------------ Set serial baudrate according to printer, and AMA0 or USB0 depending on TTL or USB printer.
sudo lpadmin -p ZJ-58 -E -v serial:/dev/ttyAMA0?baud=19600 -m zjiang/ZJ-58.ppd
echo "\n[:] Setting printer to default\n\n"
sudo lpoptions -d ZJ-58

sudo sed -i -e '$i \sleep 5' /etc/rc.local
sudo sed -i -e '$i \sudo pkill -f gvfs' /etc/rc.local
sudo sed -i -e '$i \cd ~/InstantThermalPrint/ && bash run.sh'
sudo sed -i -e '$i \rm ~/InstantThermalPrint/whitelist.txt'

echo "\n\n[:] Setup is complete..."