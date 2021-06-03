
import blynklib_mp as blynklib
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network             # allow us to connet esp32 to a wifi network
from time import sleep

import esp
esp.osdebug(None)           # garbage collector

import gc
gc.collect()

ssid = 'wifi_name'
password = 'wifi_password'

BLYNK_AUTH = 'project token'

station = network.WLAN(network.STA_IF)   # make our eps as WiFi station

station.active(True)
station.connect(ssid, password)          # connect out esp board to our router which is the access point

while station.isconnected() == False:    # if esp isn't connected to the network , enter an infinite loop waiting for connection
  pass

print('Connection successful')
print(station.ifconfig())               # print ip address of the esp 



# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

# initialize inputs and outputs
# inputs : flame sensor
# outputs : led

led = Pin(23, Pin.OUT)
sensor1 = Pin(22 , Pin.IN)


while True :
  blynk.run()
  print ('welcome to the fire system')
  
  if sensor1.value() == True:   # flame sensor becomes active
    blynk.notify('Warning critical value')  # send a notification on the mobile app
    led.value(1)              # blink LED
    print('LED ON')
    sleep(1)
    led.value(0)
    print('LED OFF')
    sleep(1)
    
  else :
    led.value(0)        # turn OFF the led
    print('LED OFF')
    
    
  


