# program to print smallest integer in a list


def get_smallest_integer(my_list):

    #This function return the smallest number from the list
    return min(my_list)

if __name__ == "__main__":

    my_list = [3, 11, 4, 1, 5, 9] #sample list

    print(get_smallest_integer(my_list))  # Output: 1

