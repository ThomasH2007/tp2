import random

def jeu_devinette():
    borne_max = int(input("Quel sera la borne max"))
    borne_min = int(input("Quel sera la borne minimum"))

    nombre_rand = random.randint(borne_min, borne_max)
    essai = int(input("Quel numero pensé vous que j'ai choisi"))
    nombre_essai = 0
    while essai != nombre_rand:
        nombre_essai += 1
        if essai < nombre_rand:
            essai = int(input("le numéro que j'ai choisi est plus élévé"))

        elif essai > nombre_rand:
            essai = int(input("le numéro que j'ai choisi est plus petit"))
    while essai == nombre_rand:
        print (" Bravo tu a deveni le numero que j'avais chois en " + str(nombre_essai) = "essai")
        recommencer = stre(input("Voulez vous recommencer"))
        if recommencer == "oui":
            jeu_devinette()
        if recommencer == "non":
            exit()
jeu_devinette()