import time
from machine import Pin

buildin_led = Pin(2, Pin.OUT)

for i in range(10):
    buildin_led.value(1)
    time.sleep(0.5)
    buildin_led.value(0)
    time.sleep(0.5)