import book


book_list = "978-0060000000,To Kill a Mockingbird,Harper Lee,3,True"

def main():
    add_book(book_list)


def add_book(book_list):
    '''Receives book list
    Gets ISBN, title, author, and genre from user, validating genre name
    Creates new instance of book and appends it to the list'''
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

if __name__ == "__main__":
    main()