print("Pozdravljen uporabnik, danes bomo spreminjali kilometre v milje!")

while True:
    print("Navedi stevilo kilometrov za pretrvorbo!")
    kilometer = input("Napisi stevilo: ")
    kilometer = float(kilometer)

    milja = kilometer * 0.6213712

    print(f"{kilometer} kilometrov je {milja} milj.")

    izbira = input("Bi radi ponovno vpisali stevilo kilometrov (da/ne): ")
    if izbira.lower() != "da":
        break
