# program that return sum of all even numbers from the list

def sum_even_numbers(my_list):

    sum = 0

    for i in my_list:

        if (i % 2 == 0):

            sum = sum+i

    return sum

# calling of def with an arguement of [12,5,10,3,6]


if __name__ == "__main__":

    print(sum_even_numbers([12, 5, 10, 3, 6]))
