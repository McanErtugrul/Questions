from Library import *

print("""***********************************
Welcome to the Library CMD Program.
Operations:
1. Show Books
2. Show One Books
3. Add Books
4. Delete Books
5. Increase the number of Books
Press 'e' to exit.
***********************************""")

library = Library()

while True:
    operation = input("Your operation : ")

    if (operation == "e"):
        print("Program Ending.....")
        break

    elif (operation == "1"):
        library.ShowBooks()

    elif (operation == "2"):
        title = input("Which book do you want ? ")
        print("Questioning the Book ...")
        time.sleep(2)

        library.BookInquery(title)

    elif (operation == "3"):
        title = input("Title :")
        author = input("Author :")
        publisher = input("Publisher :")
        type = input("Type :")
        readcount = int(input("ReadCount :"))

        newBook = Book(title, author, publisher, type, readcount)

        print("Adding book ....")
        time.sleep(2)

        library.AddBook(newBook)
        print("Book Added ....")


    elif (operation == "4"):
        title = input("Which book do you want to delete ?")

        result = input("Are you sure ? (Y/N)")
        if (result == "Y"):
            print("Deleting Book ...")
            time.sleep(2)
            library.DeleteBook(title)
            print("The book has been deleted ....")


    elif (operation == "5"):
        title = input("Which book would you like to increase the number of reads ?")

        library.AddRead(title)
        print("Book reading count increased")

    else:
        print("Invalid Transaction ...")



