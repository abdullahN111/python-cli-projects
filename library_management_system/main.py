import os
import datetime

os.getcwd()

class LMS:
    """This class is used to keep record of books"""
    
    def __init__(self, list_of_books: str, library_name: str):
        self.list_of_books = "books.txt"
        self.library_name = library_name
        self.books_dict: dict = {}
        
        id = 101
        
        with open(self.list_of_books) as b:
            content = b.readlines()
        for line in content:
            self.books_dict.update({str(id): {"books_title": line.replace("\n", ""), "lender_name": "", "issue_date": "", "status": "Available"}})
            id = id+1
            
    def display_books(self):
        print("\n<---List Of Books--->\n")
        print("Book ID", "\t", "Title")
        print("---------------------------")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "- [", value.get("status"), "]")
            
    def issue_books(self):
        book_id = input("Enter Book ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if book_id in self.books_dict.keys():
            if not self.books_dict[book_id]["status"] == "Available":
                print(f"This book is already issued to {self.books_dict[book_id]["lender_name"]} on {self.books_dict[book_id]["issue_date"]}")
                return self.issue_books()
            elif self.books_dict[book_id]["status"] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[book_id]["lender_name"] = your_name
                self.books_dict[book_id]["issue_date"] = current_date
                self.books_dict[book_id]["status"] = "Already Issued"
                print("Book issued successfully. \n")
            
        else:
            print("Book ID not found!")
            return self.issue_books()
        
    def add_books(self):
        new_book = input("Enter book title with author name: ")
        if new_book == "":
            return self.add_books()
        
        elif len(new_book) > 50:
            print("Title length too long! It should be less than 30 characters.")
            return self.add_books()
        
        else:
            with open(self.list_of_books, "a") as b:
                b.writelines(f"{new_book}.\n")
            self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_book,'lender_name':'','lend_date':'', 'status':'Available'}})
            print(f"The books '{new_book}' has been added successfully !!!")
            
            
    def return_books(self):
        books_id = input("Enter Books ID : ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] == 'Available':
                print("This book is already available in library. Please check book id. !!! ")
                return self.return_books()
            elif not self.books_dict[books_id]['status'] == 'Available':
                self.books_dict[books_id]['lender_name'] = ''
                self.books_dict[books_id]['lend_date'] = ''
                self.books_dict[books_id]['status']= 'Available'
                print("Successfully Updated !!!\n")
        else:
            print("Book ID Not Found !!!")

if __name__ == "__main__":
    try:
        mylms = LMS("list_of_books.txt", "Python's")
        press_key_list = {"1": "Display Books", "2": "Issue Books", "3": "Add Books", "4": "Return Books", "5": "Quit"}    
        
        key_press = ""
        while not (key_press == "5"):
            print(f"\n----------Welcome To {mylms.library_name}'s Library Management System---------\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ")
            if key_press == "1":
                print("\nCurrent Selection : DISPLAY BOOKS \n")
                mylms.display_books()
                
            elif key_press == "2":
                print("\nCurrent Selection : ISSUE BOOKS\n")
                mylms.issue_books()

            elif key_press == "3":
                print("\nCurrent Selection : ADD BOOK\n")
                mylms.add_books()
            
            elif key_press == "4":
                print("\nCurrent Selection : RETURN BOOK\n")
                mylms.return_books()
            elif key_press == "5":
                break
            else:
                continue
    except Exception as e:
        print("Something went wrong. Please check. !!!")