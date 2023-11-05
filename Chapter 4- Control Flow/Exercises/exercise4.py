# <2: baby, =2<4: toddler, =4<13: kd, =13<20: teen,
# =20<65: adult, =65<: elder
age = int(input("How old are you? "))


if age < 2 :
    print ("\tYou are a baby")
elif age < 4 :
    print ("\tYou are a toddle")
elif age <13 :
    print ("\tYou are a kid")
elif age <20 :
    print ("\tYou are a teen")
elif age <65 :
    print ("\tYou are an adult")
elif age >65 :
    print ("\tYou are an elder")
else :
    print ("\ttry again")