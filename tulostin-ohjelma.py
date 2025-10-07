teksti = input("Mitä haluat tulostaa? ")

try:
    maara = int(input("Kuinka monta kertaa? "))
    for i in range(maara):
        print(teksti)
except ValueError:
    print("Virhe: kirjoita numerona toistojen määrä.")
