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
    new_isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    new_title = input("Enter title: ")
    new_author = input("Enter author name: ")
    new_genre = input("Enter genre: ")
    while new_genre not in book.Book.GENRE_DICT.values():
        print("Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller, Young Adult, Children's Fiction, Self-help, Fantasy, Historical Fiction, Poetry")
        new_genre = input("Enter genre: ")
    genre_int_list = list(book.Book.GENRE_DICT.values())
    genre_int = genre_int_list.index(new_genre)
    book_list.append()


def remove_book():
    '''Receives book list
    Gets ISBN from user validating with find_book_by_isbn()
    If book is found, remove it from list. Else display appropriate message'''
    pass

def print_books():
    '''Receives book list
    Displays book info heading and displays each book object on seperate line'''
    pass

def save_books():
    '''Receives book list and a pathname to csv
    Creates a comma seperated string from each book object
    Writes each string as a seperate line, and returns number of books'''
    pass