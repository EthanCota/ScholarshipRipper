
#Author:thefourtheye on StackOverflow
#Returns True if the input string contains a number in it
def containsnumber(string):
    return any(char.isdigit() for char in string)

#Author:Erik Fortin on StackOverflow
#Returns the index of the first instance of substring within string
def findsubstring(string, substr):#Code from Erik Fortin on StackOverflow
    index = 0

    if substr in string:
        char = substr[0]
        for ch in string:
            if ch == char:
                if string[index:index+len(substr)] == substr:
                    return index

            index += 1

    return -1
