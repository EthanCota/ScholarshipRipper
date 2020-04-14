# Returns True if the string contains a number
def hasNumbers(string):
    for char in string:
        if(char.isdigit()):
            return True
    return False

# Returns the first two digit number in a string, or -1 if no such number exists within the string
def getTwoDigit(string):
    for i in range(0,len(string)):
        if(string[i].isdigit() and string[i+1].isdigit() and not(string[i+2].isdigit())):
            return int(string[i:i+2])
    return -1
            
#Returns the first four digit number in a string, or -1 if no such number exists within the string
def getFourDigit(string):
    for i in range(0,len(string)):
        if(string[i].isdigit() and string[i+1].isdigit() and string[i+2].isdigit() and string[i+3].isdigit() and not(string[i+4].isdigit())):
            return int(string[i:i+4])
    return -1

#Returns the index of the first instance of substring within string
def findSubstring(string, substr):
    index = 0

    if substr in string:
        char = substr[0]
        for ch in string:
            if ch == char:
                if string[index:index+len(substr)] == substr:
                    return index

            index += 1

    return -1

#Converts a string date (October 15, 2002) into a formatted date (2002/10/15)
def convertDate(string):
    MM=''
    DD=''
    
    if('Jan' in string):
        MM='01' 
    elif('Feb' in string):
        MM='02' 
    elif('Mar' in string):
        MM='03' 
    elif('Apr' in string):
        MM='04' 
    elif('May' in string):
      MM='05' 
    elif('Jun' in string):
        MM='06' 
    elif('Jul' in string):
        MM='07' 
    elif('Aug' in string):
        MM='08' 
    elif('Sep' in string):
        MM='09' 
    elif('Oct' in string):
        MM='10' 
    elif('Nov' in string):
        MM='11' 
    elif('Dec' in string):
        MM='12'
    else: return 'unknown'
    
    temp = getTwoDigit(string)
    if(temp > 0):
        DD = str(temp)
        return MM + '/' + DD
    else: return MM
