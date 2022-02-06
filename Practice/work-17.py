def perfectnumber(number):

    total = 0

    for i in range(1,number):
        if number % i == 0:
            total += i

    return total == number

                