#Nathan Sullivan
#3/23/17
#Heros inventory

#creat a tuple with some iteams and display with a for loop

inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

print("Your items:")
for item in inventory:
    print(item)

input("\n Press enter key to continue")

#get the length of a tuple
print("you have", len(inventory), "items in your possession.")

input("\n Press enter key to continue")

#test for membership with in

if "healing potion" in inventory:
    print("You will live to fight another day")
    
#display one item trough an index

index = int(input("\n Enter the index number for an item in inventory:  "))
print("At index", index, "is", inventory[index])

#display a slice
start = int(input("\n Enter the index number to begin slice:"))

finish = int(input("\n Enter the index number to end slice:"))

print("inventory[", start, ":", finish, "] is", end= " ")

print(inventory[start:finish])

input("\n Press the enter key to continue.")

#concatenate two tuples
chest = ("gold", "gems")

print("you found a chest. it contains:")

print(chest)

print("you add the contents of the chest to your inventory.")

inventory += chest

print("Your inventory is not:")
print(inventory)

input("\n Press the enter key to continue.")
