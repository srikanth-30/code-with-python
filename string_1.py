def find_longest_word(string):
    words = string.split()
    longest_word = ""
    longest_lenght = 0
    
    for word in words:
        if len(word) > longest_lenght:
            longest_word = word
            longest_lenght = len(word)
    return longest_word, longest_lenght
input_string = input("enter the string: ")
longest_word, word_length = find_longest_word(input_string)
print("THe longest word is: ",longest_word)
print("the length of the longest word is :",word_length)