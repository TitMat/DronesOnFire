# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

from drone import Drone
from zone import Zone
import turtle
tur = turtle.Turtle()


# Demande du nombre de drones à instancier
# Demande de la longuer de la zone
# Demande de la largeur de la zone
nombreDrones = int(input("Combien de drone doivent être envoyés sur zone ?"))
longueurZone = int(input("Quelle est la longueur de la zone ?"))
largeurZone = int(input("Quelle est la largeur de la zone ?"))
# Instanciation zone
z1 = Zone(1, "Zone1", 0, 0, longueurZone, largeurZone)

# Largeur d'un secteur
largeurSecteur = round(z1.longitude2/nombreDrones)

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

    print("Positionnement du drone aux coordonnées : " + str(zone.latitude) + " x " + str(zone.longitude))
    drone.latitude = zone.latitude
    drone.longitude = zone.longitude
    if drone.id == 1:
        tur.left(90)
    tur.setposition(drone.latitude*10, drone.longitude*10)
    tur.setpos(drone.latitude*10, drone.longitude*10)
    print("Parcours de la zone jusqu'aux coordonnées : " + str(zone.latitude2) + " x " + str(zone.longitude2))
    feuTrouve = False
    tur.pendown()
    while drone.latitude < zone.latitude2: #and feuTrouve is False:
        while drone.longitude < zone.longitude2 and drone.longitude >= zone.longitude: #and feuTrouve is False:
            if getTemperature(drone) > 50:
                print("*** Feu suspecté à la position : " + str(drone.latitude) + " x " + str(drone.longitude))
                #feuTrouve = True
                #tur.penup()
                showfire()
            drone.longitude = drone.longitude + (-1) ** (drone.deplacement)
            tur.forward((-1) ** (drone.deplacement) * 10)
        if (-1) ** (drone.deplacement) == (1):
            tur.right(90)
            drone.latitude = drone.latitude + 1
            if drone.latitude < zone.latitude2:
                tur.forward(10)

            tur.left(90)
        else:
            tur.right(90)
            drone.latitude = drone.latitude + 1
            if drone.latitude < zone.latitude2:
                tur.forward(10)

            tur.left(90)
        drone.deplacement = drone.deplacement + 1
        drone.longitude = drone.longitude + (-1)**(drone.deplacement)
    tur.penup()

    if drone.id == 1 or drone.id == nombreDrones:
        drone.latitude = zone.latitude2
        if drone.id == 1:
            drone.longitude = zone.longitude
        else:
            drone.longitude = zone.longitude2
        if (-1) ** (drone.deplacement) == -1:
            if drone.id == 1:
                tur.right(180)
                tur.forward(largeurSecteur * 10)
                tur.left(180)
        if (-1) ** (drone.deplacement) == 1:
            if drone.id == nombreDrones:
                tur.forward(largeurSecteur * 10)
        tur.left(90)
        tur.pendown()
        tur.pencolor("black")
        for i in range(zone.latitude2-1):
            drone.longitude = drone.longitude + (-1)
            tur.forward(10)
        tur.penup()
        tur.right(90)


def showfire():
    print(tur.fillcolor())
    tur.fillcolor("red")
    tur.begin_fill()
    tur.right(90)
    tur.forward(3)
    tur.left(90)
    for i in range(4):
        tur.forward(6)
        tur.left(90)
    tur.end_fill()
    tur.pencolor("black")
    tur.left(90)
    tur.forward(3)
    tur.right(90)



# Instanciation et envoi drones
for i in range(1, nombreDrones+1):
    parcourirZone(Drone(i, "Drone"+str(i), 0, 0, 0), Zone(i, "Secteur"+str(i), z1.latitude, z1.longitude + largeurSecteur * (i-1), z1.latitude2, z1.longitude + largeurSecteur * i))

turtle.done()
