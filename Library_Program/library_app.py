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

# Import Modules
import os
import book

# Declare constants
MENU_DELIMITER = "="
CATALOG_DELIMITER = "-"
VALID_MENU_SELECTION = {'0', '1', '2', '3', '2130'}
VALID_LIBRARIAN_MENU_SELECTION = {'0', '1', '2', '3', '4', '5', '6'}

def main():
    '''Entry point for system
    Sets up book list
    Gets pathname and calls load_books()
    Presents menu with validation
    Calls save_books() before ending the program'''

    print("Starting the system ...")
    file_path = input("Enter book catalog filename: ")
    while not os.path.exists(file_path):
        file_path = input("File not found. Re-enter book catalog filename: ")
    book_list = []
    load_books(book_list, file_path)
    menu_selection = print_menu()
    while menu_selection != '0':
        match menu_selection:
            case '1':
                print("\n-- Search for books --")
                search_value = input("Enter search value: ")
                books_found_list = search_books(book_list, search_value)
                if len(books_found_list) == 0:
                    print('No matching books found')
                else:
                    print_books(books_found_list)
                menu_selection = print_menu()
            case '2':
                borrow_book(book_list)
                menu_selection = print_menu()
            case '3':
                return_book(book_list)
                menu_selection = print_menu()
            case '2130':
                menu_selection = print_librarian_menu()
                while menu_selection != '0':
                    match menu_selection:
                        case '1':
                            print("-- Search for books --")
                            search_value = input("Enter search value: ")
                            books_found_list = search_books(book_list, search_value)
                            print_books(books_found_list)
                            menu_selection = print_librarian_menu()
                        case '2':
                            borrow_book(book_list)
                            menu_selection = print_librarian_menu()
                        case '3':
                            return_book(book_list)
                            menu_selection = print_librarian_menu()
                        case '4':
                            add_book(book_list)
                            menu_selection = print_librarian_menu()
                        case '5':
                            remove_book(book_list)
                            menu_selection = print_librarian_menu()
                        case '6':
                            print("\n" + CATALOG_DELIMITER * 2 + ' Print book catalog ' + CATALOG_DELIMITER * 2)
                            print_books(book_list)
                            menu_selection = print_librarian_menu()
    save_books(book_list, file_path)
    print("\n" + CATALOG_DELIMITER * 2 + " Exit the system " + CATALOG_DELIMITER * 2)
    print("Book catalog has been saved.\nGood Bye!")
    
def load_books(list, file_path):
    """
    Description: load_books loads the contents of the books.csv file into an empty list that will contain a list of book
                 objects. It does this by opening the file line by line, splits each line into individual strings, sets the
                 genre string into an integer value and the availability string into a boolean value, then passes all strings
                 from the line into a new book object that gets appended into the list. It closes the file and returns the 
                 number of books loaded from the file.
    
    Arguments:
        - takes list containing list of book objects
        - takes file_path which contains the file location of books.csv
    Return Values: 
        - returns number of books written into books.csv
    """
    number_of_books = 0
    file = open(file_path)

    for line in file:
        line = line.rstrip()
        line_split = line.split(",")

        if (line_split[4] == "True"):
            line_split[4] = True
        else:
            line_split[4] = False

        list.append(Book(line_split[0], line_split[1], line_split[2], int(line_split[3]), line_split[4]))

        number_of_books += 1
    
    file.close()
    return number_of_books

def print_menu():
    '''Receives and diplays menu heading and menu options
    Gets selection from user until valid selection, which is returned'''
    pass

def search_books(book_list, search_value):
    '''Checks for the book objects that contain the user's request substring
    within the isbn, title, author, and genre values of each book object.
    The books that contain the substring within one or more of its attributs
    are added to a list.

    Arguments:
    book_list: a list.
    search_value: a str.

    Returns:
    search_result_list: a list.'''

    search_result_list = []
    for book_obj in book_list:
        book_obj_items = []
        book_obj_items.append(str(book_obj.get_isbn()).lower())
        book_obj_items.append(str(book_obj.get_title()).lower())
        book_obj_items.append(str(book_obj.get_author()).lower())
        book_obj_items.append(str(book_obj.get_genre_name()).lower())

        if '¬'.join(book_obj_items).find(str(search_value).lower()) != -1:
            search_result_list.append(book_obj)
    return search_result_list


