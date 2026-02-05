# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    
    movie = {"name"    : name, 
             "director": director,
             "year"    : year,
             "runtime" : runtime}

    database.append(movie)

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database) 
# [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, 
#  {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]

