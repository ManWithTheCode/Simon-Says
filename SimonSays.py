# Simon-Says Coding Attempt
import time
import board
import touchio
import digitalio as dio
import neopixel

my_list = [red, green, blue, yellow]
def simon_says(my_list):
  rgb = [255, 0, 0]
  Touch1 = rgb
  
touch_pad = board.A1
touch = touchio.TouchIn(touch_pad)
led = dio.DigitalInOut(board.LED)
led.direction = dio.Direction.OUTPUT 
my_list = [red, green, blue, yellow]

A1 = board.AI
A2 = board.A2
A3 = board.A3
A4 = board.A4

Touch1 = touchio.TouchIn(A1)
Touch2 = touchio.TouchIn(A2)
Touch3 = touchio.TouchIn(A3)
Touch4 = touchio.TouchIn(A4)

while True:
  
  print(my_list)
