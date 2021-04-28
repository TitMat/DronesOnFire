class Zone:
    # Classe décrivant une zone rectangulaire"
    # Hypothèse: la zone est un rectangle
    # Les premières coordonnées sont celles de l'angle supérieur gauche
    # Les secondes coordonnées sont celles de l'angle inférieur droit

    def __init__(self, c_id, c_nom, c_latitude, c_longitude,c_latitude2, c_longitude2):
        self.id = c_id
        self.nom = c_nom
        self.latitude = c_latitude
        self.longitude = c_longitude
        self.latitude2 = c_latitude2
        self.longitude2 = c_longitude2

        print("Instanciation de la zone: ")
        print(" - Identifiant : " + str(self.id))
        print(" - Nom : " + self.nom)
        print(" - Coordonnes angle supérieur gauche : ")
        print("    - Latitude : " + str(self.latitude) + " Longitude : " + str(self.longitude))
        print(" - Coordonnes angle inférieur droit : ")
        print("    - Latitude : " + str(self.latitude2) + " Longitude : " + str(self.longitude2))