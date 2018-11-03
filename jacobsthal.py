# a(n) = a(n-1) + 2*a(n-2), with a(0) = 0, a(1) = 1


def jacobsthal(n=5, output=[], number=0):
    amount = input('Choose a number (at least 5): ')
    try:
        amount = int(amount)
        if amount < 5:
            n = 5
            print('I chose 5 for you because you can\'t follow instructions')
        else:
            n = amount
    except ValueError:
        print('That was not a number. Try again later')
        exit()
    while n > 0:
        output.append(number)
        if len(output) >= 2:
            number = output[len(output) - 1] + 2 * output[len(output) - 2]
        else:
            number = 1
        n -= 1
    return output


print(jacobsthal())
