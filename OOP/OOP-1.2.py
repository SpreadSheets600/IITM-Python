# We Define A Class Uing `class` Keyword
# It Defines A Blueprint For Creating Objects


class Student:  # <--- Class Name Should Be Capitalized ( Standard Practice )
    roll_no = None  # <--- Class Variable, It's None Since It Will vary From Student To Student
    name = None  # <--- Another Class Variable


# Now We Can Create Objects Of This Class, Which Will Have These Variables And Default Values Would Be None

# Creating Object Of Student Class
s0 = (
    Student()
)  # <--- Object Of Student Class, It's A Special Function Called Constructor
s1 = Student()  # <--- Another Object Of Student Class
s2 = Student()  # <--- Another Object Of Student Class
# Constructor Is A Function ( Having Same Name As Class ) That Gets Called When We Create An Object Of A Class

s0.roll_no = 0  # <--- Setting Roll No Of Student 0
s0.name = "SOHAM"  # <--- Setting Name Of Student 0

# Using Construtor We Created The Object Of Student Class
# Using Dot Operator We Can Access The Variables Of The Object
# Format For Using Dot Operator : `Object.Variable` Or `Object.Method()`
# This Is How We Access The Attributes And Behaviour Of An Object

# This Is How We Make Sure Have It's Own Identity, But Still Have Some Common Attributes

print(s0.roll_no, s0.name)  # <--- Printing Roll No And Name Of Student 0
