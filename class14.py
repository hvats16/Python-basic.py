import time
class Library:
    Books ={"000": "DC-PANDEY", "001": "HC-VERMA", "002": "KL ROY"}
    Lenders = {"002" : "vishal"}

    def add(self, ke, value):
        self.Books[ke] = value

    def lend(self, ky, value):
        self.Lenders[ky] = value

    def deposit(self, ke):
        del self.Lenders[ke]

    def is_available(self, ke):
        if ke in self.Lenders:
            return 0
        else:
            return 1

    def display_book(self):
        for key, value in self.Books.items():
            print(key, " ", value)

    def not_available(self):
        for key, value in self.Lenders.items():
            print(key, " ", value)

library = Library()

library.add("003", "ML")
#library.display_book()

while 1:
    print("TOTAL BOOKS")
    library.display_book()
    print("NOT AVAILABLE")
    library.not_available()
    print("PRESS 1 FOR LENDING")
    print("PRESS 2 FOR ADDITION")
    print("PRESS 3 FOR DEPOSITING")
    req = int(input())
    if req == 1:
        key = input("ENTER BOOK_ID")
        if library.is_available(key) == 1:
            name = input("ENTER NAME OF STUDENT")
            library.lend(key, name)
        else:
            print("NOT AVAILABLE TAKEN BY - ", end=" ")
            print(library.Lenders[key])
        time.sleep(5)
    elif req == 2:
        name = input("ENTER NAME OF BOOK")
        key = input("ENTER ID OF BOOK")
        library.add(key, name)
        time.sleep(5)
    else:
        key = input("ENTER ID OF BOOK")
        library.deposit(key)
        time.sleep(5)