from gpiozero import LED
from time import sleep

RedLed= LED(17)
YellowLed=LED(27)
GreenLed=LED(22)
x = 0

while x < 5:
    RedLed.on()
    print("LED RED IS ON")
    sleep(5)
    RedLed.off()
    print("LED RED IS OFF")
    sleep(1)


    YellowLed.on()
    print("LED YELLOW IS ON")
    sleep(5)
    YellowLed.off()
    print("LED YELLOW IS OFF")

    sleep(1)




    GreenLed.on()
    print("LED GREEN IS ON")
    sleep(5)
    GreenLed.off()
    print("GREEN IS OFF")
    sleep(1)

    x +=1



    

