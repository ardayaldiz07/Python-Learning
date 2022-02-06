# Toplama işlemi.
def sum(number1, number2):
    return number1 + number2

# Çıkarma işlemi.
def ext(number1, number2):
    return number1 - number2

# Çarpma işlemi
def imp(number1, number2):
    return number1 * number2


# Bölme işlemi.
def div(number1, number2):
    return number1/number2

# Faktöriyel bulma işlemi.
def factorial(number):
    total = 1

    for i in range(2, number + 1):
        total *= i

    return total

# Çift sayı bulma işlemi.
def double(number):
    doublelist = []

    for i in range(1, number + 1):
        if i % 2 == 0:
            doublelist.append(i)
    return doublelist

# Fibonacci serisi oluşturma.
def fibonacci(number):

    a = 1
    b = 1

    fibonacci = [a, b]

    for i in range(1, number):
        a, b = b, a+b
        fibonacci.append(b)
        
    print(fibonacci)
    
    return a, b

# Asal sayı bulma.
def prime(number):
    if (number == 1):
        return "Asal değil"

    elif(number == 2):
        return "Asal"
    else:
        for i in range(2, number):
            if (number % i == 0):
                return "Asal değil"
        return "Asal"

# Sayı yuvarlama.
def roundnumber(number):
    return round(number)
