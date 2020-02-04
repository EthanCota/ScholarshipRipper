from Selenium import Webdriver

codeList = open('codes.txt','r', encoding='UTF8')

driver = webdriver.Chrome('C:\\chromedriver') #TODO correct path
driver.get('http://ultimatescholarshipbook.com')
searchBox = driver.find_element_by_name('criteria')
edition = driver.find_element_by_tag_name('select')

def ObtainData:
     code = str(codeList.readline())
  
    searchBox.sendKeys(code)
    editions = edition.find_elements_by_tag_name('option')
    for e in editions:
        if (str(e.get_attribute('value')) == "2019"):
            e.click()
    searchSubmit = driver.find_element_by_class_name('search_submit')
    searchSubmit.click()
       
    titles = driver.find_elements_by_class_name('AwardTitle')
    awardTitle = str(title[0])
    
    info = driver.find_elements_by_class_name('AwardBody')
    
def SetData:
    awardGiver = str(info[0])
    awardTarget = str(info[1])
    awardPurpose = str(info[2]) #TODO substring
    awardEligible = str(info[3])
    awardLink = info[info.len()-2]
    
    targetHighSchool = False
    targetCollege = False
    targetGraduate = False
    targetAdult = False
    
    awardNeedBased = False #TODO Add SAT and ACT info
    awardEssay = False
    awardTranscript = False
    awardStatement = False
    
    for i in info:
        if(i.startswith('Minimum')):
            awardGPA = str(i) #TODO substring
        elif(i.startswith('Amount')):
            awardAmount = str(i) #TODO substring
        elif(i.startswith('Number')):
            awardQuantity = str(i) #TODO substring
        elif(i.startswith('Deadline')):
            awardDeadline = str(i) #TODO substring
    
    if(awardEligible.contains('financial need') or awardEligible.contains('need based') or awardEligible.contains('financial aid')):
        awardNeedBased = True
    elif(awardEligible.contains('essay')):
        awardEssay = True
    elif(awardEligible.contains('transcript')):
         awardTranscript = True
    elif(awardEligible.contains('personal statement')):
        awardStatement = True
        
    if(awardTarget.contains('high')):
        targetHighSchool = True
    elif(awardTarget.contains('college')):
        targetCollege = True
    elif(awardTarget.contains('graduate')):
        targetGraduate = True
    elif(awardTarget.contains('adult')):
        targetAdult = True
        
for k in range(0, 9999) #TODO Fix 9999 value
   ObtainData()
   SetData()
    
