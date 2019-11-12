import time
import unicornhat as uh
uh.set_layout(uh.PHAT)
uh.brightness(0.5)

for x in range(8):
    for y in range(4):
        uh.set_pixel(x, y, 168, 50, 129)
uh.show()
time.sleep(10)
