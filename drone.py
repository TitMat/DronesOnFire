class Drone:
    # Classe décrivant un drône"

    def __init__(self, c_id, c_nom, c_latitude, c_longitude, c_aideDeplacement):
        self.id = c_id
        self.nom = c_nom
        self.latitude = c_latitude
        self.longitude = c_longitude
        self.deplacement = c_aideDeplacement

        print("Instanciation du drone: ")
        print(" - Identifiant : " + str(self.id))
        print(" - Nom : " + self.nom)