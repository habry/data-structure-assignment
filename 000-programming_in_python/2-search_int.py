# search for the first occurence of an interger

def find_first_occurence(my_list, num):

    # loop for iterating elements in my_list

    for i in range(len(my_list)):

        if my_list[i] == num:

            # here return value for elements in my list when iterating

            return i


# return statement if the elements in list does not exist

    return -1


# calling statement with an arguement of [6,7,9,3,1] and the searching element is 9

if __name__ == "__main__":
    
    print(find_first_occurence([6, 7,1, 9, 3, 1], 1))
