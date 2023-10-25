Money = float(input("Enter amount: "))
extra = 0
if Money  > 170 :
    extra = 100
else:
    extra = 0
print("Your Extra : " + str(extra ))

# nested desicion structure
dogs = int(input("How many dogs do u have: "))
cats = int(input("How many cats do you have: "))

if dogs > cats:
    if cats == dogs:
        print("You love both cats and dogs equally")
    else: print ("You are a cat person")
else: print ("You are a dog person")z