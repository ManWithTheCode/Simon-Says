import board
import neopixel
import time
import random

BRIGHTNESS = 1.0
np = neopixel.NeoPixel(board.A1, 10, brightness=BRIGHTNESS, auto_write=False)
num_pixels = 10


def fire(background, foreground):
    for j in range(45):
        intensity = random.random() * 0.7 + 0.3
        i_background = [int(i * intensity) for i in background]
        np.fill(i_background)
        for i in range(random.randint(2, int(num_pixels/5))):
            intensity = random.random() * 0.7 + 0.3
            i_foreground = [int(i * intensity) for i in foreground]
            rgb[random.randint(0, num_pixels-1)] = i_foreground
        np.show()
        time.sleep(0.06)

'''
Function: light
Description: Creates lightning
Parameters: back: base color for lightning, fore: color used to flash
return value: none
'''
def light(back, fore):
    ran = random.random()/20
    for j in range(10):
        intense = random.random() * 0.7 + 0.3
        i_back = [int(i * intense) for i in back]
        np.fill(i_back)
        for i in range(random.randint(2, int(num_pixels/5))):
            intense = random.random() * 0.7 + 0.3
            i_fore = [int(i * intense) for i in fore]
            np[random.randint(0, num_pixels-1)] = i_fore
        np.show()
        time.sleep(ran)
def fade_out(color, sec=0.001):
    mx = max(color[0], max(color[1], color[2]))
    r_inc = color[0]/mx
    g_inc = color[1]/mx
    b_inc = color[2]/mx
    while color[0] >= 0 and color[1] >= 0 and color[2] >= 0:
        color[0] -= r_inc
        color[1] -= g_inc
        color[2] -= b_inc
        rgb.fill((int(color[0]), int(color[1]), int(color[2])))
        rgb.show()
        time.sleep(sec)
# Changes Opacity and makes the color visible again after the fadeout
def fade_in(color, sec=0.001):
    r, g, b = color
    r1 = r
    g1 = g
    b1 = b
    mx = max(color[0], max(color[1], color[2]))
    r_inc = color[0]/mx
    g_inc = color[1]/mx
    b_inc = color[2]/mx
    r = 0
    b = 0
    g = 0
    while r < r1 and g < g1 and b < b1:
        r += r_inc
        g += g_inc
        b += b_inc
        rgb.fill((int(r), int(g), int(b)))
        rgb.show()
        time.sleep(sec)

def sparkle(color1, color2, delay):
    np.fill(color1)
    for i in range(4):
        np[random.randint(0, 9)] = color2
    np.show()
    time.sleep(delay)
leds = [0 for x in range(10)]
print(leds)
result = 0
number = 4
for q in range(100):
    for j in range(len(leds)):
        leds[j] = 1
    for i in range(len(leds)):
        if i % number == result:
            leds[i] = 0
    print(leds)
    print(result)
    result += 1
    result %= number
def chase(color1, color2, loop=20, count=3, delay=0.1):
    result = 0
    for outer in range(count * loop):
        np.fill(color1)
        for i in range(num_pixels):
            if i % count == result:
                np[i] = color2
        np.show
        time.sleep(delay)
        result += 1
        result %= count
        np.show()

while True:
    for i in range(3):
        fire((36, 2, 120), (95, 52, 145))
        light((255, 129, 0), (255, 129, 0))
    fire((36, 2, 120), (95, 52, 145))
    fade_out([36, 2, 120], 0.01)
    fade_in([0, 75, 0], 0.01)
    fade_out([0, 75, 0], 0.01)
    chase((240, 15, 3), (57, 3, 0))
    fade_out([240, 15, 3], 0.01)
    sparkle((255, 129, 0), (85, 78, 0))
