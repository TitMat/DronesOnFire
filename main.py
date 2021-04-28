# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

from drone import Drone
from zone import Zone


# Demande du nombre de drones à instancier
nombreDrones = input("Combien de drone doivent être envoyés sur zone ?")

# Instanciation zone
z1 = Zone(1, "Zone1", 0, 0, 10, 10)

# Largeur d'un secteur
largeurSecteur = z1.longitude2/int(nombreDrones)

# Affecte une temperature haute de manière aléatoire à un point de la zone
def startFeuZone(zone):
    global latitudeFeu
    global longitudeFeu
    print("Feu démarré à des coordonnées aléatoires")
    latitudeFeu = random.randrange(1, zone.latitude2)
    print("Latitude feu: " + str(latitudeFeu))
    longitudeFeu = random.randrange(1, zone.longitude2)
    print("Longitude feu: " + str(longitudeFeu))


startFeuZone(z1)

# Retourne la temperature aux coordonnées du drone
def getTemperature(drone):
    #print("Demande de température pour le drone de coordonnées : " + str(drone.latitude) + " x " + str(drone.longitude))
    if drone.latitude == latitudeFeu and drone.longitude == longitudeFeu:
        return 200
    else:
        return 20

#Simule le déplacement d'un drone dans la zone et à chaque mouvement le controle de la temperature
def parcourirZone(drone, zone):
    print("Positionnement du drone aux coordonnées : " + str(drone.latitude) + " x " + str(drone.longitude))
    print("Parcours de la zone jusqu'aux coordonnées : " + str(zone.latitude2) + " x " + str(zone.longitude2))
    feuTrouve = False
    while drone.latitude < zone.latitude2 and feuTrouve is False:
        while drone.longitude < zone.longitude2 and feuTrouve is False:
            if getTemperature(drone) > 50:
                print("Feu suspecté à la position : " + str(drone.latitude) + " x " + str(drone.longitude))
                feuTrouve = True
            drone.longitude = drone.longitude + 1
        drone.latitude = drone.latitude + 1
        drone.longitude = 0

# Instanciation et envoi drones
for i in range(1,int(nombreDrones)+1):
    d1 = Drone(i, "Drone"+str(i), 0, 0)
    parcourirZone(d1, zone(i, "Zone"+str(i),))

