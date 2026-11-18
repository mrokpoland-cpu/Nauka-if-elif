bilet = input("Jaki masz bilet: ")

if bilet == "Vip+":
    print("Wejscie Vip+")
elif bilet == "Vip":
    print("Wejscie Vip")
elif bilet == "Normalny":
    print("Wejscie normalne")
else:
    print("Nie wchodzisz")
if bilet == "Vip+":
    print ("Siedzisz w pierszym rzedzie")
elif bilet == "Vip":
    print ("Siedzisz w 2 rzędzie")
elif bilet == "Normalny":
    print ("Stoisz")


print("Po koncercie wlasciciele mowia ze osoby z biletami Vip+ moga wejsc na backstage")
print("Ochrona sie pyta")
bilet = input("Jaki masz bilet?")

if bilet == "Vip+":
    print("Masz dostep na backstage")
    print("Ochrona cie wpuszcza")
else: 
    print("Nie masz dostepu na backstage ochrona cie wyprasza")