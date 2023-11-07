#define
password = 'password'
username = 'admin'
logged_in = 0
script_running = 1

#main script loop start
while script_running == 1:
    while logged_in == 0:
        print('log in')
        user_name = input('enter username: ')
        user_password = input('enter password: ')

        if user_name == username and password == user_password:
            logged_in = 1
            print('logged in')



        else:
            print('''
            loggin failed''')
            print('''

               ''')
    # everything from here on will work if logged_in = 1
    # if logged_in = 0 it will loop back to login recuired

    choose_program = input('''
    choose program:
    [1] custom dice
    [2] basic calkulator
    [3] log out
    [4] shutt down
     ''')

    if choose_program == '1':
        import random

        # start of dice loop
        dice_running = 'y'

        while dice_running == 'y':
            # clears screen
            for i in range(100):
                print()

            # print title
            print('''
                                o                        8  o              
                                8                        8                  
            .oPYo. o    o .oPYo.  o8P .oPYo. ooYoYo.   .oPYo8 o8 .oPYo. .oPYo.
            8    ' 8    8 Yb..     8  8    8 8' 8  8   8    8  8 8    ' 8oooo8
            8    . 8    8   'Yb.   8  8    8 8  8  8   8    8  8 8    . 8.    
            `YooP' `YooP' `YooP'   8  `YooP' 8  8  8   `YooP'  8 `YooP' `Yooo'
            :.....::.....::.....:::..::.....:..:..:..:::.....::..:.....::.....:
            :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            ''')


            # number one=sides of dice. number two=how many times its rolled
            def my_function(x, y):
                result = []

                for i in range(int(y)):
                    result.append(random.randint(int(1), int(x)))

                return result

            numb1 = input('how many sides: ')
            numb2 = input('how many times: ')

            result = my_function(numb1, numb2)

            # print result list and sum
            print(result)
            print((str('sum: ')) + str(sum(result)))
            print()

            # run program again or stop code?
            run_again = input('run again? [y] or [n]: ')
            if run_again == 'y':
                print('loding...')

            else:
                print('shutting down...')
                dice_running = 'n'






    if choose_program == '2':
        run_program2 = 'y'
        while run_program2 == 'y':
            # importing nessesery systems
            print('''
            basic adission calculator
            ''')
            first_number = int(input('enter first number: '))
            second_number = int(input('enter second number: '))
            third_number = first_number + second_number
            print()
            print('sum: ' + str(third_number))
            print()

            # user input for redoing second code
            print('do you want to run this code again program again? ')
            run_program2 = input('press [y] to confirm, and [n] to decline ')
            if run_program2 == 'y':
                run_program2 = 'y'

            else:
                run_program2 = 'n'


    if choose_program == '3':
        # logout
        print('do you want to log out? ')
        log_out = input('press [y] to confirm, and [n] to decline ')

        if log_out == 'y':
            print('''logging out...

                      ''')
            logged_in = 0

        else:
            print()

    if choose_program == '4':
        shutting_down = input('''do you want to shut down?
        press [y] to confirm, and [n] to decline ''')

        if shutting_down == 'y':
            print('shutting down...')
            script_running = 0

        else:
            print()


#main script loop end
