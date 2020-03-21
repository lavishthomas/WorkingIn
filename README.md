# WorkingIn

## Requirement given by **Suzanne** via Mail

Please create a public repository, and write a solution for the following small coding challenge, using clean code principles, and preferable C++, Python, or Javascript as a programming language:

 - Calculate the 15th element for this sequence: 2, 2, 4, 6, 10, 16, ...? - the new element is calculated based on the last two element sum, so the next element will be 10 + 16.

 - Please create a docblock and answer the following questions:
   - What is the 15th element of the sequent?
   - What is your solution time and space complexity, regarding for the n(th) element of the sequent?
   - What clean code principles you have been used, and why?
   - Bonus: can you make your code recursive? If yes, what would be your time and space complexity?

If you are ready with your code, and comments please upload to any online repository (github, gitlab, repl.to, etc) and send only the link to us, not the code.

## Solution Details

 - The solution has programmed in both Python and Javascript programming in the following file repectively.
 - The Javascript file can be executed in NodeJS platform using the command **node .\sequence_printer.js**
 - The Python file can be executed in python3 platform using the command **python .\sequence_printer.py**
 - The 15th element of the sequence is 1220 which is printed in both programs using both loop and recursive program.

## Program details:

Both languages implement identical solutions in both languages. <br>

Two functions are provided which is implements the solution using foor loop (sequence_element_printer) 
and recursive program recursive_element_printer
### Function Details
-----------------------------------------------------------------------------------------------------
sequence_element_printer(int: n)
----------------------------------------------------------------------------------------------------- 

This function takes one input: the position of the element sequence to be printed.

The function uses a for loop which iterates for n times to calculate the 
next element based on previous two elements.

The time complexity of the function is O(n).

The space complexity of the function is O(1).
Only one element has to be kept in memory for the exection. 
Practically two variables but in theory it is represented usally as O(1).

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

## Output of the programs :
The  15 th number of the sequence using recursive function is :  122 0 <br>
The  15 th number of the sequence using loop method is :  1220 <br>
