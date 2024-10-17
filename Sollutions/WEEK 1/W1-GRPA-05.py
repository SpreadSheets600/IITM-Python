age = int(input())  # int: Read age from standard input
dob = input()  # str: Read date of birth in format day/month/year from standard input
day, month, year = dob.split("/")  # str: split the dob into day, month and year

fifth_birthday = f"{day}/{month}/{int(year)+5}"  # str: dob same day after 5 years formatted as day/month/year

last_birthday = f"{day}/{month}/{int(year)-1}"  # str: dob same day last year formatted as day/month/year

tenth_month = f"{day}/10/{year}"  # str: dob in 10th month formatted as day/10/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(f"{tenth_month}, {fifth_birthday}, {last_birthday}")

weight = float(input())  # float: Read weight in kg from standard input

weight_readable = f"{str(int(weight.split('.')[0]))} kg {str(int(weight.split('.')[1]))} g"  # str: weight in kg and gms

# print weight_readable
print(weight_readable)
