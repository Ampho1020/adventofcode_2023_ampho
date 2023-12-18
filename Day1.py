import fileinput

summa = 0
first_number = 0
last_number = 0
i_number = 0

def ConvertStringToNumbers(stringy):
    number_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    new_stringy = stringy
    tmp_string = ""
    i_found = False
    #We iterate five times. What we need is read the whole text, and without thinking, we read
    #character by character. If we read a first char, we check if it looks like any of the 
    #array's first character. And then the next. If it doesn't anymore, we delete the tmp string,
    #and start over. Make sure we read the string and delete first, before storing the character!
    for i in range(len(new_stringy)):
        char = new_stringy[i]
        for j in range(len(number_strings)):
            #We iterate this character through the next few characters. If the rest is found, then we add the number to the 
            #tmp_string. If not found, we simply add is as is to the tmp_string.
            if (char == number_strings[j][0]):
                #We search from the new_stringy's found index to the end of that number_string's character number for that string
                if (new_stringy[i : i+len(number_strings[j]) ] == number_strings[j]):
                    tmp_string += (str)(j+1)
                    i_found = True
        if (i_found == False):
            tmp_string += char

        i_found = False        
                
    return tmp_string

for l in fileinput.input(files = "Day1_input.txt"):

    #Converts the line into numbers. Needs upgrade!
    l_converted = ConvertStringToNumbers(l)

    #Checks for a digit, and then it will change them into two digit numbers, and add them to the sum. Works as intended!
    for i in range(len(l_converted)):
        if ((l_converted[i]).isdigit()) == True and (first_number == 0):
            first_number = (int)(l_converted[i])
        elif ((l_converted[i]).isdigit() == True) and (first_number != 0):
            last_number = (int)(l_converted[i])
    if (first_number != 0) and (last_number != 0):
        i_number = 10 * first_number + last_number
        summa += i_number
    elif (first_number != 0) and (last_number == 0):
        i_number = 10 * first_number + first_number
        summa += i_number
    first_number = 0
    last_number = 0
    i_number = 0

print(summa)