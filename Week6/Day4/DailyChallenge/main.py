# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~
#
# The number of candles on the cake should be the last number of the users age, if they
#     are 53, then add 3 candles.


birth_date = input('Give us your birthdate in the following format DD/MM/YYYY: ')

day, month, year = birth_date.split('/')
current_date = {
    'day': 10,
    'month': 11,
    'year': 2021
}

day, month, year = int(day), int(month), int(year)

age = current_date['year'] - year
if month > current_date['month']:
    age -= 1
elif month == current_date['month'] and day > current_date['day']:
    age -= 1

print(f'I am {age} years old')
candles = int(str(age)[-1]) * 'i'


candle_string = f"{(11-len(candles))//2 * '_'}{candles}{(11-len(candles))//2 * '_'}"
if len(candle_string) % 2 == 0:
    candle_string += '_'

cake = f'''
       {candle_string}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
'''
print(cake)

