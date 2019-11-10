import unicornhat as uh
import time
while True:
	uh.set_layout(uh.PHAT)
	uh.brightness(0.5)

	uh.set_pixel(0, 0, 255, 0, 0)
	uh.show()

	time.sleep(1)

	uh.clear()
	uh.show()

	for x in range(8):
    		for y in range(4):
        		uh.set_pixel(x, y, 0, 255, 255)
	uh.show()
	time.sleep(1)
	uh.clear()
