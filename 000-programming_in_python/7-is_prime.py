# to write a program to declare if entered number is prime or not

def is_prime(number):

    #check if number is less than or equal to 1
    if number<=1:
        return False
    
    #check the factor from 2 to the square root of a number
    for i in range(2, int(number**0.5)+1):

        if number % i ==0: #when number divisible by i is not prime number
            return False
    return True
user = int(input("Enter number:"))

if __name__=="__main__":

    print(is_prime(user))