from Selenium import Webdriver  #figure out how to create my own module
import datetime as dt
import ethanmod as em

codeList = open('codes.txt','r', encoding='UTF8')

d = webdriver.Chrome('C:\\chromedriver')
d.get('http://ultimatescholarshipbook.com')
search = d.find_element_by_name('criteria')
editions = d.find_element_by_tag_name('select').find_elements_by_tag_name('option')
submit = d.find_element_by_class_name('search_submit')

def ObtainData():
     code = codeList.readline()
     code = code[:len(code)-1]
  
    search.sendKeys(code)
    
    for e in editions:
        if (str(e.get_attribute('value')) == "2019"):
            e.click()
    
    submit.click()
       
    titles = d.find_elements_by_class_name('AwardTitle')
    awardTitle = str(title[0])
    
    info = d.find_elements_by_class_name('AwardBody')
    
def SetData():
    awardGiver = info[0].text
    
    
    awardTarget = info[1].text
    
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
    
    
    awardPurpose = info[2].text[9:]
    
    
    awardEligible = info[3] #TODO Add SAT and ACT info || substring
    
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
        awardGPA = info[4].text #TODO substring
        j+=1
    
       
    awardAmount = info[k+4].text
    
    if not (awardAmount.contains('Var')):
       awardAmount = awardAmount[find_str(awardAmount, '$')+1:find_str(awardAmount, '.')]
    else: awardAmount = 'varies'
       
       
    awardQuantity = info[k+5].text
    if(hasNumbers(awardQuantity)):
       awardQuantity = awardQuantity[len(awardQuantity)-2:len(awardQuantity)]
    else: awardQuantity = 'varies'
       
       
    awardDeadline = info[k+6].text #TODO figure out how to use the DateTime module
    if(hasNumbers(awardDeadline)):
        
    else: awardDeadline = 'varies'
       
       
    awardLink = info[len(info)-2].text
  

for l in range(0, 2654)
   ObtainData()
   SetData()
    
