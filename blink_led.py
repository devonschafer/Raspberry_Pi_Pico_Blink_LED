from machine import Pin
import utime

#pin 0 is the GPIO 0 (GP0)
led = Pin(0, Pin.OUT)

#this is the run loop
while True:
    #toggle is the built in logic
    led.toggle()
    #wait for one second
    utime.sleep(1)
    