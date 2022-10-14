# Simon-Says Coding Attempt
import time
import board
import touchio
import digitalio as dio

touch_pad = board.A1
touch = touchio.TouchIn(touch_pad)
led = dio.DigitalInOut(board.LED)
led.direction = dio.Direction.OUTPUT 
my_list = [red, green, blue, yellow]
my_list.append(random.randint(0, 4))

while True:
    
  print(my_list)
