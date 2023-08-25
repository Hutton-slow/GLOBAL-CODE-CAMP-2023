import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
buzzer_pin = 17

GPIO.setup(buzzer_pin, GPIO.OUT)


def buzzer_sound(frequency, duration):
    period = 1.0 / frequency
    delay = period /2
    cycles = int(duration * frequency)


    for _ in range(cycles):
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(buzzer_pin, GPIO.LOW)
        time.sleep(6)

try:
    buzzer_sound(4, 2)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
