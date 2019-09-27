# Bash script to install prerequisits
echo "[:] Updating apt-get\n\n"
sudo apt-get update

echo "[:] Installing Pre-reqs\n\n"
sudo apt-get install gphoto2 git cups wiringpi build-essential libcups2-dev libcupsimage2-dev -yqq

echo "[:] Getting printer driver\n\n"
git clone https://github.com/adafruit/zj-58
cd zj-58
make
sudo ./install

echo "[:] Setting printer parameters\n\n"
sudo lpadmin -p ZJ-58 -E -v serial:/dev/ttyAMA0?baud=19600 -m zjiang/ZJ-58.ppd
echo "[:] Setting printer to default\n\n"
sudo lpoptions -d ZJ-58

sudo sed -i -e '$i \sleep 5' /etc/rc.local
sudo sed -i -e '$i \sudo pkill -f gvfs' /etc/rc.local
sudo sed -i -e '$i \cd ~/InstantThermalPrint/ && bash run.sh

echo "\n\n[:] Setup is complete..."