# a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2)


def pell(n=5, output=[], number=0):
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
        if number > 1:
            number = 2 * output[len(output) - 1] + output[len(output) - 2]
        else:
            number += 1
        n -= 1
    return output


print(pell())
