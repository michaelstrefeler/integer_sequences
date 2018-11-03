# a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4) with a(0)=a(1)=a(2)=0, a(3)=1


def tetranacci(n, output=[0, 0, 0], number=1):
    x = n
    while n > 0:
        output.append(number)
        if len(output) >= 4:
            number = output[len(output) - 1] + output[len(
                output) - 2] + output[len(output) - 3] + output[len(output) -
                                                                4]
        n -= 1
    return output[:x]


number = input('Choose a number (at least 5): ')
try:
    number = int(number)
    if number < 5:
        number = 5
        print('I chose 5 for you because you can\'t follow instructions')
except ValueError:
    print('That was not a number. Try again later')
    exit()

print(tetranacci(number))
