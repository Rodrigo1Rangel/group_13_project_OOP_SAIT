from book import Book

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
def load_books(list, file_path):
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
def save_books(list, file_path):
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


book_list = []

load_books(book_list, file_path=r"C:\SAIT powerpoints & documents\Final Group Assignment\books.csv")

#for entry in book_list:
#   print(entry)



book_list.append(Book("978-9999999999","example_book","example_author",0,True))

save_books(book_list, file_path=r"C:\SAIT powerpoints & documents\Final Group Assignment\books.csv")

file = open(r"C:\SAIT powerpoints & documents\Final Group Assignment\books.csv", "r")

for line in file:
    line = line.rstrip()
    print(line)


file.close()


book_list.clear()