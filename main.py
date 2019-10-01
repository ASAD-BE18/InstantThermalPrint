from print_manager import queue_and_print
import RPi.GPIO as GPIO

#           Pi pinout for reference.......
#                        J8
#                        .___.
#               +3V3---1-|O O|--2--+5V
#       (SDA)  GPIO2---3-|O O|--4--+5V
#      (SCL1)  GPIO3---5-|O O|--6--_
# (GPIO_GLCK)  GPIO4---7-|O O|--8-----GPIO14 (TXD0)
#                   _--9-|O.O|-10-----GPIO15 (RXD0)
# (GPIO_GEN0) GPIO17--11-|O O|-12-----GPIO18 (GPIO_GEN1)
# (GPIO_GEN2) GPIO27--13-|O O|-14--_
# (GPIO_GEN3) GPIO22--15-|O O|-16-----GPIO23 (GPIO_GEN4)
#               +3V3--17-|O O|-18-----GPIO24 (GPIO_GEN5)
#  (SPI_MOSI) GPIO10--19-|O.O|-20--_
#  (SPI_MOSO) GPIO9 --21-|O O|-22-----GPIO25 (GPIO_GEN6)
#  (SPI_SCLK) GPIO11--23-|O O|-24-----GPIO8  (SPI_C0_N)
#                   _-25-|O O|-26-----GPIO7  (SPI_C1_N)
#    (EEPROM) ID_SD---27-|O O|-28-----ID_SC Reserved for ID EEPROM
#             GPIO5---29-|O.O|-30--_
#             GPIO6---31-|O O|-32-----GPIO12
#             GPIO13--33-|O O|-34--_
#             GPIO19--35-|O O|-36-----GPIO16
#             GPIO26--37-|O O|-38-----GPIO20
#                   _-39-|O O|-40-----GPIO21
#                        '---'
#                    40W 0.1" PIN HDR
#       (https://github.com/tvierb/raspberry-ascii)

if __name__ == "__main__":

    button_pin = 3  # Using BCM3 (Physical 5)

    try:
        # ---------------- SETUP GPIO ------------------------------------------------------------|
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(button_pin, GPIO.IN)  # Set button as input

        # Set up a callback to call the queue and print function upon falling edge on button
        GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=queue_and_print, bouncetime=1500)

        # ---------------- MAIN LOOP -------------------------------------------------------------|
        while True:
            if GPIO.event_detected(button_pin):
                print('Button pressed')

    finally:
        # Upon unexpected end-of-universe python script heat-death,
        GPIO.cleanup(button_pin)  # Clean the GPIO resource
