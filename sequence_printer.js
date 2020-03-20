n = 15

const sequence_element_printer = async (n) => {
    previous_element = 0
    current_element = 2
    for (count = 1; count < n; count++) {
        current_element = current_element + previous_element
        previous_element = current_element - previous_element
        // console.log(current_element);
    }
    return current_element
}

sequence_element_printer(n).then(number => {
    console.log('The ', n, 'th number of the sequence is : ', number)
})

var recursive_element_printer = function (n, current_element = 2, previous_number = 0) {
    n--
    console.log(n)
    if (n > 0) {
        current_element = recursive_element_printer(n, current_element + previous_number, current_element);
    }
    return current_element
};
console.log('The ', n, 'th number of the sequence is : ', recursive_element_printer(n))

