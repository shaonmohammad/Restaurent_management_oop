class Reader:
    def __init__(self,name,author) -> None:
        self.name = name
        self.author = author

class Library:
    all_book = {}
    def __init__(self,name) -> None:
        self.name = name

    def add_book(self,name,author):
        reader = Reader(name,author)
        self.all_book[reader.name] = reader.author
    def show_all_book(self):
        print('---------------ALL BOOk-------------')
        for key,value in self.all_book.items():
           print(f'Name is:{key} and author is {value}')

library = Library('School Libraay')

library.add_book('Phisics','linko')
library.add_book('C++','jankar')

library.show_all_book()


