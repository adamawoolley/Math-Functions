def prime(Tested_Number):
    
    Number = 2
    Prime = True

    while Prime == True and Number < Tested_Number:

        if Tested_Number % Number == 0:
            Prime = False
        else:
            Number += 1
            
    if Prime == False:
        return str(Tested_Number) + ' is not a prime number'
    else:
        return str(Tested_Number) + ' is a prime number'

print(prime(int(input('What number do you want to check for prime?: '))))
