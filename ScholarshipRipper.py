#TODO import a module to put information into google sheets/excel
from Selenium import Webdriver
import datetime as dt
import ethanmod as em

#Returns True if the input string contains a number in it
def containsnumber(string):
    return any(char.isdigit() for char in string)

#Returns the index of the first instance of substring within string
def findsubstring(string, substr):
    index = 0

    if substr in string:
        char = substr[0]
        for ch in string:
            if ch == char:
                if string[index:index+len(substr)] == substr:
                    return index

            index += 1

    return -1
#Opens document containing scholarship codes
codeList = open('codes.txt','r', encoding='UTF8')
#Opens ultimatescholarshipbook.com and preps site for code entry
d = webdriver.Chrome('C:\\chromedriver')
d.get('http://ultimatescholarshipbook.com')
search = d.find_element_by_name('criteria')
editions = d.find_element_by_tag_name('select').find_elements_by_tag_name('option')
submit = d.find_element_by_class_name('search_submit')

def ObtainData():
     #takes the '\n' out of the code then enters it into the site
     code = codeList.readline()
     code = code[:len(code)-1]
    search.sendKeys(code)
    for e in editions:
        if (str(e.get_attribute('value')) == "2019"):
            e.click()
    submit.click()
    
    
    
def SetData():
    #Finds the scholarship title
    titles = d.find_elements_by_class_name('AwardTitle')
    awardTitle = str(title[0])
    
    info = d.find_elements_by_class_name('AwardBody')
    #Finds the scholarship awarder
    awardGiver = info[0].text
    
    #Finds who the scholarship is for
    awardTarget = info[1].text
    #Resets all target values to False
    targetJuniorHigh = False
    targetHighSchool = False
    targetCollege = False
    targetGraduate = False
    targetAdult = False
    #Sets target true if it contains said keyword
    if(awardTarget.contains('younger')):
        targetJuniorHigh = True
    elif(awardTarget.contains('high')):
        targetHighSchool = True
    elif(awardTarget.contains('college')):
        targetCollege = True
    elif(awardTarget.contains('graduate')):
        targetGraduate = True
    elif(awardTarget.contains('adult')):
        targetAdult = True
    
    #Finds the listed purpose of the award
    awardPurpose = info[2].text[9:]
    
    #Finds the paragraph describing eligibility
    awardEligible = info[3] #TODO Add SAT and ACT info || substring
    #Resets eligiility variables to False
    isNeedBased = False 
    isEssay = False
    isTranscript = False
    isStatement = False
    #Sets eligibility variable to true if it contains said keyword
    if(awardEligible.contains('financial need') or awardEligible.contains('need based') or awardEligible.contains('financial aid')):
        isNeedBased = True
    elif(awardEligible.contains('essay')):
        isEssay = True
    elif(awardEligible.contains('transcript')):
         isTranscript = True
    elif(awardEligible.contains('personal statement')):
        isStatement = True
    #Finds up to 3 eligibility statements within the paragraph
    if(awardEligible.contains('must') and awardEligible.contains('. ')):
        req1 = awardEligible[find_str(awardEligible, 'must')+4:find_str(awardEligible, '. ')]
        awardEligible = awardEligible[find_str(awardEligible, 'must')+4:find_str(awardEligible, '. ')]
        if(awardEligible.contains('must') and awardEligible.contains('. ')):
            requirement2 = awardEligible[find_str(awardEligible, 'must')+4:find_str(awardEligible, '. ')]
            awardEligible = awardEligible[find_str(awardEligible, 'must')+4:find_str(awardEligible, '. ')]
            if(awardEligible.contains('must') and awardEligible.contains('. ')):
                requirement3 = awardEligible[find_str(awardEligible, 'must')+4:find_str(awardEligible, '. ')]
                awardEligible = awardEligible[find_str(awardEligible, 'must')+4:find_str(awardEligible, '. ')]
            else: req3 = ''
        else: req2 = ''
            req3 = ''
    else: req1 = ''
        req2 = ''
        req3 = ''
    
    #Detects if there is a required GPA and sets up proceeding variables accordingly
    j = 0
    if(info[4].text.startswith('Min'):
        awardGPA = info[4].text #TODO substring
        j+=1
    
    #Finds scholarship reward
    awardAmount = info[j+4].text
    if not (awardAmount.contains('Var')):
       awardAmount = awardAmount[find_str(awardAmount, '$')+1:find_str(awardAmount, '.')]
    else: awardAmount = 'varies'
       
    #Finds the quanitity of scholarships given
    awardQuantity = info[j+5].text
    if(hasNumbers(awardQuantity)):
       awardQuantity = awardQuantity[len(awardQuantity)-2:len(awardQuantity)]
    else: awardQuantity = 'varies'
       
    #Finds the scholarship deadline
    awardDeadline = info[j+6].text 
    if(hasNumbers(awardDeadline)):
        #Convert deadline to MM/DD/YY
    else: awardDeadline = 'varies'
       
    #Finds the hyperlink for the award
    awardLink = info[len(info)-2].text
  

for l in range(0, 2654) #TODO add main function 
   ObtainData()
   SetData()
    
