# April 22, 2024 - CPRG 216D - Project: Class
# Group Members:
# Ace Nisperos (student ID: 000846849)
# Alex Mohamed (student ID: 000941933)
# Rodrigo Rangel (student: ID 000931691)
# Ryan Howie (student ID: 000279872)

# This program is a librarian management system to track inventory and
# borrowing processes.
# The program has a menu, which by default has customer options, but
# can shift to a librarian staff mode with more options.
# The customers have the option to search, borrow, and return books.
# The librarian staff has the option to search, borrow, return, add,
# remove, and print books.

import book

def main():
    '''Entry point for system
    Sets up book list
    Gets pathname and calls load_books()
    Presents menu with validation
    Calls save_books() before ending the program'''
    pass

def load_books():
    '''Receives empty list and a pathname to csv file
    Parses book list into seperate values
    Creates book objects and adds them to list
    Returns number of books loaded'''
    pass

def print_menu():
    '''Receives and diplays menu heading and menu options
    Gets selection from user until valid selection, which is returned'''
    pass

def search_books():
    '''Receives book list and search string
    Checks for search string in isbn, title, author, and genre,
        adding book to results if found
    Returns search result list'''
    pass

def borrow_book():
    '''Receives book list
    Gets ISBN from user and calls find_book_by_isbn()
    Invokes borrow_it() if ISBN matches an available book
        and an appropriate message if not available'''
    pass

def find_book_by_isbn():
    '''Receives book list and ISBN
    Finds exact match of ISBN in book list or stops at end
    Returns the index of the matching book or -1 if none found'''
    pass

def return_book():
    '''Receives book list
    Gets ISBN from user and calls find_book_by_isbn() with input
    If ISBN matches a borrowed book, calls return_it() or displays
        appropriate message if none found'''
    pass

def add_book(book_list):
    '''Receives book list
    Gets ISBN, title, author, and genre from user, validating genre name
    Creates new instance of book and appends it to the list'''

    '''Arguments:
    book_list: A list of Book class objects'''

    '''Returns:
    Nothing'''

    new_book_isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    new_book_title = input("Enter title: ")
    new_book_author = input("Enter author name: ")
    new_book_genre = input("Enter genre: ")
    while new_book_genre not in book.Book.GENRE_DICT.values():
        print("Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller, Young Adult, Children's Fiction, Self-help, Fantasy, Historical Fiction, Poetry")
        new_book_genre = input("Enter genre: ")
    genre_int_list = list(book.Book.GENRE_DICT.values())
    new_book_genre_int = genre_int_list.index(new_book_genre)
    new_book = book.Book(new_book_isbn, new_book_title, new_book_author, new_book_genre_int, True)
    book_list.append(new_book)
    print(f'"{new_book.get_title()}" with ISBN {new_book.get_isbn()} sucessfully added.')

def remove_book(book_list):
    '''Receives book list
    Gets ISBN from user validating with find_book_by_isbn()
    If book is found, remove it from list. Else display appropriate message'''

    '''Arguments:
        book_list: A list of Book class objects'''

    '''Returns:
        Nothing'''
    
    print("\n" + "CATALOG_DELIMITER * 2" + ' Remove a book ' + "CATALOG_DELIMITER * 2")
    isbn_to_remove = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    isbn_to_remove_index = find_book_by_isbn(book_list, isbn_to_remove)
    if isbn_to_remove_index != -1:
        book_for_remove = book_list.pop(isbn_to_remove_index)
        print(f'"{book_for_remove.get_title()}" with ISBN {book_for_remove.get_isbn()} sucessfully removed.')
    else:
        print("No book found with that ISBN.")

def print_books(book_list):
    '''Receives book list
    Displays book info heading and displays each book object on seperate line'''

    '''Arguments:
        book_list: A list of Book Class objects'''
    
    '''Returns:
        Nothing'''
    
    print(f'{"ISBN":<15} {"Title":<25} {"Author":<25} {"Genre":<20} {"Availability":<12}')
    print("*" * 96)
    for book in book_list:
        print(book)

def save_books():
    '''Receives book list and a pathname to csv
    Creates a comma seperated string from each book object
    Writes each string as a seperate line, and returns number of books'''
    pass