from gpiozero import LED
from time import sleep

led = LED(17)

# blinking an LED forever
while True:
  #set the led ON for one second
  led.on()
  sleep(1)
  #set the led ON for one second
  led.off()
  sleep(0.06)

  #set the led ON for one second
  led.on()
  sleep(0.7)
  #set the led ON for one second
  led.off()
  sleep(0.9)