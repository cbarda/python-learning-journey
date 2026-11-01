#Η τράπεζα μάς προσφέρει ετήσιο επιτόκιο 0,01%
#Αυτό σημαίνει ότι αν έχουθμε καταθέσει ένα ποσό x,τότε 
#μετά από ένα χρόνο θα μας αυξήσει το ποσό κατά 0.01% (νέο ποσό = x+x*0.01)
#Κατασκευάστε ένα πρόγραμμα python το οποίο:
#Θα αποθηκεύει σε μια μεταβλητή το ποσό της κατάθεσης (π.χ 100)
#θα αποθηκεύει σε μια μεταβλητή το επιτόκιο (π.χ 0.01)
#θα υπολογίζει το ποσό της κατάθεσης μετά από ένα χρόνο

arxiko_poso = 100
epitokio = 0.01
teliko_poso = arxiko_poso + (arxiko_poso * epitokio)
print(teliko_poso)

arxiko_poso = 100
epitokio = 0.01
print(arxiko_poso + (arxiko_poso * epitokio))

poso = 100
epitokio = 0.01
poso = poso + (poso * epitokio)
print(poso)

poso = 100
epitokio = 0.01
poso += poso * epitokio
print(poso)