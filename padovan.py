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


print(padovan(50))
