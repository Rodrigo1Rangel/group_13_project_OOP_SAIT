class Book:
    """
    A class used to represent a book.

    Parameters
    ----------
    isbn : str
    title : str
    author : str
    genre : int
    available : bool

    Attributes
    ----------
    no public attributes
    """

    GENRE_DICT = {0:"Romance", 1:"Mystery", 2:"Science Fiction", 3: "Thriller", 4:"Young Adult", 5:"Children's Fiction", 6:"Self-help", 7:"Fantasy", 8:"Historical Fiction", 9:"Poetry"}

    # Getters / Accessors

    def __init__(self, isbn, title, author, genre, available):
        """
        Book constructor

        Parameters
        ----------
        isbn : str
        title : str
        author : str
        genre : int
        available : bool
        """
        # initialise instance variables
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = available

    # Getters
    def get_isbn(self):
        """
        Returns the book's isbn for an instance of the Book

        Returns
        -------
        str
        """
        return self.__isbn
    
    def get_title(self):
        """
        Returns the book's title for an instance of the Book

        Returns
        -------
        str
        """
        return self.__title
    
    def get_author(self):
        """
        Returns the book's author for an instance of the Book

        Returns
        -------
        str
        """
        return self.__author
    
    def get_genre(self):
        """
        Returns the book's genre number for an instance of the Book

        Returns
        -------
        int
        """
        return self.__genre
    
    def get_available(self):
        """
        Returns the book's availability for an instance of the Book

        Returns
        -------
        bool
        """
        return self.__available

    def get_genre_name(self):
        """
        Returns the book's genre name for an instance of the Book

        Returns
        -------
        str
        """
        return Book.GENRE_DICT.get(self.__genre, "N/A")

    def get_availability(self):
        """
        Returns the book's availability status for an instance of the Book

        Returns
        -------
        str
        """
        if self.__available == True:
            availability_status = "Available"
        else:
            availability_status = "Borrowed"
        return availability_status

    # Setters / Mutators

    def set_isbn(self, isbn):
        """
        Sets new isbn for a Book instance

        Parameters
        ----------
        isbn : str 
        """
        self.__isbn = isbn

    def set_title(self, title):
        """
        Sets new title for a Book instance

        Parameters
        ----------
        title : str 
        """
        self.__title = title

    def set_author(self, author):
        """
        Sets new author for a Book instance

        Parameters
        ----------
        author : str 
        """
        self.__author = author

    def set_genre(self, genre):
        """
        Sets new genre for a Book instance

        Parameters
        ----------
        genre : int
        """
        self.__genre = genre

    # Other instance methods for Book class

    def borrow_it(self):
        """
        Sets the available hidden attribute to False for a Book instance
        """
        self.__available = False

    def return_it(self):
        """
        Sets the available hidden attribute to True for a Book instance
        """
        self.__available = True
    
    # String format
    def __str__(self):
        """
        Returns a formatted string representation of a Book instance

        Returns
        -------
        str
        """
        return f'{self.__isbn:<15} {self.__title:<25} {self.__author:<25} {Book.GENRE_DICT.get(self.__genre):<20} {self.get_availability():<12}'