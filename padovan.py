# a(n) = a(n-2) + a(n-3) with a(0)=1, a(1)=a(2)=0


def padovan(n=5, output=[], number=1):
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
        if len(output) >= 3:
            number = output[len(output) - 2] + output[len(output) - 3]
        else:
            number = 0
        n -= 1
    return output


print(padovan())
