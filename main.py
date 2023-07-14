# welcoming statement

print("==========================")
print(" Welcome to the UMBC Car Customization Form! ")
print("==========================")

print()
print()

# customer's name
name = input(" Name: ")
name = name.capitalize()

# Make and Model Choice
print(" please enter the letter of the selection you are looking for ~ Make & Model~ ")

print()

print(" 1. what model of the car  are you ordering?")
print("a. lightning speedster")
print("b. Eco leaf")
print("c. Harp Chord")
print("d. Chevron Jolt")

print()
model_make = input(" please enter 'a'- 'd': ")

print()
print()

# asking for an upgrade ~ 4 door to 2 door~
print(" 2. would you like to upgrade from the 4-door optioon to the 2-door option?")
doors = input(" please enter 'yes' or 'no': ")


print()
print()

# exterior statement
print("~ exterior ~")
print(" 3. what color would you like your car to be? ")

excolor = input(" you may enter the name of any color you'd like: ")

print()
print()

# preferred weather package
print("4. would you like the deluxe weather package?")

pack = input(" please enter 'yes' or 'no': ")

print()
print()

# interior statement
print("~ interior ~")
print(" 5. which engine would you like your car to have?")

print(" I-4 entry engine")
print("b. V-6 performance engine")
print("c. Eco Diesel Engine")
print("d. Chevron Jolt")

print()
interior = input(" please enter 'a'- 'c': ")

print()
print()

# heated seats 
print(" 6. would you like heated seats?")
heated = input(" please enter 'yes' or 'no': ")

print()
print()
print("==========================")

#summary
print("~ summary ~")
print(model_make)
print(doors)
print(excolor)
print(pack)
print(interior)
print(heated)

print()
print("==========================")

# thank you!!
print()
print(f" Thank you, {name}! your order is received")