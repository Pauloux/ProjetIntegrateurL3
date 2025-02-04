import unicornhathd as uhd 
import time 

#configuration 
uhd.rotation(0)
uhd.brightness(0.5)

def set_led(x, y, color) : 
	""" Allume une LED à la position (x,y) avec une courleur (R,G,B) """
	uhd.set_pixel(x, y, color[0], color[1], color[2])
	uhd.show()

# j'allume la LED en rouge
set_led(5, 5, (255, 0, 0))

# attendre 20s avant d'éteindre 
time.sleep(20)
uhd.clear()
uhd.show() 
 