#program that accept string into dictionary

def character_frequency(string):
    # Initialize an empty dictionary to store character frequencies
    freq_dict = {}
    
    # Convert the entire string to lowercase to handle case insensitivity
    string = string.lower()
    
    # Iterate through each character in the string
    for char in string:
        # Check if the character is alphabetic
        if char.isalpha():
            # Update the frequency count for the character
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    
    return freq_dict

if __name__ == "__main__":
    
    my_string = input("Enter the string")

    print(character_frequency(my_string))
