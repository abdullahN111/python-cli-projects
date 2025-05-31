
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    def display_person(self) -> None:
        print(f"Person [ Name: {self.name}, Age: {self.age} ] ")
        
        
class Student(Person):
    rollnum: int
    courses: list[str] = []
    
    def __init__(self, name: str, age: int, rollNum: int) -> None:
        super().__init__(name, age)
        self.rollnum = rollNum
    
    def register_courses(self, course) -> None:
        self.courses.append(course)


class Course:
    id: int
    name: str
    students: list[str] = []
    instructers: list[str] = []
    
    
    def __init__(self):
        pass