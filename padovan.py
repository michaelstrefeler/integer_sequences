# a(n) = a(n-2) + a(n-3) with a(0)=1, a(1)=a(2)=0


def padovan(n, output=[], number=1):
    while n > 0:
        output.append(number)
        if len(output) >= 3:
            number = output[len(output) - 2] + output[len(output) - 3]
        else:
            number = 0
        n -= 1
    return output


number = input('Choose a number (at least 5): ')
try:
    number = int(number)
    if number < 5:
        number = 5
        print('I chose 5 for you because you can\'t follow instructions')
except ValueError:
    print('That was not a number. Try again later')
    exit()

print(padovan(number))
