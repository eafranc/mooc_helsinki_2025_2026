# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name   = name
        self.author = author
        self.genre  = genre
        self.year   = year

# -----------------------------
# Write your solution here
# -----------------------------
def older_book(book1: Book, book2: Book):
    equal = True
    if book1.year < book2.year:
        equal = False
        older = book1
    elif book2.year < book1.year:
        equal = False
        older = book2

    if equal:
        print(f"{book1.name} and {book2.name} were published in {book1.year}")
    else:
        print(f"{older.name} is older, it was published in {older.year}")

if __name__ == "__main__":
    python  = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma   = Book("Norma", "Sofi Oksanen", "crime", 2015)

    older_book(python, everest) # High Adventure is older, it was published in 1956
    older_book(python, norma) # Fluent Python and Norma were published in 2015
