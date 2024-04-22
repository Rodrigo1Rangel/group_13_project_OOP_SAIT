class Book:


    """
    Description: genre_names stores 10 different genres with key values 0-9
    """
    genre_names = {0: "Romance", 1: "Mystery", 2: "Science Fiction", 3: "Thriller", 4: "Young Adult", 5: "Children's Fiction", 6: "Self-help", 7: "Fantasy", 8: "Historical Fiction", 9: "poetry"}


    """
    Description: __init__ constructor initializes the book object's isbn value, title, author, genre, and availability.
    Arguments:
        - takes self 
        - takes an arugment for the new title
    Return Values: N/A
    """
    def __init__(self, isbn, title, author, genre, availability):

        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__availability = availability


    """
    Description: get_isbn returns book object's self.__isbn
    Arguments:
        - takes self 
    Return Values: N/A
    """
    def get_isbn(self):
        return self.__isbn
    

    """
    Description: set_isbn sets self.__isbn to equal the arguement isbn 
    Arguments:
        - takes self 
        - takes an arugment for the new isbn
    Return Values: N/A
    """
    def set_isbn(self, isbn):
        self.__isbn = isbn
    

    """
    Description: get_title returns book object's self.__title
    Arguments:
        - takes self 
    Return Values: 
        - returns self.__title 
    """
    def get_title(self):
        return self.__title
    

    """
    Description: set_title sets self.__title to equal the arguement title
    Arguments:
        - takes self 
        - takes an arugment for the new title
    Return Values: N/A
    """
    def set_title(self, title):
        self.__title = title
    

    """
    Description: get_author returns book object's self.__author
    Arguments:
        - takes self 
    Return Values: 
        - returns self.__author
    """
    def get_author(self):
        return self.__author
    

    """
    Description: set_author sets self.__genre to equal the argument author
    Arguments:
        - takes self 
        - takes an argument for the new author
    Return Values: N/A
    """
    def set_author(self, author):
        self.__author = author


    """
    Description: get_genre returns book object's self.__genre 
    Arguments:
        - takes self 
    Return Values:
        - returns self.__genre
    """
    def get_genre(self):
        return self.__genre
    

    """
    Description: set_genre sets self.__genre to equal the argument genre
    Arguments:
        - takes self 
        - takes an argument for the new genre
    Return Values: N/A
    """
    def set_genre(self, genre):
        self.__genre = genre
    

    """
    Description: get_availability returns the string "Available" if self.__availability is true and "Borrowed" if it is false
    Arguments:
        - takes self 
    Return Values:
        - returns avail which either stores "available" or "Borrowed"
    """    
    def get_availability(self):
        avail = ""

        if self.__availability:
            avail = "Available"
        else:
            avail = "Borrowed"

        return avail
    

    """
    Description: get_genre_name returns the key value of the integer stored in self.__genre. Returns Error if no key is found.
    Arguments:
        - takes self 
    Return Values:
        - returns the genre represented by the key in the dictionary genre_names
    """
    def get_genre_name(self):
        return Book.genre_names.get(self.__genre, "Error")
        

    """
    Description: borrow_it changes the availability of the book object to True
    Arguments:
        - takes self 
    Return Values: N/A
    """
    def borrow_it(self):
        self.__availability = False


    """
    Description: return_it changes the availability of the book object to False
    Arguments:
        - takes self 
    Return Values: N/A
    """
    def return_it(self):
        self.__availability = True


    """
    Description: __str__ prints information about the book object
    Arguments:
        - takes self 
    Return Values:
        - returns a formatted string of the books isbn value, title, author, genre, and its availability
    """
    def __str__(self):
        return "{:14s} {:25s} {:25s} {:20s} {:s}".format(self.__isbn, self.__title, self.__author, self.get_genre_name(), Book.get_availability(self))
    
    #list brief description.
    #list arguments with variable name followed by data type.
    #list return values variable followed by data type.

    """
    Test
    """