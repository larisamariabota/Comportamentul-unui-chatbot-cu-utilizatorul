import random
import math

# Parametri
p_intelegere = float(input("Introduceți probabilitatea de înțelegere (0-1): "))
rata_timp = float(input("Introduceți rata pentru timpul de răspuns (ex. 1.5): "))
media_satisfactie = float(input("Introduceți media satisfacției (ex. 7.5): "))
dev_satisfactie = float(input("Introduceți deviația standard a satisfacției (ex. 1.2): "))

# definire distributii
def uniform():
    u = 0.0
    while u == 0.0:
        u = random.random()
    return u

def geometrica(p_intelege):
    u = uniform()
    return math.ceil(math.log(1 - u) / math.log(1 - p))


def binomiala(n, p_intelegere):
    succese = 0
    for _ in range(n):
        if random.random() < p:
            succese += 1
    return succese

def exponential(lmbda):
    u = uniform()
    return -math.log(u) / lmbda

def normal(media, dev):
    u1 = uniform()
    u2 = uniform()
    z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    return media + dev * z0

def simuleaza_conversatie():
    intrebari = []
    print("Scrie întrebările tale (scrie 'gata' când ai terminat):")
    while True:
        q = input("Întrebare, (gata=stop): ")
        if q.lower() == "gata":
            break
        if q.strip() == "":
            print("Te rog introdu o întrebare validă.")
            continue
        intrebari.append(q)

    if len(intrebari) == 0:
        print("Nu ai introdus nicio întrebare.")
        return

    raspunsuri = []
    timpi = []
    nr_corecte = 0

    for idx, intrebare in enumerate(intrebari):
        corect = 1 if random.random() < p_intelegere else 0
        timp = exponential(rata_timp)
        timpi.append(round(timp, 2))

        if corect:
            raspuns = f"AI răspunde corect la întrebarea {idx+1}: {intrebare}"
            nr_corecte += 1
        else:
            raspuns = f"AI nu înțelege întrebarea {idx+1}: {intrebare} și cere clarificare"

        raspunsuri.append(raspuns)

    # Simulare satisfactie utilizator
    satisfactie = normal(media_satisfactie, dev_satisfactie)
    satisfactie = max(0, min(10, satisfactie))  # limitez între 0 și 10

    print("\nRezultatele simulării:\n")
    for i, rasp in enumerate(raspunsuri):
        print(f"{i+1}. {rasp} (timp răspuns: {timpi[i]} secunde)")
    print(f"\nNumăr întrebări corecte: {nr_corecte} din {len(intrebari)}")
    print(f"Nivel satisfacție utilizator: {satisfactie:.2f} / 10")

# Rulează simularea
simuleaza_conversatie()
