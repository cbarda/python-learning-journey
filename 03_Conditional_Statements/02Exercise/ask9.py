#Διορθωστε την ασκηση 10 του μαθηματος 02_Variables ωστε 
# να απεικονιζεται η ωρα πιο κομψα πχ 01:14:23 αντι 1:14:23

hours = int(input("Δώσε τις ώρες: "))
hours_to_print = str(hours)
if hours < 10:
    hours_to_print = "0" + str(hours)
minutes = int(input("Δώσε τα λεπτά: "))
minutes_to_print = str(minutes)
if minutes < 10:
    minutes_to_print = "0" + str(minutes)
seconds = int(input("Δώσε τα δευτερόλεπτα: "))
seconds_to_print = str(seconds)
if seconds < 10:
    seconds_to_print = "0" + str(seconds)
message =  hours_to_print + ":" + minutes_to_print + ":" + seconds_to_print
print("Η ώρα είναι: " + message)