def sequence_element_printer(n):
    previous_element = 0
    current_element = 2 
    
    for i in range (1, n+1):        
        current_element = current_element + previous_element 
        previous_element = current_element - previous_element
        #print ( i , ' : ', current_element) 
    return current_element 


n = 15
number = sequence_element_printer(n)
print ( 'The ' , n , 'th number of the sequence is : ', number)


def recursive_element_printer(n, current_number = 2, previous_number = 0 ):
    if (n > 0 ):
        #print(current_number)
        n -= 1
        current_number = recursive_element_printer(n, current_number+previous_number, current_number)
        #print(current_number)
   
    return current_number        
     
n = 15
number = recursive_element_printer(n)
print ( 'The ' , n , 'th number of the sequence is : ', number)
