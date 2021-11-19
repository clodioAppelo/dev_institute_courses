# Exercise 7: When Will I Retire ?
# Instructions
# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).

# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# After calculating the age of a person, the function should return the age (the age is an integer).
# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.


def get_age(day, month, year):
    current_year = 2021
    current_month = 11
    current_day = 18
    age = current_year - year
    if current_month < month:
        age -= 1
    elif current_month == month:
        if current_day < day:
            age -= 1
    return age


def can_retire(gender, date_of_birth):
    num_date_list = list(map(lambda s: int(s), date_of_birth.split('/')))

    my_age = get_age(*num_date_list)
    if gender == 'm' and my_age >= 67:
        return True
    elif gender == 'f' and my_age >= 62:
        return True
    else:
        return False


print(can_retire('m', '27/10/1952'))
