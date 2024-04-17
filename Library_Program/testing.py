import book


book_list = "978-0060000000,To Kill a Mockingbird,Harper Lee,3,True"

def main():
    add_book(book_list)


def add_book(book_list):
    '''Receives book list
    Gets ISBN, title, author, and genre from user, validating genre name
    Creates new instance of book and appends it to the list'''
    # new_isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    # new_title = input("Enter title: ")
    # new_author = input("Enter author name: ")
    new_genre = input("Enter genre: ")
    # if book.Book.get_genre_name
    # print(book.Book.GENRE_DICT.keys())
    if new_genre in book.Book.GENRE_DICT.values():
        genre_int_list = list(book.Book.GENRE_DICT.values())
        genre_int = genre_int_list.index(new_genre)
        print(genre_int)
"C:\Users\howie\Documents\GitHub\group_13_project_OOP_SAIT\commands"

if __name__ == "__main__":
    main()