#Δυο εμπειροι παικτες στο ταβλι, αποφασιζουν ποιος θα παιξει πρωτος
#ριχνοντας απο 2 ζαρια ο καθενας. Νικαει αυτος με το μεγαλυτερο αθροισμα.
#κατασκευαστε ενα προγραμα το οποιο θα ποφασιζει ποιος νικησε

paiktis1_zari1 = int(input("Zari 1: "))
paiktis1_zari2 = int(input("Zari 2: "))
paiktis2_zari1 = int(input("Zari 3: "))
paiktis2_zari2 = int(input("Zari 4: "))

paiktis1_athroisma = paiktis1_zari1 + paiktis1_zari2
paiktis2_athroisma = paiktis2_zari1 + paiktis2_zari2

if paiktis1_athroisma > paiktis2_athroisma:
    print("Παικτης 1")
elif paiktis1_athroisma < paiktis2_athroisma:
    print("Παικτης 2")
else:
    print("Isopalia")