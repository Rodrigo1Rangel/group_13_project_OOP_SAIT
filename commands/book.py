class Book:

    GENRE_NAMES = {0: "Romance", 1: "Mystery", 2: "Science Fiction", 3: "Thriller", 4: "Young Adult", 5: "Children's Fiction", 6: "Self-help", 7: "Fantasy", 8: "Historical Fiction", 9: "poetry"}

    def __init__(self, isbn, title, author, genre, availability):

        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = availability

    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, isbn):
        self.isbn = isbn
    
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title
    
    def get_author(self):
        return self.author
    
    def set_author(self, author):
        self.author = author

    def get_genre(self):
        return self.genre
    
    def set_genre(self, genre):
        self.genre = genre
    
    def get_availability(self):
        avail = ""

        if (self.availability):
            avail = "Available"
        else:
            avail = "Borrowed"

        return avail
    
    def get_genre_name(self):
        print(self.genre)
        print(Book.GENRE_NAMES.get(self.genre))
        return Book.GENRE_NAMES.get(self.genre)
        
    def borrow_it(self):
        self.availability = False

    def return_it(self):
        self.availability = True

    def __str__(self):
        avail = ""

        if (self.availability):
            avail = "Available"
        else:
            avail = "Borrowed"
            

        return "{:14s} {:25s} {:25s} {:20s} {:s}".format(self.isbn, self.title, self.author, Book.get_genre_name(self), avail)