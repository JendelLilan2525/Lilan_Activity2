# PART 1: ENVIRONMENT SETUP
class Greeter:

    def greet(self):
        print("Hello! welcome to OOP.")


# Create object
person = Greeter()

# Call method
person.greet()

#PART 2: CLASSES AND OBJECTS

#PART 3: ADDING METHODS
class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.total_km = 0

    def drive(self, km):
        self.total_km += km
        print(self.brand, self.model, "Drove", km, "km.")

    def age(self, current_year):
        return current_year - self.year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self):
        return f"Car('{self.brand}','{self.model}',{self.year})"



#Create car objects
car1 = Car("Toyota", "Vios", 2022)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("Tesla", "Roadster", 2026)

#Display car information
print("\n--- Car 1 ---")
print(car1.brand)
print(car1.model)
print(car1.year)

print("\n--- Car 2 ---")
print(car2.brand)
print(car2.model)
print(car2.year)

print("\n--- Car 3 ---")
print(car3.brand)
print(car3.model)
print(car3.year)
print("Wheels:", car3.wheels)

# Test drive method
car1.drive(50)
car2.drive(100)
car3.drive(30)

print("\n--- Car Kilometers ---")
print("Toyota total distance:", car1.total_km, "km")
print("Honda total distance:", car2.total_km, "km")
print("Tesla total distance:", car3.total_km, "km")

print("\n--- Car Ages ---")
print("Toyota age:",car1.age(2026), "years")
print("Honda age:", car2.age(2026), "years")
print("Tesla age:", car3.age(2026), "years")

#Test __str__ method
print("\n--- Car Information ---")
print(car1)
print(car2)
print(car3)

#Test __repr__ method
print("\n--- Car Representation ---")
print(repr(car1))
print(repr(car2))
print(repr(car3))

#PART 4: LIBRARY BOOK SYSTEM
class Book:
    book_count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        Book.book_count += 1

    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is already borrowed.")

    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not borrowed.")

    def display_info(self):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"

        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", status)

      
                        
#Create book objects
book1 = Book("Atomic Habits","James Clear")
book2 = Book("The Art of Seduction","Robert Greene")
book3 = Book("The 48 Laws of Power","Robert Greene")

#Test Borrowing books
print("\n--- Borrowing Books ---")
book1.borrow()
book2.borrow()
book3.borrow()

#Test borrowing the same book twice
print("\n--- Borrowing the Same Book Twice ---")
book2.borrow()

#Test returning books
print("\n--- Returning Books ---")
book2.return_book()

#Test book information
print("\n--- Book Information ---")
book1.display_info()
print()
book2.display_info()
print()
book3.display_info()

#Display total number of books
print("\n--- Library Book Count ---")
print("Total books:", Book.book_count)