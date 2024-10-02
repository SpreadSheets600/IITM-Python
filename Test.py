time = '02 AM'
is_time_valid = True if ( int(time[0:2]) >= 1 and int(time[0:2]) <= 12 ) else False
print(is_time_valid)