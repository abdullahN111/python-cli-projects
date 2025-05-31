import json
from typing import Any


file_path = "students.json"
def load_students():
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

        
class Course:
    def __init__(self, courses: list[str]) -> None:
        self.courses = courses
        
        

courses: Course = Course([
    "Software Engineering",
    "Computer Science",
    "Data Science",
    "Artificial Intelligence",
    "Bio Technology",
    "Robotics Engineering",
])


  
class Student:
        
    def save_student(self, student: Any) -> None:
        data = load_students()
        data.append(student)
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    def register_student(self) -> None:
        
        
        try:
            std_name: str = input("Enter Student Name: ")
            std_age: int = int(input("Enter Student Age: "))
            std_rollNum: int = int(input("Enter Student Roll Number: "))
            print("\nSelect a course.")
            for index, course in enumerate(courses.courses):
                print(f"#{index+1}. {course}")
            std_course_index_input: str = input("\nEnter Student Course Number: ")
            try:
                std_course_index = int(std_course_index_input) - 1
            except ValueError:
                print("Invalid course number!")
                return
            if std_course_index not in range(len(courses.courses)):
                print("Invalid course number!")
                return

            std_course = courses.courses[std_course_index]

            for student in load_students():
                if student["name"] == std_name or student["rollNum"] == std_rollNum:
                    print("Student already exist!")
                    return
                    
            new_student: dict[str, Any] = {
                "rollNum": std_rollNum,
                "name": std_name,
                "age": std_age,
                "course": std_course
            }
        
            self.save_student(new_student)
            print("Student Registered Successfully.")
            

            
    
    def list_students(self) -> None:
        students = load_students()
    
        if not students:
            print("\nNo students found.")
            return

        print("\nList of Students:\n")
        for index, student in enumerate(students, start=1):
            print(f"{index}. Name     : {student['name']}")
            print(f"   Age      : {student['age']}")
            print(f"   Roll No. : {student['rollNum']}")
            print(f"   Course   : {student['course']}")
            print("-" * 30)
            

student: Student = Student()

def main() -> None:
    condition = True
    options = ["List Students", "Register Student", "Exit"]
    
    print("\n<---Student Management System--->\n")
    print("---------------")
    while condition:
        for index, option in enumerate(options):
            print(f"{index+1}. {option}")
            
        user: int = int(input("\nSelect an option: "))
        
        if user == 1:
            student.list_students()
        
        elif user == 2:
            student.register_student()
            
        elif user == 3:
            print("\nExiting...")
            condition = False
            
        else:
            print("Invalid Input!")
            continue
        

            
if __name__ == "__main__":
    main()