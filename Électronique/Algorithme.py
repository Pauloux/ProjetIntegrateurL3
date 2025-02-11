import unicornhathd as uhd
import time
import os

def prendre_image(nom_image="test", temps_expo_us="50000", raw=False):
    if not raw:
        commande = f"rpicam-still -o {nom_image}.jpeg --shutter {temps_expo_us} --immediate"
    else:
        commande = f"rpicam-raw -o {nom_image}.raw"
    os.system(commande)

# Configuration de la matrice LED
uhd.rotation(0)
uhd.brightness(0.1)  # Réduire la luminosité

def set_led(x, y, color):
    """Allume une LED à la position (x,y) avec la couleur (R,G,B)"""
    uhd.set_pixel(x, y, color[0], color[1], color[2])
    uhd.show()

# Création de l'ordre des LEDs en serpentin 16x16
ordre_des_leds = []
for i in range(16):
    start = i * 16 + 1
    end = (i + 1) * 16
    if i % 2 == 0:
        ordre_des_leds.append(list(range(start, end + 1)))
    else:
        ordre_des_leds.append(list(range(end, start - 1, -1)))

nom_du_dossier = "Images"
temps_exposition = 2

# Vérification/Création du dossier de sortie
if not os.path.exists(nom_du_dossier):
    os.makedirs(nom_du_dossier)

# Parcours de toutes les LEDs
for numero_recherche in range(1, 257):
    # Recherche de la position de la LED
    position_trouvee = None
    for i, ligne in enumerate(ordre_des_leds):
        if numero_recherche in ligne:
            j = ligne.index(numero_recherche)
            position_trouvee = (i, j)
            break
    
    if position_trouvee:
        x, y = position_trouvee
        
        # Allumage de la LED en blanc
        set_led(x, y, (255, 255, 255))
        
        # Capture de l'image
        nom_image = os.path.join(nom_du_dossier, f"Image{numero_recherche}")
        #prendre_image(nom_image, "50000", raw=True)
        time.sleep(0.1)  # Délai supplémentaire pour s'assurer que la LED est éteinte
        time.sleep(temps_exposition)
        # Extinction de la LED
        set_led(x, y, (0, 0, 0))
        
        
        # Éteindre toutes les LEDs pour éviter la persistance
        uhd.off()
        uhd.show()
        
        

# Éteindre toutes les LEDs avant de quitter
uhd.off()
