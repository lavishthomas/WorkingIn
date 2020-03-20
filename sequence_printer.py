n = 15


def sequence_element_printer(n):
    previous_element = 0
    current_element = 2

    for i in range(1, n):
        current_element = current_element + previous_element
        previous_element = current_element - previous_element
        #print ( i , ' : ', current_element)
    return current_element


number = sequence_element_printer(n)
print('The', n, 'th number of the sequence using loop method is :', number)


def recursive_element_printer(n, current_element=2, previous_number=0):
    n -= 1
    if (n > 0):
        # print(current_element)
        current_element = recursive_element_printer(
            n, current_element+previous_number, current_element)

    return current_element


number = recursive_element_printer(n)
print('The', n, 'th number of the sequence using recursive function is :', number)
