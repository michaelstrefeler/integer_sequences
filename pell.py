# a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2)


def pell(n, output=[], number=0):
    while n > 0:
        output.append(number)
        if number > 1:
            number = 2 * output[len(output) - 1] + output[len(output) - 2]
        else:
            number += 1
        n -= 1
    return output


print(pell(50))
