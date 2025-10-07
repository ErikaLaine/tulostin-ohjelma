tiedosto = input("Anna tulostettavan tiedoston nimi: ")

mustetta_jaljella = input("Onko tulostimessa mustetta? (kyllä/ei): ").strip().lower()

if mustetta_jaljella == "kyllä":
    print(f"Tulostetaan tiedosto: {tiedosto}")
else:
    print("Tulostus epäonnistui: Ei mustetta.")
