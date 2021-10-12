
# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'soybello'
password = 'rosa0000'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led5 = Pin(5, Pin.OUT)
led4 = Pin(4, Pin.OUT)
led0 = Pin(0, Pin.OUT)
led2 = Pin(2, Pin.OUT)

print('Finish pins...')

