species = "Dog"
age = 4

if species == "Dog":
    if age < 2:
        print("Puppy food for your Dog")
    else:
        print("Adult dog food")

elif species == "Cat":
    if age > 5:
        print("Senior cat food for your Cat")
    else:
        print("Adult cat food")

else:
    print("Unknown pet species")