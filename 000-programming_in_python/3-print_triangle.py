# program to print right triangle
def print_right_triangle(height):


    for i in range(1, height + 1): #Loop through each level of the triangle
       
        #print i star for current level
        print('*' * i)
if __name__ == "__main__":
    #when this script is run directly, call the function to print triangle of 5h
    print_right_triangle(5)

