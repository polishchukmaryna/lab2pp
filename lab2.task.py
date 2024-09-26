class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.__price = price 

    @staticmethod
    def get_currency():
        return "USD"  

    def get_price(self):
        return self.__price

    def display_info(self):
        return "Book: '" + self.title + "' by " + self.author + ", Price: " + str(self.__price) + " " + Book.get_currency()


class DigitalProduct:
    def __init__(self, file_size):
        self.file_size = file_size

    def download(self):
        print("Downloading file of size " + str(self.file_size) + " MB")


class EBook(Book, DigitalProduct):
    def __init__(self, title, author, price, file_size):
        Book.__init__(self, title, author, price)
        DigitalProduct.__init__(self, file_size)

    def display_info(self):
        return "E-Book: '" + self.title + "' by " + self.author + ", File size: " + str(self.file_size) + " MB, Price: " + str(self.get_price()) + " " + Book.get_currency()


class AudioBook(Book):
    def __init__(self, title, author, price, narrator):
        super().__init__(title, author, price)
        self.narrator = narrator  

    def display_info(self):
        return "AudioBook: '" + self.title + "' by " + self.author + ", Narrated by " + self.narrator + ", Price: " + str(self.get_price()) + " " + Book.get_currency()


class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, book):
        self.items.append(book)
        print("Added '" + book.title + "' to your cart.")

    def remove_from_cart(self, book_title):
        for book in self.items:
            if book.title == book_title:
                self.items.remove(book)
                print("Removed '" + book_title + "' from your cart.")
                return
        print("'" + book_title + "' is not in your cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for book in self.items:
                print(" - " + book.display_info())

    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            total_price = sum([book.get_price() for book in self.items])
            print("Checking out the following books:")
            for book in self.items:
                print(" - " + book.display_info())
            print("Total Price: $" + str(total_price))
            self.items.clear()
            print("Purchase complete. Thank you!")


class BookStore:
    def __init__(self):
        self.books = []
        self.cart = Cart()

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("'" + title + "' has been removed from the store.")
                return
        print("'" + title + "' not found in the store.")

    def display_books(self):
        if not self.books:
            print("No books available in the store.")
        else:
            print("Available books:")
            for book in self.books:
                print(" - " + book.display_info())


def bookstore_menu():
    while True:
        print("\n----- Bookstore Menu -----")
        print("1. Show all books")
        print("2. Add book to cart")
        print("3. Remove book from cart")
        print("4. View cart")
        print("5. Checkout")
        print("0. Exit")
        choice = int(input("Enter your choice (1-5): "))

        match choice:
            case 1:
                store.display_books()
            case 2:
                store.display_books()
                book_title = input("Enter the title of the book to add to cart: ")
                for book in store.books:
                    if book.title == book_title:
                        store.cart.add_to_cart(book)
                        break
                else:
                    print("'" + book_title + "' is not available.")
            case 3:
                store.cart.view_cart()
                book_title = input("Enter the title of the book to remove from cart: ")
                store.cart.remove_from_cart(book_title)
            case 4:
                store.cart.view_cart()
            case 5:
                store.cart.checkout()
            case 0:
                print("See ya, goodbye :)")
                break

store = BookStore()

store.add_book(Book('I See You Are Interested in the Dark', 'Illarion Pavliuk', 14))
store.add_book(EBook("1984", "George Orwell", 10, 5))
store.add_book(AudioBook('Sherlock Holmes', "Arthur Conan Doyle", 20, "Simon Vance"))
store.add_book(Book('Harry Potter', 'J.K. Rowling', 18))

bookstore_menu()










# # Додатковий клас для доставки (логістика)
# class Shippable:
#     def __init__(self, delivery_company):
#         self.delivery_company = delivery_company  # Властивість компанії доставки

#     def ship_book(self, book_title):
#         print("Shipping '" + book_title + "' with " + self.delivery_company + ".")


# # Клас Book з логістикою (множинне наслідування)
# class Book(Shippable):
#     def __init__(self, title, author, price, delivery_company):
#         Shippable.__init__(self, delivery_company)  # Ініціалізація класу Shippable
#         self.title = title
#         self.author = author
#         self.__price = price  # Приватна властивість

    
#     @staticmethod
#     def get_currency():
#         return "USD"  # Статичний метод для валюти

#     def get_price(self):
#         return self.__price

#     def display_info(self):
#         return "Book: '" + self.title + "' by " + self.author + ", Price: " + str(self.__price) + " " + Book.get_currency()

#     def ship(self):
#         self.ship_book(self.title)  # Виклик методу доставки з класу Shippable
# # Новий клас для цифрових продуктів
# class DigitalProduct:
#     def __init__(self, file_size):
#         self.file_size = file_size

#     def download(self):
#         print("Downloading file of size" + self.file_size+ "MB")

# # Множинне наслідування: EBook наслідує як від Book, так і від DigitalProduct
# class EBook(Book, DigitalProduct):
#     def __init__(self, title, author, price, file_size, delivery_company):
#         Book.__init__(self, title, author, price, delivery_company)
#         DigitalProduct.__init__(self, file_size)

#     def display_info(self):
#         return "E-Book: '" + self.title + "' by " + self.author + ", File size: " + str(self.file_size) + "MB, Price: " + str(self.get_price()) + " " + Book.get_currency()

# # Клас AudioBook без логістики (звичайне наслідування)
# class AudioBook(Book):
#     def __init__(self, title, author, price, narrator, delivery_company):
#         super().__init__(title, author, price, delivery_company)
#         self.narrator = narrator  # Додаткова властивість

#     def display_info(self):
#         return "AudioBook: '" + self.title + "' by " + self.author + ", Narrated by " + self.narrator + ", Price: " + str(self.get_price()) + " " + Book.get_currency()


# # Клас Cart для керування кошиком
# class Cart:
#     def __init__(self):
#         self.items = []
#         self.delivery_method = None

#     def add_to_cart(self, book):
#         self.items.append(book)
#         print("Added '" + book.title + "' to your cart.")

#     def remove_from_cart(self, book_title):
#         for book in self.items:
#             if book.title == book_title:
#                 self.items.remove(book)
#                 print("Removed '" + book_title + "' from your cart.")
#                 return
#         print("'" + book_title + "' is not in your cart.")

#     def view_cart(self):
#         if not self.items:
#             print("Your cart is empty.")
#         else:
#             print("Items in your cart:")
#             for book in self.items:
#                 print(" - " + book.display_info())

#     def set_delivery_method(self):
#         print("Choose delivery method:")
#         print("1. Standard Delivery (5 USD)")
#         print("2. Express Delivery (10 USD)")
#         choice = int(input("Enter choice (1 or 2): "))
#         if choice == 1:
#             self.delivery_method = ("Standard Delivery", 5)
#         elif choice == 2:
#             self.delivery_method = ("Express Delivery", 10)
#         else:
#             print("Invalid choice, setting default delivery method: Standard Delivery")
#             self.delivery_method = ("Standard Delivery", 5)

#     def checkout(self):
#         if not self.items:
#             print("Your cart is empty.")
#         else:
#             if not self.delivery_method:
#                 self.set_delivery_method()

#             total_price = sum([book.get_price() for book in self.items]) + self.delivery_method[1]
#             print("Checking out the following books:")
#             for book in self.items:
#                 print(" - " + book.display_info())
#             print("Delivery method: " + self.delivery_method[0])
#             print("Total Price: $" + str(total_price))
#             self.items.clear()
#             print("Purchase complete. Thank you!")


# # Клас User для користувачів
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.cart = Cart()


# # Клас BookStore для керування книгарнею
# class BookStore:
#     def __init__(self):
#         self.books = []
#         self.users = {}

#     def add_book(self, book):
#         self.books.append(book)

#     def remove_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 self.books.remove(book)
#                 print("'" + title + "' has been removed from the store.")
#                 return
#         print("'" + title + "' not found in the store.")

#     def display_books(self):
#         if not self.books:
#             print("No books available in the store.")
#         else:
#             print("Available books:")
#             for book in self.books:
#                 print(" - " + book.display_info())

#     def register_user(self, name):
#         if name in self.users:
#             print("User " + name + " already exists.")
#         else:
#             self.users[name] = User(name)
#             print("User " + name + " has been registered.")

#     def select_user(self, name):
#         if name in self.users:
#             return self.users[name]
#         else:
#             print("User " + name + " not found.")
#             return None


# def bookstore_menu():
#     while True:
#         print("\n----- Bookstore Menu -----")
#         print("1. Register new user")
#         print("2. Select user")
#         print("3. Show all books")
#         print("4. Add book to cart")
#         print("5. Remove book from cart")
#         print("6. View cart")
#         print("7. Checkout")
#         print("0. Exit")
#         choice = int(input("Enter your choice (1-7): "))

#         match choice:
#             case 1:
#                 name = input("Enter new user name: ")
#                 store.register_user(name)
#             case 2:
#                 name = input("Enter user name: ")
#                 global user
#                 user = store.select_user(name)
#             case 3:
#                 store.display_books()
#             case 4:
#                 if user:
#                     store.display_books()
#                     book_title = input("Enter the title of the book to add to cart: ")
#                     for book in store.books:
#                         if book.title == book_title:
#                             user.cart.add_to_cart(book)
#                             break
#                     else:
#                         print("'" + book_title + "' is not available.")
#                 else:
#                     print("No user selected. Please select a user first.")
#             case 5:
#                 if user:
#                     user.cart.view_cart()
#                     book_title = input("Enter the title of the book to remove from cart: ")
#                     user.cart.remove_from_cart(book_title)
#                 else:
#                     print("No user selected. Please select a user first.")
#             case 6:
#                 if user:
#                     user.cart.view_cart()
#                 else:
#                     print("No user selected. Please select a user first.")
#             case 7:
#                 if user:
#                     user.cart.checkout()
#                 else:
#                     print("No user selected. Please select a user first.")
#             case 0:
#                 print("See ya, goodbye :)")
#                 break


# store = BookStore()
# user = None  

# store.add_book(Book('I See You Are Interested in the Dark', 'Illarion Pavliuk', 14, "DHL"))
# store.add_book(EBook("1984", "George Orwell", 10, 5, "No Delivery"))
# store.add_book(AudioBook('Sherlock Holmes', "Arthur Conan Doyle", 20, "Simon Vance", "UPS"))
# store.add_book(Book('Harry Potter', 'J.K. Rowling', 18, "FedEx"))

# bookstore_menu()