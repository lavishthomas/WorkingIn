'''
The program can be executed in any python3 platform by calling the command:
python .\sequence_printer.py
'''

'''
-----------------------------------------------------------------------------------------------------
sequence_element_printer(int: n)
-----------------------------------------------------------------------------------------------------
This function takes one input: the position of the element sequence to be printed.

The function uses a for loop which iterates for n times to calculate the next 
element based on previous two elements.

The time complexity of the function is O(n).

The space complexity of the function is O(1).
Only one element has to be kept in memory for the exection. 
Practically two variables but in theory it is represented usally as O(1)
-----------------------------------------------------------------------------------------------------
'''
def sequence_element_printer(n):
    previous_element = 0
    current_element = 2

    for i in range(1, n):
        current_element = current_element + previous_element
        previous_element = current_element - previous_element
        #print ( i , ' : ', current_element)
    return current_element

'''
-----------------------------------------------------------------------------------------------------
recursive_element_printer(int: n, int: current_element (optional),int: previous_number (optional) )
-----------------------------------------------------------------------------------------------------
This function takes one mandatory input and two optional inputs: 
    1) The position of the element sequence to be printed.
    2) Current element in the sequence
    3) Previous element in the sequence

The function is executed recursively till the element to be found is calculated 
which in-returns the last element at the end to the external consumer of the function.

The time complexity of the function is O(n).

The space complexity of the function is O(n).
Because of the function pointer stack for the nested execution; 
variable current_element is kept in memory for each call till the recursive call is executed.

-----------------------------------------------------------------------------------------------------
'''
def recursive_element_printer(n, current_element=2, previous_number=0):
    n -= 1
    if (n > 0):
        # print(current_element)
        current_element = recursive_element_printer(
            n, current_element+previous_number, current_element)

    return current_element
'''
This is the execution start point of the program. 
A variable n is set as 15 (as per requirement). 
Both function are called to find the 15th element in the sequene. 

Output is :

The  15 th number of the sequence using recursive function is :  1220
The  15 th number of the sequence using loop method is :  1220
'''
n=15
number = sequence_element_printer(n)
print('The', n, 'th number of the sequence using loop method is :', number)
number = recursive_element_printer(n)
print('The', n, 'th number of the sequence using recursive function is :', number)
