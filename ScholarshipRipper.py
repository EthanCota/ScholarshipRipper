#TODO import gspead?
from Selenium import Webdriver as wd
import datetime as dt
import cotaLib as cl

def PrepScholar(): #Opens ultimatescholarshipbook.com and preps site for code entry
    codeList = open('codes.txt','r', encoding='UTF8')
    d = wd.Chrome('C:\\chromedriver')
    d.get('http://ultimatescholarshipbook.com')
    search = d.find_element_by_name('criteria')
    editions = d.find_element_by_tag_name('select').find_elements_by_tag_name('option')
    submit = d.find_element_by_class_name('search_submit')

def ObtainScholar(): #Enters a code into the site
     code = codeList.readline()
     code = code[:len(code)-1]
    search.sendKeys(code)
    for e in editions:
        if (str(e.get_attribute('value')) == "2019"):
            e.click()
    submit.click()
    
def SetData(): #Scrapes site to collect scholarship info
    titles = d.find_elements_by_class_name('AwardTitle')
    info = d.find_elements_by_class_name('AwardBody') 
    
    awardTitle = title[0].txt #Scholarship Title
    
    awardGiver = info[0].text #Scholarship Giver
    
    awardTarget = info[1].text #Scholarship Target
    targetJuniorHigh = False
    targetHighSchool = False
    targetCollege = False
    targetGraduate = False
    targetAdult = False
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
    
    awardPurpose = info[2].text[9:] #Scholarship Purpose
    
    awardEligible = info[3] #TODO Add SAT and ACT info || substring #Scholarship Eligibility (Need-based, essay, etc.)
    isNeedBased = False 
    isEssay = False
    isTranscript = False
    isStatement = False
    if(awardEligible.contains('financial need') or awardEligible.contains('need based') or awardEligible.contains('financial aid')):
        isNeedBased = True
    elif(awardEligible.contains('essay')):
        isEssay = True
    elif(awardEligible.contains('transcript')):
         isTranscript = True
    elif(awardEligible.contains('personal statement')):
        isStatement = True
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
    
    j = 0
    if(info[4].text.startswith('Min'):
        awardGPA = info[4].text #TODO substring #Scholarship GPA Requirement
        j+=1
    
    awardAmount = info[j+4].text #Scholarship Reward
    if not (awardAmount.contains('Var')):
       awardAmount = awardAmount[find_str(awardAmount, '$')+1:find_str(awardAmount, '.')]
    else: awardAmount = 'varies'
       
    awardQuantity = info[j+5].text #Scholarship Quantity
    if(hasNumbers(awardQuantity)):
       awardQuantity = awardQuantity[len(awardQuantity)-2:len(awardQuantity)]
    else: awardQuantity = 'varies'
       
    awardDeadline = info[j+6].text #Scholarship Deadline
    if(hasNumbers(awardDeadline)):
        #TODO: Convert deadline to MM/DD/YY
    else: awardDeadline = 'varies'
       
    awardLink = info[len(info)-2].text #Scholarship Link
 
def main():
    for l in range(0, 2654) #TODO add main function 
        ObtainData()
        SetData()

if __name__ == '__main__':
       main()
