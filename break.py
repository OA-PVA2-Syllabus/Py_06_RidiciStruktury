# Nekonečná smyčka je smyčka, která se nikdy neukončí. Pokud je podmínka smyčky vždy True, stává se taková smyčka nekonečnou.
# Nejjednodušší způsob, jak vytvořit nekonečnou smyčku, je použít while True. Klíčové slovo break slouží k opuštění smyčky.

count = 0

while True:  # Tato podmínka nemůže být nepravdivá
    print(count)
    count += 1
    if count >= 5:
        break               # Ukončení smyčky, pokud count >= 5


zoo = ["lion", "tiger", "elephant", "giraffe", "python"]
while True:                 # Tato podmínka nemůže být nepravdivá
    animal = zoo.pop()      # Vyjmutí jednoho prvku z konce seznamu
    print(animal)
    # TODO: Přidání podmínky pro ukončení smyčky
        # Ukončení smyčky

print(zoo)