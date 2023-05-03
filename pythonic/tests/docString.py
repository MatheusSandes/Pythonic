def string_reverse(str):
    #thats an a example of docString in the functions
    #Returns the reversed String.

    #Parameters:
    #    str (str):The string which is to be reversed.

    #Returns:
    #    reverse(str):The string which gets reversed.   

    reverse_str = ''
    i = len(str)
    while i > 0:
        reverse_str += str[i - 1]
        i = i- 1
    return reverse_str