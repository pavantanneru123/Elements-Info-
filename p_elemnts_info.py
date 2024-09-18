import periodictable

element_name=input("Type in the element symbol: ").capitalize()
pavan = getattr(periodictable,element_name, None)

if pavan:
    print("Element name:", pavan.name)
    print("Atomic number:", pavan.number)
    print("Atomic mass:", pavan.mass)
    print("Atomic density:", pavan.density)
else:
    print("Element not found")