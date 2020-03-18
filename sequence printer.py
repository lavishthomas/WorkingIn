def sequence_element_printer(n):
    previous_element = 0
    current_element = 2 
    
    for i in range (1, n):
        #print (current_element) 
        current_element = current_element + previous_element 
        previous_element = current_element - previous_element
    return current_element 


n = 3
number = sequence_element_printer(n)
print (number)


def recursive_element_printer(n, current_number = 2 ):    
    if (n > 0 ):
        print(n)
        n -= 1
        current_number = recursive_element_printer(n,current_number )
        #print(current_number)
    else :
        return current_number        
     

n = 3
number = recursive_element_printer(n)
print (number)    
