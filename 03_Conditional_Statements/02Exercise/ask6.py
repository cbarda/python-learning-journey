#Διορθωστε το προγραμμα της ασκησης 5 ωστε να χειριζεται αποδοτικα την 
#περιπτωση που ο χρηστης εισαγει αριθμους που ειναι ισοι μεταξυ τους

x = int(input("Give x: "))
maximum = x
y = int(input("Give y: "))
if y > maximum:
    maximum = y
z = int(input("Give x: "))
if x > maximum:
    maximum = z
print(z)