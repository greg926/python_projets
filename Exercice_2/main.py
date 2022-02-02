import random


def demander_nombre(nb_min, nb_max):
    # Devinez un nombre  (entre 1 et 1000000)
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Devinez le nombre (entre {nb_min} et {nb_max}) ? ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez.")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR: Le nombre doit être entre {nb_min} et {nb_max}. Réessayez.")
                nombre_int = 0
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 1000000
NOMBRE_A_DEVINER = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_ESSAIS = 50

"""nombre = 0
essais = NB_ESSAIS
while not nombre == NOMBRE_A_DEVINER and essais > 0:
    print(f"Il vous reste {essais} essais")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_A_DEVINER:
        print("Bravo, vous avez gagné")
    elif nombre > NOMBRE_A_DEVINER:
        print("Le nombre a deviné est plus petit")
        vies -= 1
    else:
        print("Le nombre a deviné est plus grand")
        vies -= 1

if essais == 0:
    print(f"Vous avez perdu! Le nombre a deviné était: {NOMBRE_A_DEVINER}")"""

gagne = False
for i in range(0, NB_ESSAIS):
    essais = NB_ESSAIS-i
    print(f"Il vous reste {essais} essais")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_A_DEVINER:
        print("Bravo, vous avez gagné")
        gagne = True
        break
    elif nombre > NOMBRE_A_DEVINER:
        print("Le nombre a deviné est plus petit")
    else:
        print("Le nombre a deviné est plus grand")

if not gagne:
    print(f"Vous avez perdu! Le nombre a déviné était: {NOMBRE_A_DEVINER}")
