
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
new_animals = []
i = 0
while i < len(Animals):
    if len(Animals[i]) == 7:
        new_animals.append(Animals[i])
    i += 1
print(new_animals)