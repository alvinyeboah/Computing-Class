movie_list = {"Infinity War": 2018,"Endgame": 2021, "Terminator": 1998, "The Matrix" : 2000}

for key, value  in movie_list.items():
    print(f"{key}, {value}")
del movie_list["Infinity War"]
movie_list["Ben 10"] = 2020
print(movie_list)


