class Student:

    def __init__(self, roll_no=None, name=None, total_marks=0):
        self.total_marks = total_marks
        self.roll_no = roll_no
        self.name = name

    def display(self):
        print(self.roll_no, self.name, self.total_marks)

    def result(self):
        if self.total_marks > 100:
            return "PASS"
        else:
            return "FAIL"


class Employee:

    def __init__(self, emp_id=None, name=None, salary=0):
        self.salary = salary
        self.emp_id = emp_id
        self.name = name

    def display(self):
        print(self.emp_id, self.name, self.salary)


# In The Above Two Classes There Is A Lot Of Common Things, Like Name And ID
# We Can Create A Super Class And Inherit It In The Other Classes
# This Will Help In Reducing The Code Duplication
# This Is Called Inheritance


class Person:  # <--- Super Class / Parent Class / Base Class

    def __init__(
        self, profession=None, name=None, age=0
    ):  # <--- Constructor For The Super Class Which Will Be Inherited By The Sub Classes
        self.__profession = (
            profession  # <--- Private Attribute, Can Only Be Accessed Inside The Class
        )
        self.name = name
        self.age = age

    def display(
        self,
    ):  # <--- Method For The Super Class Which Will Be Inherited By The Sub Classes
        print(self.profession, self.name, self.age)


class Student(
    Person
):  # <--- Sub Class / Child Class / Derived Class : Directly Inheriting From The Super Class ( Person ) And It Will Have All The Attributes And Methods Of The Super Class

    def __init__(
        self, roll_no=None, name=None, age=0, total_marks=0
    ):  # <--- Constructor For The Sub Class And It Has It's Own Attributes And Also The Attributes Of The Super Class
        super().__init__(
            name, age
        )  # <--- Calling The Constructor Of The Super Class, So That The Super Class Attributes Are Also Initialized
        self.total_marks = total_marks
        self.roll_no = roll_no

    def display(self):
        print(self.roll_no, self.name, self.age, self.total_marks)

    def result(self):
        if self.total_marks > 100:
            return "PASS"
        else:
            return "FAIL"


class Employee(Person):

    def __init__(
        self, emp_id=None, name=None, age=0, salary=0
    ):  # <--- Constructor For The Sub Class
        super().__init__(name, age)  # <--- Calling The Constructor Of The Super Class
        self.salary = salary
        self.emp_id = emp_id

    def display(self):
        print(self.emp_id, self.name, self.age, self.salary)


s0 = Student(0, "SOHAM", 18, 150)
s0.display()

e0 = Employee(
    0, "Sagnik", 18, 100000
)  # <--- Creating Object Of Employee Class, It Will Have All The Attributes Of The Super Class ( Person ) And It's Own Attributes
e1 = Employee(1, "Utkarsh", 17, 100000)
e0.display()

# Data Hiding
# We Can Make The Attributes Private By Prefixing Them With Double Underscore
# This Will Make The Attributes Private And Can Only Be Accessed Inside The Class
# We Can Create Methods To Access These Attributes
# This Is Called Data Hiding


class Gamer(Person):

    def __init__(self, name=None, age=0, games=None):
        super().__init__(name, age)
        self.__games = games

    def display(self):
        print(self.name, self.age, self.__games)

    def get_games(self):
        return self.__games

    def set_games(self, games):
        self.__games = games


# Encapsulation
# Encapsulation Can Be Achieved By Making The Attributes Private And Creating Methods To Access Them
# Encapsulation Is Used To Prevent Direct Access To Some Of The Object's Components
# Encapsulation Is The Packing Of Data And Functions Into A Single Component
# It Is The Restriction Of Direct Access To Some Of An Object's Components
# Encapsulation Is Also Called As Information Hiding
