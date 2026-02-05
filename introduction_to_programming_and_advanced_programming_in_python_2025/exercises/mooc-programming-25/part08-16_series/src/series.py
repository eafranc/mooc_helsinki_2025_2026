# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title       = title
        self.seasons     = seasons
        self.genres      = genres
        self.ratings_num = 0
        self.ratings_lst = []
        self.ratings_avg = 0

    def __str__(self):
        lines     = [0] * 3
        lines[0]  = f"{self.title} ({self.seasons} seasons)"
        lines[1]  = "genres: " + ", ".join(self.genres)
        if self.ratings_avg == 0:
            lines[2] = "no ratings"
        else:
            lines[2] = f"{self.ratings_num} ratings, average {self.ratings_avg: .1f} points"
        return "\n".join(lines)

    def rate(self, rating: int):
        self.ratings_num += 1
        self.ratings_lst.append(rating)
        self.ratings_avg = sum(self.ratings_lst) / self.ratings_num

def minimum_grade(rating: float, series_list: list[Series]):
    graded_series = []
    for series in series_list:
        if series.ratings_avg >= rating:
            graded_series.append(series)
    return graded_series

def includes_genre(genre: str, series_list: list[Series]):
    genre_specified_series = []
    for series in series_list:
        if genre in series.genres:
            genre_specified_series.append(series)
    return genre_specified_series

if __name__ == "__main__":
# PART 1
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    print(dexter)

# Dexter (8 seasons)
# genres: Crime, Drama, Mystery, Thriller
# no ratings

# PART 2
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)
# Dexter (8 seasons)
# genres: Crime, Drama, Mystery, Thriller
# 5 ratings, average 3.4 points

# PART 3
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)
# a minimum rating of 4.5:
# Dexter
    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
# genre Comedy:
# South Park
# Friends
