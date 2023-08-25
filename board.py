from gpiozero import LED, Button
from time import sleep
from signal import pause
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------
owm = OWM('9feb8ab55ac666276d6eed156cbec7eb')
mgr = owm.weather_manager()

place = input("Please enter a city\n")

place = place.lower()
observation = mgr.weather_at_place("accra")

w = observation.weather

detailed = w.detailed_status        
wind = w.wind()                  
humidity = w.humidity                
temperature = w.temperature('celsius') 
rain = w.rain                    
heat = w.heat_index             
clouds = w.clouds 


print(f"In {place.upper()} there's, {detailed} \nthe speed of wind is {wind['speed']} \nthe humidity is {humidity} \nthe temperature is {temperature['temp']} degrees celcius \nrain is {rain} \nheat is {heat} \nand cloud is {clouds}")



red = LED(17)
yellow = LED(26)
green = LED(21)
buzzer = LED(22)
button = Button(2)

print(button)





time = 5

def redOn():
    red.on()
    yellow.on()
    green.on()
    buzzer.on()

def redOff():
    red.off()
    yellow.off()
    green.off()
    buzzer.off()

def yellowOn():
    yellow.on()
    sleep(time)
    yellow.off()

def greenOn():
    green.on()
    sleep(time)
    green.off()

def buzzerOn():
    buzzer.on()
    sleep(0.2)
    buzzer.off()
    sleep(0.1)


button.when_pressed = redOn
button.when_released = redOff

pause()
if(rain):
    print(rain)
    greenOn()
else:
    redOn()