ya = int(input("How old are you? "))
if ya>=18:
    print("You can vote!")
else: 
    print("You can't vote!")
fam = int(input("How many family members do you have? "))
if fam<=2:
    print("You should get the single pack.")
elif fam==3:
    print("You should get the double pack.")
elif fam==4 or fam==5:
    print("You should get the family pack.") 
elif fam>=6:
    print("You can get any combination of packs.")