def borrow_book(book_list):
    '''Receives the list with the books registered in the library.
    Prompts the user for the ISBN value. The function find_book_by_isbn()
    is called to check for the book existance in the registry system.
    If available, the function borrow_it() is invoked. If not, just an
    informative message is displayed to the user.

    Arguments:
    book_list: a list.

    Returns:
    isbn_reseach_result: a str.'''

    print("\n" + CATALOG_DELIMITER * 2 + ' Borrow a book ' + CATALOG_DELIMITER * 2)
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    isbn_book_research = find_book_by_isbn(book_list, isbn)
    if isbn_book_research != -1:
        if book_list[isbn_book_research].get_available() == False:
            isbn_reseach_result = print(f"'{book_list[isbn_book_research].get_title()}' with ISBN {book_list[isbn_book_research].get_isbn()} is not currently available.")
        if book_list[isbn_book_research].get_available() == True:
            book_list[isbn_book_research].borrow_it()
            isbn_reseach_result =  print(f"'{book_list[isbn_book_research].get_title()}' with ISBN {book_list[isbn_book_research].get_isbn()} successfully borrowed.")
    else:
        isbn_reseach_result = print("No book found with that ISBN.")
    return isbn_reseach_result


def find_book_by_isbn(book_list, isbn):
    '''Receives the list with the books registered in the library, and
    the ISBN that the user is looking for. As iterating through the
    book objects in the list, it checks for a match between the researched
    ISBN value and each book's ISBN attribute. If found a match, the index
    related to the that object position in the argument list is returned.

    Arguments:
    book_list: a list.
    isbn: a str.

    Returns:
    find_result: an int.'''

    indexing_counter = -1
    for book_obj in book_list:
        indexing_counter += 1
        book_obj_isbn = book_obj.get_isbn()
        if book_obj_isbn == isbn:
            find_result = indexing_counter
        else:
            find_result = -1
    return find_result


def return_book(book_list):
    '''Receives the list with the books registered in the library.
    Prompts the user for the ISBN value. The function find_book_by_isbn()
    is called to check for the book existance. If unavailable, the
    return_it() object method is invoked. If not, just an informative
    message is displayed to the user.

    Arguments:
    book_list: a list.

    Returns:
    return_book_result: a str.'''

    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    search_result_index = find_book_by_isbn(book_list, isbn)
    if search_result_index == -1:
        return_book_result = print("No book found with that ISBN.")
    else:
        if book_list[search_result_index].get_available() == False:
            book_list[search_result_index].return_it() # self.__available = True
            return_book_result = print(f'"{book_list[search_result_index].get_title()}" with ISBN {book_list[search_result_index].get_isbn()} sucessfully returned.')
        else:
            return_book_result = print(f'"{book_list[search_result_index].get_title()}" with ISBN {book_list[search_result_index].get_isbn()} is not currently borrowed.')
    return return_book_result


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
    
    print("\n" + CATALOG_DELIMITER * 2 + ' Remove a book ' + CATALOG_DELIMITER * 2)
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
    print(CATALOG_DELIMITER * 96)
    for book in book_list:
        print(book)


def save_books(list, file_path):
    """
    Description: save_books saves changes made to the book list back to the books.csv file. It does this by opening the file and
                 rewriting all lines in the file with a string containing book object information from list with each line containing
                 the information of one book. It then closes the file and returns the number of books written to the file.
    Arguments:
        - takes list containing list of book objects
        - takes file_path which contains the file location of books.csv
    Return Values: 
        - returns number of books written into books.csv
    """
    number_of_books = 0
    file = open(file_path, "w")

    for entry in list:
        avail = entry.get_availability()

        if  (avail == "Available"):
            avail = "True"
        else:
            avail = "False"

        file.write(f"{entry.get_isbn()},{entry.get_title()},{entry.get_author()},{entry.get_genre()},{avail}")
        file.write("\n")
        number_of_books += 1
    
    file.close()
    print("Book catalog has been loaded.")
    return number_of_books
