'''
✅ Section B: Lower Intermediate (2–3 Marks Each)

(Conditions, Loops, String Operations, Functions Basics)
11. Write a function that takes two numbers and returns the larger one.
12. Write a program that prints all odd numbers between 1 to 20.
13. Explain the difference between break and continue with examples.
14. Write a Python program to count the number of lowercase and uppercase letters in a string.
15. Create a function that checks if a string contains only alphabets.
16. Explain scope of a variable (global vs local) with examples.
17. Write a program to find the length of a string without using len().
18. Write a function that accepts a string and returns it in reverse order.
19. What is the purpose of pass in Python? Explain with a case.
20. Write a program that prints the square of each number from 1 to 10 using a loop.

✅ Section C: Intermediate Level (3 Marks Each)

(Data Structures, Functions, Input Validation, Math Logic)
21. Write a function that accepts a list and returns a new list with only even numbers.
22. Create a program to count occurrences of each character in a string using dictionary.
23. Write a function that checks whether a given year is a leap year.
24. Write a program to merge two dictionaries.
25. What is list slicing? Show 3 slicing operations on a sample list.
26. Write a program to display the multiplication table of a number (1 to 10).
27. Create a menu-driven program: 1. Add, 2. Subtract, 3. Exit
28. Write a function to calculate the LCM of two numbers.
29. Create a program to remove all spaces from a sentence.
30. Write a Python program that checks if a number is a strong number.

✅ Section D: Upper Intermediate Level (4 Marks Each)

(Advanced Functions, Sets, Tuples, Lambda, Exception Handling)
31. Write a function using lambda to square each element of a list.
32. Explain the use of map() with a program to double list elements.
33. Write a program to input 5 numbers and store only unique values in a set.
34. Write a program that accepts marks of 5 subjects and prints grade with percentage.
35. What are args and kwargs in Python? Demonstrate both.
36. Write a function that checks whether a string is an anagram of another.
37. Write a program to handle ValueError using try-except block.
38. Create a tuple of 5 elements. Show how to convert it to a list and modify the third item.
39. What is recursion? Write a recursive function for factorial.
40. Create a function that returns True if all items in a list are of the same type.
'''


# Q11 ->>11. Write a function that takes two numbers and returns the larger one.

def larger_number(a,b):
    """Returns the larger of two numbers."""
    if a>b:
        return a
    else:
        return b

def LargeN_calling_func():
    """Calculate the larger of two numbers."""
    input_a = int(input("Enter first number: "))
    input_b = int(input("Enter second number: "))
    larger = larger_number(input_a,input_b)
    lower = (input_a + input_b) - larger
    print(f"The larger number is: {larger} and lower number is:{lower}")


