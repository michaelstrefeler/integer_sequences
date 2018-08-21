# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1


def fibonacci(n, output=[], number=0):
    while n > 0:
        output.append(number)
        if len(output) >= 2:
            number = output[len(output) - 1] + output[len(output) - 2]
        else:
            number = 1
        n -= 1
    return output


print(fibonacci(50))
