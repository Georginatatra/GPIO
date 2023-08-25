from gpiozero import LED
from time import sleep

red_led = LED(18)
yellow_led = LED(17)
green_led = LED(27)

while True:
	red_led.on()
	sleep(4) 
	red_led.off()
	yellow_led.on()
	sleep(2)
	yellow_led.off()
	green_led.on()
	sleep(4)
	green_led.off()
	yellow_led.on()
	sleep(2)
	yellow_led.off()


