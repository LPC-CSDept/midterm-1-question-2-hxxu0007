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
    
    if(len(words[0]) <= len(words[1])):
        shortest = words[0]
        longest = words[1]
    else:
        shortest = words[1]
        longest = words[0]
    for i in range(2, len(words)):
        if(len(words[i]) > len(longest)):
            longest = words[i]
        if(len(words[i]) < len(shortest)):
            shortest = words[i]
    print(longest)
    print(shortest)
    ########################################
    # Do not delete the return statement
    ########################################
    return longest, shortest
##


if __name__ == '__main__':
    main()
