print('To find a factor just type factor(number you want to find the factors of) into the console and type enter')

##Find the factors of any number

def factor(test_number):
    
    divisor = 1
    factors = str('')

    while test_number >= divisor:

        if test_number % divisor == 0:
            factors += str(divisor)
            factors += str(' ')
            divisor += 1
        else:
            divisor += 1

    print('The factors of ' + str(test_number) + ' are ' + str(factors))