# Q12 ->>12. Write a program that prints all odd numbers between 1 to 20.
def print_odd_Even_numbers():
    """Prints all Odd and Even numbers between 1 to that number and find out all prime numbers in odd numbers.""" # this is a docstring, it describes the function's purpose
    # Using list comprehension to generate odd numbers
    # user input 
    Users_Choice = input("Do you want to print this? (yes/no): ")
    if Users_Choice.lower() != "yes":
        print("Exiting the program.")
        return 
    else:
        Input_Number = int(input("Enter That Numbers:"))
        if Input_Number < 1:
            print("Please enter a number greater than 0.")
            return print_odd_numbers()
        print("\nPrinting odd and Even numbers between 1 to", Input_Number, "...\n\n")
        print_odd_numbers =[num for num in range(1,Input_Number) if num % 2 != 0]
        Find_All_prime_numbers_odd = [num for num in print_odd_numbers if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
        print_Even_numbers =[num for num in range(1,Input_Number) if num % 2 == 0]
        print(f"Odd numbers between 1 to {Input_Number} are: {print_odd_numbers}\n\nAnd Even numbers are: {print_Even_numbers}\n\n")
        print(f"In the odd numbers list,\nAll prime numbers are: {Find_All_prime_numbers_odd} \n\n")
        

# Q13 ->>13. Explain the difference between break and continue with examples.
def break_continue_example():
    """Demonstrates the difference between break and continue in loops.

    Break statements are used to exit a loop prematurely, 
    while 
    continue statements skip the current iteration and move to the next one.

    Here's an example of each: 

    """
    print("Break Example:")
    for i in range(10):
        if i == 5:
            break  # Exits the loop when i is 5
        print(i, end=' ')
    print("\nBreaking at 5")

    print("\nContinue Example:")
    for i in range(10):
        if i == 5:
            continue  # Skips the rest of the loop when i is 5
        print(i, end=' ')
    print("\nSkipping 5")


# Q14 ->>14. Write a Python program to count the number of lowercase and uppercase letters in a string.
def count_string_case(String):
    """Counts the Number of Lowercase and uppercase letters in a user inputed string."""
    lower_count = sum(1 for char in String if char.islower()) 
    """ 
    # here I use sum() and a generator expression to count lowercase letters 
    # above this line means 

    lower_count = sum(
    # return this value   for each char in String   if condition is true
        1               for char in String         if char.islower()
    )
    """
    upper_count = sum(1 for char in String if char.isupper())
    print(f"Lowercase letters: {lower_count}, Uppercase letters: {upper_count}")
    

#Q14-analysis conditions and understanding 
# lower_count = sum(1 for char in String if char.islower()) # this line works like below that code 
count = 0
String = "Mahadeb Maity"
for char in String:
    if char.islower():
        count += 1  # This "+= 1" is the same as returning 1 in the generator
lower_count = count

# Q14- Improved version of these questions in verious ways like below
def Count_print_lowercase_uppercase():
    """ You can combine both counting and collecting lowercase and uppercase characters in one line by using tuple unpacking inside a single generator expression or comprehension."""
    
    Input_String = input("Enter a string to count lowercase and uppercase letters: ")
    String = Input_String.strip()  # Remove leading and trailing whitespace
    '''    
    this is one way to do this

    lower_count, lower_characters = (
        sum(1 for char in String if char.islower()), # using generator expression to count lowercase letters
        [char for char in String if char.islower()] # using list comprehension to collect lowercase characters
    )
    upper_count, upper_characters = (
        sum(1 for char in String if char.isupper()), # same as above but for uppercase letters
        [char for char in String if char.isupper()]
    )
    print(f"Input String: {String}")
    print(f"Lowercase letters: {lower_count}, Characters: {lower_characters}")
    print(f"Uppercase letters: {upper_count}, Characters: {upper_characters}")
    '''
    '''
    # this is one way to do this

    lower_characters = [char for char in String if char.islower()]
    lower_count = len(lower_characters)
    upper_characters = [char for char in String if char.isupper()]
    upper_count = len(upper_characters)
    print(f"Input String: {String}")
    print(f"Lowercase letters: {lower_count}, Characters: {lower_characters}") 
    print(f"Uppercase letters: {upper_count}, Characters: {upper_characters}")
    '''

    # This is the best way to do this
    lower_count, lower_characters = (lambda chars: (len(chars), chars))([c for c in String if c.islower()])
    upper_count, upper_characters = (lambda chars: (len(chars), chars))([c for c in String if c.isupper()])
    print(f"Input String: {String}")
    print(f"Lowercase letters: {lower_count}, Characters: {lower_characters}")
    print(f"Uppercase letters: {upper_count}, Characters: {upper_characters}")


# Q15 ->>15. Create a function that checks if a string contains only alphabets.
def is_alphabets_string(String):
    """Checks if a string contains only alphabets."""
    if String.isalpha():
        print(f"The string '{String}' contains only alphabets.")
        return True
    else:
        print(f"The string '{String}' contains non-alphabet characters.")
        return False
    

# Q16 ->>16. Explain scope of a variable (global vs local) with examples.
def variable_scope_example():
    """Demonstrates the scope of variables in python."""
    global_variable = "I am a global variable"
    def local_scope_example():
        local_scope_example_variable = "I am a local variable"
        print(local_scope_example_variable)
        print(global_variable)
    local_scope_example()  # This will print the local variable and access the global variable
    print("inside the function, global variable is accessible:")
    print("but outside the function, local variable is not accessible:")
    print(local_scope_example) # returns garbase collection object value 



# Q17 ->>17. Write a program to find the length of a string without using len().

def String_lenth():
    """Finds the length of a string without using len()."""
    Name = input("Enter a string to find its length: ").strip()
    count = 0
    for _ in Name:
        count +=1
    print(f"The length of the '{Name}' is: {count}")


# Q18 ->>18. Write a function that accepts a string and returns it in reverse order.
def string_reverse():
    Name = " Mahadeb Maity"
    # reverse = Name[::-1]  # this is same as 
    # reverse = Name[len(Name):0:-1]
    # reverse = reversed(Name) # this will return a reverse object
    # print(f"Reverse of {Name} is : {reverse}")

    print("Reversing the string:", Name)
    print("Reversed string is: ", end='')
    for i in reversed(Name):
        print(i, end='')
    


# Q19 ->>19. What is the purpose of pass in Python? Explain with a case.def pass_example():
    """Demonstrates the use of pass in Python."""
def pass_example():
    """The pass statement is a null operation; it is used when a statement is syntactically required but you do not want any command or code to execute."""
    def empty_function():
        pass  # This function does nothing, but it is syntactically correct

    print("This function does nothing, but it is valid syntax.")
    empty_function()  # Calling the empty function


# Q20 ->>20. Write a program that prints the square of each number from 1 to 10 using a loop.
def square_numbers():
    """Prints the square of each numbers from 1 to 10 using a loop."""
    for i in range(1,11):
        square = i **2
        print(f"The square of {i} is : {square}")


#Q21 ->>21. Write a function that accepts a list and returns a new list with only even numbers.
def filter_even_numbers(numbers):
    """ Returns a new list containing only even numbers from the input list """
    return [num for num in  numbers if num % 2 == 0]

# Q22 ->>22. Create a program to count occurrences of each character in a string using dictionary.
def count_character_occurrences(string):
    """ Counts occurrences of each characer in a string using a dictionary """

    count_dict = {}
    for char in string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict


# Q23 ->>23. Write a function that checks whether a given year is a leap year.
def is_leap_year(year):
    """ Checks whether a given year is a leap year """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # return True # write anyone of these two lines
        return f"Yes, {year} is a leap year."
    else:
        # return False # write anyone of these two lines
        return f"No, {year} is not a leap year."


# Q24 ->>24. Write a program to merge two dictionaries.
def merge_dictionaries(dict1, dict2):
    """ Merges two dictionaries and returns the merged dictionary """
    merged_dict = dict1.copy()  # Create a copy of the first dictionary
    merged_dict.update(dict2)   # Update it with the second dictionary
    return merged_dict          # becuase dict is a mutable data type 

def marge_dictionaries_calling_func():
    dict1 = {"x": 1, "y": 2}
    dict2 = {"z": 3, "y": 100}

    merged_as_set = {*dict1, *dict2} # Using set to merge dictionaries, this will remove duplicate keys
    merged = {**dict1, **dict2}  # Using dictionary unpacking to merge dictionaries
    print(merged_as_set,type(merged_as_set))  # Using set to merge dictionaries, this will remove duplicate keys
    print(merged,type(merged))  # Call the function to merge dictionaries


# Q25 ->>25. What is list slicing? Show 3 slicing operations on a sample list.
# list slicing is a way to access a subset of elements from a list by specifying a start index, an end index, and an optional step value.
#syntax: list[start:end:step]
def list_slicing_operations():
    """ Demonstrates list slicing operations on a sample list """
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Slicing to get elements from index 2 to index 5 (exclusive)
    slice1 = sample_list[2:5]  # Output: [3, 4, 5]
    
    # Slicing to get every second element from the list
    slice2 = sample_list[::2]   # Output: [1, 3, 5, 7, 9]
    
    # Slicing to get the last three elements of the list
    slice3 = sample_list[-3:]   # Output: [8, 9, 10]
    
    print("Sample List:", sample_list)
    print("Slice from index 2 to 5:", slice1)
    print("Every second element:", slice2)
    print("Last three elements:", slice3)



# Q26 ->>26. Write a program to display the multiplication table of a number (1 to 10).
def multiplication_table(number,Range=10):
    """ Displays the multiplication table of a number from 1 to 10 """
    print(f"Multiplication Table of {number}:")
    for i in range(1,Range+1):
        print(f"{number} x {i} = {number * i}") 


# Q27 ->>27. Create a menu-driven program: 1. Add, 2. Subtract, 3. Exit
def menu_driven_program():
    """ A Simple menu-driven program for addition and subtraction """

    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print("Exiting the program.")
            break


# Q28 ->>28. Write a function to calculate the LCM of two numbers.
import math
def lcm(a, b):
    """ Calculates the Least Common Multiple (LCM) of two numbers """
    return abs(a * b) // math.gcd(a, b) # here abs() use becuase LCM is always positive, and abs returns the absolute value of a number ( positive value of a number )
 

# Q29 ->>29. Create a program to remove all spaces from a sentence.
def remove_spaces(sentence):
    """ Removes all spaces from a sentence """
    # return sentence.replace(" ", "")  # Using str.replace() to remove spaces
    return sentence.replace("  ","")

# Q30 ->>30. Write a Python program that checks if a number is a strong number.
def is_strong_number(number):
    """ Checks if a number is a strong number """
    original_number = number      # Keep a copy of the original number
    sum_of_factorials = 0         # To store sum of factorials of digits
    
    while number > 0:             # Repeat until all digits are processed
        digit = number % 10       # Extract last digit
        factorial = math.factorial(digit)  # Factorial of that digit
        sum_of_factorials += factorial     # Add factorial to the sum
        number //= 10             # Remove last digit (integer division by 10)
    
    # After loop ends, check condition
    if sum_of_factorials == original_number:
        return f"{original_number} is a strong number."
    else:
        return f"{original_number} is not a strong number."


#  Q31 ->>31. Write a function using lambda to square each element of a list.
def square_list_elements():
    """ Squares each element of a list using a lambda funtion """
    user_input = input("Enter a list of numbers separated by spaces: ")
    x = list(map(int, user_input.split()))  # Convert input string to a list
    square = list(map(lambda x: x**2,x))
    print(f"The square of each element in the list {x} is: {square}")  # Call the function to square each element in the list

# Q Extra question 
def Power_Number(num,power):
    def square(x): 
        return x**power

    result = map(square, num)
    # print(list(result))
    return list(result)


#32. Explain the use of map() with a program to double list elements.
def addition_two_list(list1,list2):
    add_lists = list(map(lambda x,y: x +y , list1 , list2))
    print(f"Summation of two list:\n{list1} + {list2}\n={add_lists}")



# 33. Write a program to input 5 numbers and store only unique values in a set.
def separate_duplicate():
    unique_value = input("Enter multiple number seperate by space:")
    final_value = set(map(int,unique_value.split()))
    print(sorted(final_value))
    print(type(final_value))


# 34. Write a program that accepts marks of 5 subjects and prints grade with percentage.

def student_markssheet():
    """Accept marks for N subjects (default 3) and print total, percentage and grade."""
    try:
        n_input = input("Enter how many subjects (press Enter for default 3): ").strip()
        n = int(n_input) if n_input else 3
        if n <= 0:
            print("Number of subjects must be positive, using 3.")
            n = 3
    except ValueError:
        print("Invalid number entered, using 3 subjects.")
        n = 3   # corrected: earlier you wrote n=3

    marks = {}   # dictionary to hold subject:marks
    Total_marks = int(input("Enter total marks of each subject:").strip())

    for i in range(1, n + 1):
        while True:
            subject = input(f"Enter Subject{i} name: ")
            s = input(f"Enter marks for {subject} (0-{Total_marks}): ").strip()
            try:
                m = float(s)
            except ValueError:
                print("Please enter a numeric value.")
                continue
            if 0 <= m <= Total_marks:
                marks[subject] = m   # ✅ store as {subject: marks}
                break
            else:
                print(f"Marks must be between 0 and {Total_marks}.")

    total = sum(marks.values())  # sum of all marks
    percentage = (total / (Total_marks * n))*100

    if percentage >= (Total_marks - 10):
        grade = "A+"
        Greetings = "Excellent Result"
    elif percentage >= (Total_marks - 20):
        grade = "A"
        Greetings = "Very Good Result"
    elif percentage >= (Total_marks - 30):
        grade = "B"
        Greetings = "Not Bad Result"
    elif percentage >= (Total_marks - 40):
        grade = "C"
        Greetings = "Not Expected"
    elif percentage >= (Total_marks - 50):
        grade = "D"
        Greetings = "Bad Result"
    else:
        grade = "F"
        Greetings = "You are not eligible for next class"

    print("\nMarks entered:")
    for sub, mark in marks.items():
        print(f"{sub}: {mark}")
    print(f"Total: {total:.2f} / out of {Total_marks * n}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(Greetings)


# 35. What are args and kwargs in Python? Demonstrate both.
'''
args : is a python function arbitary positional argument.  which is used for passing  multiple argument in a function using *args 
        1> args store value as a  tuple type 
        2> Name doesn't have to be args , it can be *data , *value  etc.
kwargs : is a python function arbitary key value pairs argument . which is passing multiple key with argument in a function using **kwargs
        1> kwargs store value as a dictionary type 
        2> Name doesn't have to be kwargs , it can be **keyvalue, **valuepair
'''
def func1(*addvalue):
    return f"Sum of all value are:{sum(addvalue)}"

def func2(**Info):
    for name,age in Info.items():
        print(f"Name:{name},age:{age}")


# 36. Write a function that checks whether a string is an anagram of another.

def anagram(str1,str2):
    """ 👉 **It means:**
You have to compare two strings (words). If the letters of one word can be rearranged to form the other word, then they are called **anagrams**.

### Example:

* `"listen"` and `"silent"` → ✅ Anagram
* `"triangle"` and `"integral"` → ✅ Anagram
* `"hello"` and `"world"` → ❌ Not Anagram
"""
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    print(f"{str1} == {str2}")
    return sorted(str1) == sorted(str2)

# 37. Write a program to handle ValueError using try-except block.
def handle_error():
    try:
        Divisor = int(input("Enter Divisor:"))
        Dividend =  int(input("Enter Dividend:"))
        division = Divisor / Dividend
        print(division)
    except ZeroDivisionError:
        print(f"{Divisor} is Not Divided by Zero!")

# 38. Create a tuple of 5 elements. Show how to convert it to a list and modify the third item.
def ListTuple_convertion():
    Tuple = (1,2,3,4,7)
    convert_tuple = list(Tuple)
    convert_tuple[2] = 10
    print(f"Original Tuple: {Tuple, type(Tuple)}")
    print(f"Converted Tuple: {convert_tuple, type(convert_tuple)}")

# 39. What is recursion? Write a recursive function for factorial.
def recursive_Factorial(n):
    """ Recursion: is a function which is call itself."""
    # base case 
    if n == 0 or n == 1:
        return 1
    # recursive case 
    else:
        return n * recursive_Factorial(n-1)
    

# 40. Create a function that returns True if all items in a list are of the same type.
def list_value_typecheck():
    list = [1,2,5]
    for i in list:
        if type(list[i]) == type(list[i+1]):
            return f"All list of items are {type(i)} Type"
        else:
            return f"All list of items are not {type(i)} Type"
    

def calling_func():

    print(LargeN_calling_func.__doc__)
    LargeN_calling_func()

    print(print_odd_Even_numbers.__doc__) # __doc__ is used to print the docstring of the function 
    print_odd_Even_numbers()

    print(break_continue_example.__doc__)  # Print the docstring of the function
    break_continue_example()

    print(count_string_case.__doc__)  # Print the docstring of the function
    count_string_case(String)

    print(Count_print_lowercase_uppercase.__doc__)  # Print the docstring of the function
    Count_print_lowercase_uppercase()

    print(is_alphabets_string.__doc__)
    is_alphabets_string("MahadebMaity")  # Example string containing only alphabets
    is_alphabets_string("Mahadeb Maity 123")  # Example string containing non-alphabet characters

    print(variable_scope_example.__doc__) # Call the function to demonstrate variable scope
    variable_scope_example()  # Call the function to demonstrate variable scope

    print(String_lenth.__doc__)  # Print the docstring of the function
    String_lenth() # Example string to find length without using len()

    string_reverse() 

    print(pass_example.__doc__)  # Print the docstring of the function
    pass_example()  # Call the function to demonstrate the use of pass

    print(square_numbers.__doc__)  # Print the docstring of the function
    square_numbers()  # Call the function to print squares of numbers from 1 to

    print(filter_even_numbers.__doc__)  # Print the docstring of the function
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter_even_numbers(numbers)  # Call the function to filter even numbers
    print(f"Even numbers from the list {numbers} are: {even_numbers}")  # Print the filtered even numbers

    print(count_character_occurrences.__doc__)  # Print the docstring of the function
    string = "hello world"  
    char_count = count_character_occurrences(string)  # Call the function to count character occurrences
    print(f"Character occurrences in '{string}': {char_count}")  # Print the character occurrences

    print(is_leap_year.__doc__)  # Print the docstring of the function
    year = int(input("Enter for your checking year: "))  # Example year to check for leap year
    print(f"Is {year} a leap year? {is_leap_year(year)}")  # Call the function to check if the year is a leap year 

    marge_dictionaries_calling_func()

    print(list_slicing_operations.__doc__)  # Print the docstring of the function
    list_slicing_operations()  # Call the function to demonstrate list slicing operations

    numbers = int(input("Enter a number to display its multiplication table: "))  # Example number for multiplication table
    Range = int(input("Enter the range for the multiplication table (default is 10): ")) # Default range is 10
    print(multiplication_table.__doc__)  # Print the docstring of the function
    multiplication_table(numbers,Range)  # Example number to display its multiplication table

    print(menu_driven_program.__doc__)  # Print the docstring of the function
    menu_driven_program()  # Call the function to run the menu-driven program

    print(lcm.__doc__)  # Print the docstring of the function
    a = int(input("Enter first number for LCM: "))  # Example first number
    b = int(input("Enter second number for LCM: "))  # Example second number
    print(f"The LCM of {a} and {b} is: {lcm(a, b)}")  # Call the function to calculate LCM and print the result

    print(remove_spaces.__doc__)  # Print the docstring of the function
    print(len(remove_spaces("  Hello   World!   ")))  # Print the length of the sentence after removing spaces

    print(is_strong_number.__doc__)  # Print the docstring of the function
    number = int(input("Enter a number to check if it is a strong number: "))
    print(is_strong_number(number))  # Example number to check if it is a strong number

    print(square_list_elements.__doc__)  # Print the docstring of the function
    square_list_elements()

    num = [1, 2, 3, 4,5]
    print(f"Square of a List:{Power_Number(num,2)}") # Example list to square each element using lambda function
    print(f"Cube of a List:{Power_Number(num,3)}")  # Example list to cube each element using lambda function

    N1 = [2,3,4,5,6]
    N2 = [1,2,3,4,5]
    addition_two_list(N1,N2)

    separate_duplicate()

    print(student_markssheet.__doc__)
    student_markssheet()

    print(func1(1,2,4,5,7,9,9))
    func2(Mahadeb=22, Jayanta=23)

    print(anagram.__doc__)
    print(anagram("Mahadeb","Dehamab"))

    handle_error()

    ListTuple_convertion()
    print(recursive_Factorial.__doc__)
    N = int(input("Enter The Number:"))
    print(recursive_Factorial(N))

    print(list_value_typecheck())

if __name__ == "__main__":
    calling_func()

