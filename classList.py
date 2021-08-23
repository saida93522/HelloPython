def class_list():
    try:
        user_list = []  # empty list
        num = int(input('How many classes are you taking this semester?\t'))
        counter = 0
        # Verify user is taking classes this semester
        if num <= 0:
            print('You are not taking any classes this semester')
            return
        else:
            while num > counter:
                classes = input('Enter the name of the class: ')
                user_list.append(classes)
                counter += 1

            print('\nThe classes you are taking are:')
            for classList in user_list:
                print(classList.capitalize())
    # catch errors that user might input other than numbers
    except ValueError:
        print('Error, Make sure you are entering only a number')
        class_list()


class_list()
