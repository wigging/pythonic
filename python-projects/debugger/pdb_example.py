import pdb


def main():
    """
    Set trace if number divisible by 3.
    """

    for number in range(10):

        number_x2 = number * 2

        print('number   is', number)
        print('number×2 is', number_x2)

        if number != 0 and number % 3 == 0:
            pdb.set_trace()
            print('number is divisible by 3')


if __name__ == '__main__':
    main()
