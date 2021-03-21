import arrays
import csv

"""
File Reading

You have been given a file called "pokemon.csv". Your job is to use the file to print the name of the Pokemon of the given type that has the highest stat of the given stat type.
For example, find_highest_stat("Fire", "HP") should print "The Fire pokemon with the most HP is Emboar".
"""
def find_highest_stat(a_type, stat):
    current_highest = 0
    name = ''
    TYPE_INDEX = 2
    NAME_INDEX = 1
    try:
        with open("pokemon.csv") as csv_file:
            csv_file = csv.reader(csv_file)
            stat_name = next(csv_file)[stat]
            for line in csv_file:
                if(line[TYPE_INDEX] == a_type):
                    if(int(line[stat]) > current_highest):
                        current_highest = int(line[stat])
                        name = line[NAME_INDEX]
            print(f"The {a_type} pokemon with the most {stat_name} is {name}")
            #print("The", a_type, "pokemon with the most", stat_name, "is", name)
    except FileNotFoundError:
        print("Error, file not found")


"""
Arrays

Write a function that, given an array, creates another array called "squares" that holds the values of the original array, squared.
Then return the equivalent of the original array concatenated with squares. (Hint: you will need to create another array to do this!)
"""
def square_elements(an_array):
    array = arrays.Array(len(an_array) * 2)
    #counter = 0
    # for i in range(len(an_array)):
    #     array[i] = an_array[i] ** 2
    #     counter += 1
    # for i in range(len(an_array)):
    #     array[counter] = an_array[i]
    #     counter += 1
    # or
    counter = len(an_array)
    for i in range(len(an_array)):
        array[i] = an_array[i] ** 2
        array[i + counter] = an_array[i]
    return array

"""
Lists

Write a function that, given a filename and a letter, prints out the elements that start with the given letter. You must use a list at some point in your function!
If no element is found, print "No element starts with the letter <letter>"
"""
def find_elements(filename, letter):
    result = []
    try:
        with open(filename) as the_file:
            for line in the_file:
                if line[0].lower() == letter.lower():
                    result.append(line.strip())
    except FileNotFoundError:
        print("Error, file not found")
    
    if(len(result) == 0):
        print("No elements starts with the letter", letter)
    else:
        print(result)

    
"""
Write a function that returns true if the list is a palindrome and
false if the list is not a palidrome.

Do this without using slicing
"""
def is_palidrome(a_list):
    while(len(a_list) > 1):
        if(a_list[0] != a_list[-1]):
            return False
        #a_list = a_list[1:-1]
        # True no slicing solution
        a_list.pop(0)
        a_list.pop(-1)
    return True


"""
Recursion

Write a function that recursively computes the gcd of two numbers given as parameters. Then, write at least one test function to test your gcd function.
Use the definition that if num1 = num2 then the answer if num1
If num1 > num2 then the answer if the GCD of num1 - num2 and num2
If num2 > num2 then the answer is the GCD of num1 and num2 - num1
"""
def gcd(num1, num2):
    if num1 == num2 :
        return num1
    elif num1 > num2:
        return gcd(num1 - num2, num2)
    else:
        return gcd(num1, num2 - num1)

find_highest_stat("Fire", 5)
print(square_elements([1, 2, 3, 4, 5]))
find_elements("stockroom.txt", 'a')
find_elements("stockroom.txt", 'y')