from datetime import datetime.date

#Returns the first two digit number in a string, or -1 if no such number exists within the string
def getTwoDigit(string):
    for i in range(0,len(string)):
        if(string[i].isdigit() && string[i+1].isdigit()&&!(string[i+2].isdigit())):
            return int(string[i:i+2])
    return -1
            
#Returns the first four digit number in a string, or -1 if no such number exists within the string
def getFourDigit(string):
    for i in range(0,len(string)):
        if(string[i].isdigit() && string[i+1].isdigit() && string[i+2].isdigit() && string[i+3].isdigit() && !(string[i+4].isdigit())):
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

#Converts a string date (October 15, 2002) into a date object (2002/10/15)
def convertDate(string):
    MM='00'
    DD='00'
    YY='00'
    
    if('jan' in string):
        MM='01' 
    elif('feb' in string):
        MM='02' 
    elif('mar' in string):
        MM='03' 
    elif('apr' in string):
        MM='04' 
    elif('may' in string):
      MM='05' 
    elif('jun' in string):
        MM='06' 
    elif('jul' in string):
        MM='07' 
    elif('aug' in string):
        MM='08' 
    elif('sep' in string):
        MM='09' 
    elif('oct' in string):
        MM='10' 
    elif('nov' in string):
        MM='11' 
    elif('dec' in string):
        MM='12'
    
    temp = getTwoDigit(string)
    if(temp > 0):
        DD = str(temp)
    
    temp = getFourDigit(string)
    if(temp > 0):
        YY = str(temp)
        
    date = date(YY, MM, DD)
    return date
