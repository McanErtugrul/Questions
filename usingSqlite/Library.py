import sqlite3
import time

class Book():

    def __init__(self, title="", author="", publisher="", type="", read=0):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._type = type
        self._read = read

    def __str__(self):  # Change Print func.
        return "Title of Book : {} \n" \
               "Author : {} \n" \
               "Publisher : {} \n" \
               "Type : {} \n" \
               "Read Count : {}" \
            .format(self._title, self._author, self._publisher, self._type, self._read)


class Library():

    def __init__(self):

        self.CreateDb()

    def CreateDb(self):

        self.connection = sqlite3.connect("Library.db")

        self.cursor = self.connection.cursor()

        query = "Create Table If not exists Books (title TEXT,author TEXT,publisher TEXT,type TEXT,readcount INT)"

        self.cursor.execute(query)

        self.connection.commit()
    def ConnectionClose(self):
        self.connection.close()

    def ShowBooks(self):

        query =  "Select * From Books"

        self.cursor.execute(query)

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("Library doesn't have any book..")
        else:
            for i in books:

                book = Book(i[0], i[1], i[2], i[3], i[4])
                print(book)

    def BookInquery(self,title):

        query = "Select * From Books where title = ?"

        self.cursor.execute(query,(title,))

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no book .....")
        else:
            book = Book(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4])

            print(book)
    def AddBook(self, book):

        query = "Insert into Books Values(?,?,?,?,?)"

        self.cursor.execute(query,(book._title, book._author, book._publisher, book._type, book._read))

        self.connection.commit()

    def DeleteBook(self, title):

        query = "Delete From Books where title = ?"

        self.cursor.execute(query, (title,))

        self.connection.commit()

    def AddRead(self, title):

        query = "Select * From Books where title = ?"

        self.cursor.execute(query, (title,))


        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no such book ...")
        else:
            readcount = books[0][4]

            readcount += 1

            query2 = "Update Books set readcount = ? where title = ?"

            self.cursor.execute(query2, (readcount, title))

            self.connection.commit()




