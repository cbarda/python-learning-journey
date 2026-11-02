#Γραψτε ενα προγραμμα το οποιο θα δεχεται απο την εισοδο την ηλικια του χρηστη
#και θα τυπωνει μηνυμα για το αν ειναι ανηλικος, ενηλικος ή συνταξιουχος(>65)

age = int(input("Give your age: "))

if age < 18:
    print("Underage")
elif age >= 18 and age <= 65:
    print("Adult")
else:
    print("retired")