#Γραψτε ενα προγραμμα το οποιο θα δεχεται απο την εισοδο δυο ακεραιους
#και επειτα θα ελεγχει αν ισχυει καποιος σχεσιακος τελεστης των δυο αριθμων.
#Πχ για το ισον if x == y: print(str(x) + " equals to " + str(y))
#Το προγραμμα να ενσωμ,ατωνει τους ==, !=, <, >, <=, >=

x = int(input("Δώσε τον πρώτο ακέραιο: "))
y = int(input("Δώσε τον δεύτερο ακέραιο: "))
if x == y:
    print(str(x) + " equals to " + str(y))
if x != y:
    print(str(x) + " not equals to " + str(y))
if x > y:
    print(str(x) + " greater than " + str(y))
if x >= y:
    print(str(x) + " greater or equals to " + str(y))
if x < y:
    print(str(x) + " less than " + str(y))
if x <= y:
    print(str(x) + " less or equals to " + str(y))