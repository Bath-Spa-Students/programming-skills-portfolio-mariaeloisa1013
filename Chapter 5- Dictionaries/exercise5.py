pets = []
animal = {'name':'ramram',
          'animal':'cat',
          'breed':'scottish fold',
          'owner':'maria'}
pets.append(animal)

animal = {'name':'louie',
          'animal':'dog',
          'breed':'german sheperd',
          'owner':'eloisa'}
pets.append(animal)

animal = {'name':'jeep',
          'animal':'turtle',
          'breed':'snapping turtle',
          'owner':'pejero'}
pets.append(animal)

animal = {'name':'goldy',
          'animal':'fish',
          'breed':'goldfish',
          'owner':'butaslac'}
pets.append(animal)

for animal in pets:
    print("everything i know about " + animal['name'].title() + ":")
    for x,y in animal.items():
        print("\t" + x + ": " + y )
    print("\n")
