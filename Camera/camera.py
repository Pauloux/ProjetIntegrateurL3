import os

def prendre_image(nom_image="test", temps_expo_us="50000",raw=False):
	
	if(raw==False):	
		commande= "rpicam-still -o" + nom_image + ".jpeg" + " --shutter " + temps_expo_us + " --immediate"
	else:
		commande="rpicam-raw -o" + nom_image + ".raw" 
		
	os.system(commande)
	
	
prendre_image("testtttttt","50000",raw=True)
#os.system('rpicam-raw --output test.raw')

