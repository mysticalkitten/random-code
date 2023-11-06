import random

# start of main loop
code_running = 11
while code_running > 1:
    # clears screen
    for i in range(100):
        print()

    # print title
    print(
        """
                        o                        8  o
                        8                        8
    .oPYo. o    o .oPYo.  o8P .oPYo. ooYoYo.   .oPYo8 o8 .oPYo. .oPYo.
    8    ' 8    8 Yb..     8  8    8 8' 8  8   8    8  8 8    ' 8oooo8
    8    . 8    8   'Yb.   8  8    8 8  8  8   8    8  8 8    . 8.
    `YooP' `YooP' `YooP'   8  `YooP' 8  8  8   `YooP'  8 `YooP' `Yooo'
    :.....::.....::.....:::..::.....:..:..:..:::.....::..:.....::.....:
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    """
    )

    # number one=sides of dice. number two=how many times its rolled
    def my_function(x, y):

        result = []
        for i in range(int(y)):
            result.append(random.randint(int(1), int(x)))

        return result

    numb1 = input("how many sides: ")
    numb2 = input("how many times: ")

    result = my_function(numb1, numb2)

    # print result list and sum
    print(result)
    print((str("sum: ")) + str(sum(result)))
    print()

    # run program again or stop code?
    run_again = input("run again? [y] or [n]: ")
    if run_again == "y":
        print("loding...")

    else:
        print("shutting down...")
        code_running = 0
