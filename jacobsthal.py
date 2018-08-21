# a(n) = a(n-1) + 2*a(n-2), with a(0) = 0, a(1) = 1


def jacobsthal(n, output=[], number=0):
    while n > 0:
        output.append(number)
        if len(output) >= 2:
            number = output[len(output) - 1] + 2 * output[len(output) - 2]
        else:
            number = 1
        n -= 1
    return output


print(jacobsthal(50))
