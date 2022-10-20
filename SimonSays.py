import time
import board
import touchio
import digitalio as dio
import random

my_list = ['red', 'green', 'blue', 'yellow']


def fade_out(color, increment):
    rgb = color
    maximum = max (rgb[0], max(rgb[1], rgb[2]))
    r_inc = rgb[0] / maximum
    g_inc = rgb[1] / maximum
    b_inc = rgb[2] / maximum
    r, g, b = rgb
    while r >= 0 and g >= 0 and b >= 0:
        r -= r_inc
        g -= g_inc
        b -= b_inc
        np.fill((int(r), int(g), int(b)))
        np.show()
        time.sleep(increment)
def fade_in(color, increment):
    rgb = color
    r, g, b = rgb
    r_final = r
    g_final = g
    b_final = b
    print(r_final, g_final, b_final)
    maximum = max(rgb[0], max(rgb[1], rgb[2]))
    r_inc = rgb[0] / maximum
    g_inc = rgb[1] / maximum
    b_inc = rgb[2] / maximum
    r, g, b = 0, 0, 0
    while r <= r_final and g <= g_final and b <= b_final:
        r += r_inc
        g += g_inc
        b += b_inc
        np.fill((int(r), int(g), int(b)))
        np.show()
        time.sleep(increment)
def color_wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def switch_color(wait):
    for j in range(255):
        for i in range(len(pixels)):
            rc_index = (i * 256 // len(pixels)) + j
            pixels[i] = wheel(rc_index & 255)
        time.sleep(wait)
        
touch_pad = board.A1
touch = touchio.TouchIn(touch_pad)
led = dio.DigitalInOut(board.LED)
led.direction = dio.Direction.OUTPUT
my_list.append(random.randint(0, 4))

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
