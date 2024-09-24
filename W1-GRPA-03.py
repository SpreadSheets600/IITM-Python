# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.

s = "hello pyhton"
course_code = "24t2cs1002" # 24 - year, t2 - term 2, cs1002 - course id
# <eoi>

output1 = s[2] # str: get the third character of s

output2 = s[-4] # str: get the fourth last character of s

output3 = s[0:3] # str: get the first 3 characters of s

output4 = s[0::2] # str: get every second character of s

output5 = s[-3:] # str: get the last 3 characters of s

output6 = s[::-1] # str: get the reverse of s

course_term = int(course_code[3:4]) # int: get the term of the year as number from course_code
course_year = int(course_code[0:2]) # int: get the year as two digit number from course_code
