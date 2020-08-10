def print_upper_words(words):
    """Print out each word on seperate lines in uppercase

        >>> print_upper_words(['Programming', 'is', 'pretty', 'fun'])
        PROGRAMMING
        IS
        PRETTY
        FUN
    """
    for word in words:
        print(word.upper())

def print_other_words(words):
    """Print each word on seperate line, uppercased, if starts with e or E.

        >>> print_other_words(['eagle', 'Edward', 'Alfred'])
        EAGLE
        EDWARD
    """

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

def print_others(words, start_with):
    """Print each word on separate line, uppercased, if starts with one of given

        >>> print_others(['eagle', 'Edward', 'Alfred', 'zope'], start_with=['A', 'E'])
        EDWARD
        ALFRED
    """

    for word in words:
        if word.startswith(letter):
            print(word.upper())
            break