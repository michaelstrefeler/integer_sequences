# a(n) = a(n-1) + a(n-2) + a(n-3) with a(0)=a(1)=0, a(2)=1


def tribonacci(n):
    output = [0, 0]
    number = 1
    x = n
    while n > 0:

        output.append(number)
        if len(output) >= 2:
            number = output[len(output) - 1] + output[len(
                output) - 2] + output[len(output) - 3]
        n -= 1
    return output[:x]


print(tribonacci(50))
