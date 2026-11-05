x = int(input("Give x: "))
y = int(input("Give y: "))
z = int(input("Give x: "))

if x >= y >= z or x >= z >= y:
    print(x)
if y >= x >= z or y >= z >= x:
    print(y)
if z >= y >= x or z >= x >= y:
    print(z)