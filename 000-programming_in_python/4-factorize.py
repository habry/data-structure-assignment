# program that factorize input number into it's prime factor

def factorize(number):
    #This function return the prime factors of the given number as a list

    factors = [] #initialize an empty list to srore prime factor

    divisor = 2 #Start with the smallest prime number

    #continue the loop until the number is reduced to 1
    while number > 1: 
        #check if the current number is divisible by the divisor
        while number % divisor == 0:

            factors.append(divisor)

            number //= divisor

        divisor += 1 #increment

    return factors

if __name__ == "__main__":
    print(factorize(10))  # test for 10

