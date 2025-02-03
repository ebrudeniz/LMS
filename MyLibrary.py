class Library:

    def __init__(self):
        self.books_file_path = "books.txt"
        self.students_file_path = "students.txt"
        self.checkouts_file_path = "checkouts.txt"
        self.checkouts = []
        self.books = []
        self.students = []
        self.load_data()

    def load_data(self):
        self.books = self.read_files(self.books_file_path)
        self.students = self.read_files(self.students_file_path)
        self.checkouts = self.read_files(self.checkouts_file_path)

    def read_files(self,file_path):
        data =[]
        with open(file_path,"r") as file:
            for line in file:
                data.append(list(line.strip().split(',')))
        return data
    
    def write_files(self,file_path,data):
        with open(file_path , "w") as file:
            for item in data:
                file.write(','.join(item) + '\n')
    
    def update_checkouts(self,student_id,isbn):
        self.checkouts.append((student_id,isbn))
        self.write_files(self.checkouts_file_path,self.checkouts)

    def list_student_checkouts(self):
        for student in self.students:
            student_id = student[0]
            student_checkouts = [checkout[1] for checkout in self.checkouts if checkout[0] == student_id]
            if student_checkouts:
                print(f"student {student_id} has checked out books with isbn: {', '.join(student_checkouts)}")
            else:
                print(f"student {student_id} has not checked out any books." )

    def list_all_books(self):
        for book in self.books:
            print(book[0],":", book[1],"by" , book[2],book[3])

    def list_checked_out_books(self):
        for book in self.books:
            if book[3] == "T":
                print(book[0],":",book[1],"by",book[2],book[3],"(Checked Out)")

    def add_new_book(self):
        isbn = input("Enter ISBN number: ")
        name = input("Enter book name: ").title()
        author = input("Enter author name: ").title()
        checked = "F"
        self.books.append((isbn, name, author, checked))
        print("Book added:", name ,"by" , author)
        
    def delete_book(self):
        isbn = input("Enter ISBN number of the book to delete:")
        for book in self.books:
            if book[0] == isbn:
                if book[3] == "T" :
                    print("Warning: Book is checked out. Cannot delete.")
                else:
                    self.books.remove(book)
                    print("Book with ISBN" ,isbn, "deleted.")
                    return
        print("Book not found!")

    def search_by_isbn(self):
        isbn = input("Enter ISBN to search:")
        for book in self.books:
            if book[0] == isbn:
                print(book[0],":",book[1],"by",book[2])
                return
        print("Books with ISBN",isbn,"not found.")

    def search_by_name(self):
        name = input("Enter name to search: ")
        found_books = []

        for book in self.books:
            if name.title() in book[1].title():
                found_books.append((book[0], book[1], book[2]))

        if found_books:
            for found_book in found_books:
                print(found_book[0], ":", found_book[1], "by", found_book[2])
        else:
            print("No books found with name", name)


    def check_out_books(self):
        student_id = input("Enter student ID: ")
        isbn = input("Enter ISBN number of the book to check out: ")

        for student in self.students:
            if student[0] == student_id:
                for book in self.books:
                    if book[0] == isbn:
                        if book[3] == 'F':
                            book[3] = 'T'
                            self.update_checkouts(student_id,isbn)
                            print("Book", book[1], "checked out to student", student_id, ".")
                            return 
                        else:
                            print("Book is already checked out. Cannot check out again.")
                            return 
                else:
                    print("Book with ISBN", isbn, "not found.")
                    return
        else:
            print("Student with id", student_id, "not found.")
            return
        
    def add_new_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter student name: ").capitalize()
        surname = input("Enter student surname: ").capitalize()
        self.students.append((student_id, name, surname))
        print("Student added:",student_id, name, surname)
                        
    def list_all_students(self):
        for student in self.students:
            print(student[0],":",student[1],student[2])
        self.list_student_checkouts()
     
    def main_menu(self):
        while True:
            print(" Welcome To Library Management System Menu :")
            print(" 1. List all books in the library")
            print(" 2. List all books that are checked out")
            print(" 3. Add a new book")
            print(" 4. Delete a book")
            print(" 5. Search a book by ISBN number")
            print(" 6. Search a book by name")
            print(" 7. Check out a book to a student")
            print(" 8. Add a new student ")
            print(" 9. List all students ")
            print("10. Exit")
            print()

            choice = input("Enter your choice: ")

            if choice == "1":
                self.list_all_books()
                print()
            elif choice == "2":
                self.list_checked_out_books()
                print()
            elif choice == "3":
                self.add_new_book()
                self.write_files(self.books_file_path,self.books)
                self.load_data()
                print()
            elif choice == "4":
                self.delete_book()
                print()
            elif choice == "5":
                self.search_by_isbn()
                print()
            elif choice == "6":
                self.search_by_name()
                print()
            elif choice == "7":
                self.check_out_books()
                print()
            elif choice == "8":
                self.add_new_student()
                self.write_files(self.students_file_path,self.students)
                self.load_data()
                print()
            elif choice == "9":
                self.list_all_students()
                print()
            elif choice == "10":
                self.write_files(self.books_file_path,self.books)
                self.write_files(self.students_file_path,self.students)
                print("Exiting. Data saved.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    library = Library()
    library.main_menu()