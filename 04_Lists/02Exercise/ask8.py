my_movies = ["Movie3","Movie2","Movie4","Movie1"]

movie = input("Which is your fav movie? ")
if movie in my_movies:
   print("Not saved")
else:
    my_movies.sort()
    print(my_movies)
    print(len(my_movies))