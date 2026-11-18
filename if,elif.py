bilet = input("Jaki masz bilet: ")

if bilet == "Boss":
    print("Wejscie Boss")
elif bilet == "Vip":
    print("Wejscie Vip")
elif bilet == "Normalny":
    print("Wejscie normalne")
else:
    print("Nie wchodzisz")
if bilet == "Boss":
    print ("Siedzisz w pierszym rzedzie")
elif bilet == "Vip":
    print ("Siedzisz w 2 rzędzie")
elif bilet == "Normalny":
    print ("stoisz cwelu")


print("Po koncercie wlasciciele mowia ze osoby z biletami Boss moga wejsc na backstage")
print("Ochrona sie pyta")
bilet = input("Jaki masz bilet?")

if bilet == "Boss":
    print("Masz dostep do backstage")
    print("Ochrona cie wpuszcza")
else: 
    print("Nie masz dostepu do backstage ochrona cie wyprasza")