from re import sub
# import regEx's substring method


def to_camel_case(user_input):
    try:
        # check if sentence starts with a number
        if user_input[0].isnumeric():
            return print('Err sentence cannot start with a number')
        elif '#' in user_input or "'" in user_input:
            return print("Oops try again.Could not produce a valid variable name.Exclude: #,' ")
        else:
            user_input = sub(
                r"(_|-)+", " ", user_input).title().replace(" ", "")
            print(user_input[0].lower() + user_input[1:])
    except ValueError:
        print('Please enter only a string.Do not start with number')


to_camel_case(input('Enter a sentence:\t'))
