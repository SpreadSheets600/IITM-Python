class Student:  # <--- Class Name Should Be Capitalized ( Standard Practice )
    COUNT = 0  # <--- Class Variable It Will Be Shared By All The Objects Of The Class
    # Not Like It Will Have It's Own Copy, It Will Be Shared By All The Objects
    # It's Like A Global Variable For The Class

    def __init__(
        self, roll_no=None, name=None, total_marks=0
    ):  # <--- This Is The Constructor, Gets Called When We Create An Object Of A Class, Helps In Initializing The Object
        # It Is Used To Initialize The Object's State, It Helps To Call The Object's Attributes While Creating The Object
        # It Takes `self` As The First Argument, Which Is A Reference To The Object Itself
        # It's A Special Function, It's Called Automatically When We Create An Object
        # It Can Take More Arguments, Which Will Be Passed While Creating The Object
        self.total_marks = total_marks
        self.roll_no = roll_no
        self.name = name
        
    # Self Is A Reference To The Object Itself, It's A Reference To The Object That Is Calling The Method

    def display(self):  # <--- This Is A Method, It's A Function Inside A Class
        print(self.roll_no, self.name, self.total_marks)

    def result(self):
        if self.total_marks > 100:
            return "PASS"
        else:
            return "FAIL"


s0 = Student(0, "SOHAM", 150)  # <--- Creating Object Of Student Class
# Passing The Values To The Constructor Which Will Initialize The Object And Is Done By __init__ Method
# This Is How We Make Sure Have It's Own Identity, But Still Have Some Common Attributes
# This Is How We Can Pass The Values To The Constructor While Creating The Object
s0.display()

Student.COUNT += 1  # <--- It Is Only Copy Of COUNT, It Will Be Shared By All The Objects, Thus Used With Class Name
# But Roll No And Name Are Instance Attributes, They Are Different For Each Object
# It Is Class Attribute, It's Shared By All The Objects Of The Class

s1 = Student()
s1.display()

Student.COUNT += 1  # <--- It Is Only Copy Of COUNT, It Will Be Shared By All The Objects, Thus Used With Class Name

print(s0.result())
