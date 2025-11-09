# Summer times program

temp = float(input("Enter temperature in Celsius: "))
act = input("What do you wanna do? swimming, reading, hiking: ").lower()

if temp > 30:
    print("Woah it's hot! Swimming time!")
elif temp >= 20 and temp <= 30:
    print("Nice weather, maybe go hiking?")
else:
    print("Cold outside. Better read a book inside.")

if act == "swimming" and temp > 25:
    print("Yay! Swimming is perfect today!")
elif act == "hiking" and temp >= 20 and temp <= 30:
    print("Hiking is great now!")
elif act == "reading":
    print("Good choice, stay cozy!")
else:
    print("Hmm, not sure that activity works with this weather.")
