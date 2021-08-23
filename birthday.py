import datetime

date = datetime.datetime.now()  # date class.
# formatting date to string. %B returns full month name.
currMonth = date.strftime("%B").lower()


def birthday():
    name = input('What is your name?\t').capitalize()
    month = input(f'Hi {name}!, what month were you born in?\t').lower()

    # check if current month is users birthday month.
    if month == currMonth:
        print(f'Happy birthday month {name}!')
    else:
        print(f'Happy Early or belated birthday {name}')
    print(f'Fun fact there are {str(len(name))} letters in your name.')


birthday()
