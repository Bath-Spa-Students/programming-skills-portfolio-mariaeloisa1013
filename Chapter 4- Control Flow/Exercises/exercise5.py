#favfruits: mango, pineapple, caimito, avodaco, watermelon
fruits = ["avocado", "pineapple","mango", "caimito", "watermelon"]

fruit = str(input("name a fruit: "))
favorite_fruits = ["avocado", "mango", "caimito"]

if fruit == favorite_fruits[0]:
    print ("\tYou must love " + favorite_fruits[0]+ "! me too!")
if fruit == favorite_fruits[1]:
    print ("\tYou must love " + favorite_fruits[1]+ "! me too!")
if fruit == favorite_fruits[2]:
    print ("\tYou must love " + favorite_fruits[2] + "! me too!")
if fruit == fruits[1]:
    print ("\tme too. but it's not my top 3 list")
if fruit == " " :
    print ("\ttry again")
