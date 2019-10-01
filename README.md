# InstantThermalPrint
Code to run on PiZero, instantly print images from my camera onto thermal paper.

Installation:
```
git clone https://github.com/g-bulgarit/InstantThermalPrint.git
cd InstantThermalPrint && sudo bash install_and_configure_printer.sh
```
Installation may take a while as it installs CUPS and required drivers...

Overall components for the project:
```
* Raspberry Pi-Zero
* Canon EOS 1200D camera
* USB cable between the camera and the Pi-Zero
* Phone powerbank, 5000 mAh lasts quite a while

System Diagram:
+------------------------------------------+         +--------------------------+
|                                    |PWR  |         | Powerbank, 5v 5000mAh    |
|   TTL Thermal printer              |    <----------+                          |
|                                    |     |         |                          |
|                                    |     |         |                          |
|                                    +-----+         |                          |
|                                          |         |                          |
|   +------+ +-------+  +-------+          |         |                          |
|   |TX    | |RX     |  |GND    |          |         |                          |
+------+---+-----+---+------+---+----------+         |                          |
       |         |          |                        |                          |
       |         |          |                        |                          |
+------------------------------------------+         |                          |
|  +---v---------v----------v----------+   |         |                          |
|  |    BCM14    BCM15 |40 pin header| |   |         |                          |
|  +-----------------------------------+   |         |                          |
|      |BCM5     |GND                      |         |                          |
|      |         |                         |         |                          |
|      |         |                         |    +----+                          |
|      |         |                         |    |    |                          |
| Pi Zero        |                         |    |    |                          |
+------+---------------+-----+--------+ +--+    |    +--------------------------+
       |         |     |     |       |PWR  <----+
+------v---------v+    +--^--+       +-----+
|                 |       |
|Push Button      |       |
+-----------------+       |
+-------------------------+--+-------------+
|                      |Data |             |
|                      |Conn |             |
|                      +-----+             |
|                                          |
|                                +---------+
|                                |(SD card)|
| Canon EOS 1200D                +---------+
+------------------------------------------+
```
