age = int(input("Give your age: "))

if age < 18:
    print("Underage")
elif age >= 18 and age <= 65:
    print("Adult")
else:
    print("retired")