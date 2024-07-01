def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    i = 0
    longest = shortest = ''
    words = []
    while True:
        word = input("Enter a word-at least 2 words(type 'stop' to finish.):")
        if(word.lower() == 'stop'):
            break
        words.append(word) 
    
    if(len(words[0]) <= len(word[1])):
        shortest = word[0]
        longest = word[1]
    else:
        shortest = word[1]
        longest = word[0]
    for i in range()

    ########################################
    # Do not delete the return statement
    ########################################
    return longest, shortest
##


if __name__ == '__main__':
    main()
