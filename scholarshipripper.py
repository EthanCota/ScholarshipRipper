import openpyxl as px
from selenium import webdriver
from cotalib import getTwoDigit, getFourDigit, findSubstring, hasNumbers, convertDate

def main():

    #init webdriver
    driver = webdriver.Chrome('C:\\chromedriver')
    driver.get('http://ultimatescholarshipbook.com')

    #init codearray
    codelist = open('Codes.txt','r', encoding='UTF8')
    codeArray = []
    while(True):
        string = codelist.readline()
        if(len(string) < 3):
            break
        if(not string.endswith('19')):
            string = string[0:len(string)-1]
            codeArray.append(string)
        else: codeArray.append(string)
    codeArray[0] = codeArray[0][1:len(codeArray[0])]

    wb = px.Workbook()
    
    st = wb.active  
    st.title = 'Scholarships'
    st['a1'] = 'Scholarship'
    st['b1'] = 'Giver'
    st['c1'] = 'Purpose'
    st['d1'] = 'Quantity/Amount'
    st['e1'] = 'Deadline'
    st['f1'] = 'JH'
    st['g1'] = 'HS'
    st['h1'] = 'BS'
    st['i1'] = 'Grad'
    st['j1'] = 'Adult'
    st['k1'] = 'SAT'
    st['l1'] = 'ACT'
    st['m1'] = 'GPA'
    st['n1'] = 'NeedBased'
    st['o1'] = 'Essay'
    st['p1'] = 'Transcript'
    st['q1'] = 'Statement'


    for l in range(0, 2653):
            
        #init code number
        code = codeArray[l]
        
        #search for code
        search = driver.find_element_by_name('criteria')
        editions = driver.find_element_by_tag_name('select').find_elements_by_tag_name('option')
        submit = driver.find_element_by_class_name('search_submit')
        search.send_keys(code)
        for e in editions:
            if (str(e.get_attribute('value')) == "2019"):
                e.click()
        submit.click()
        
        #init award variable arrays
        titles = driver.find_elements_by_class_name('AwardTitle')
        info = driver.find_elements_by_class_name('AwardBody') 
        
        #init award variables
        try:
            awardTitle = 'Unknown'
            awardTitle = titles[0].text #Scholarship Title

            awardGiver = 'Unknown'
            awardGiver = info[0].text #Scholarship Giver
        
            awardTarget = info[1].text #Scholarship Target
            targetJuniorHigh = 'N'
            targetHighSchool = 'N'
            targetCollege = 'N'
            targetGraduate = 'N'
            targetAdult = 'N'
            if('Junior' in awardTarget): targetJuniorHigh = 'Y'
            if('High' in awardTarget): targetHighSchool = 'Y'
            if('College' in awardTarget): targetCollege = 'Y'
            if('Graduate' in awardTarget): targetGraduate = 'Y'
            if('Adult' in awardTarget): targetAdult = 'Y'
            
            awardPurpose = 'Unknown'
            awardPurpose = info[2].text[9:] #Scholarship Purpose
        
            awardEligible = info[3].text[13:]

            awardACT = 'N/A'
            awardSAT = 'N/A'
            isNeedBased = 'N'
            isEssay = 'N'
            isTranscript = 'N'
            isStatement = 'N'

            if('ACT' in awardEligible):
                awardACT = str(getTwoDigit(awardEligible)) #Minimum ACT Score
            if('SAT' in awardEligible):
                awardSAT = str(getFourDigit(awardEligible)) #Minimum SAT Score
            if('financial need' in awardEligible or 'need based' in awardEligible or 'financial aid' in awardEligible):
                isNeedBased = 'Y'
            if('essay' in awardEligible):
                isEssay = 'Y'
            if('transcript' in awardEligible):
                isTranscript = 'Y'
            if('personal statement' in awardEligible):
                isStatement = 'Y'

            awardGPA = 'N/A'
            j = 0
            if(info[4].text.startswith('Min')):
                awardGPA = info[4].text[13:] #Minimum GPA
                j+=1
        
            awardAmount = info[j+4].text #Scholarship Reward
            if not ('Var' in awardAmount or 'var' in awardAmount):
                awardAmount = awardAmount[findSubstring(awardAmount, '$')+1:findSubstring(awardAmount, '.')]
            else: awardAmount = 'varies'
        
            awardQuantity = info[j+5].text #Scholarship Quantity
            if(hasNumbers(awardQuantity)):
                awardQuantity = awardQuantity[len(awardQuantity)-2:len(awardQuantity)-1]
            else: awardQuantity = ''
        
            awardDeadline = info[j+6].text #Scholarship Deadline
            if(hasNumbers(awardDeadline)):
                awardDeadline = str(convertDate(awardDeadline))
            else: awardDeadline = 'varies'
        
            awardLink = 'about:blank'
            awardLink = info[len(info)-2].text #Scholarship Link

            ll = l + 1

            a = 'a' + str(ll)
            b = 'b' + str(ll)
            c = 'c' + str(ll)
            d = 'd' + str(ll)
            e = 'e' + str(ll)
            f = 'f' + str(ll)
            g = 'g' + str(ll)
            h = 'h' + str(ll)
            i = 'i' + str(ll)
            j = 'j' + str(ll)
            k = 'k' + str(ll)
            l = 'l' + str(ll)
            m = 'm' + str(ll)
            n = 'n' + str(ll)
            o = 'o' + str(ll)
            p = 'p' + str(ll)
            q = 'q' + str(ll)
            
            st[a] = '=HYPERLINK(' + '\"' + awardLink + '\",\"' + awardTitle + '\")'
            st[b] = awardGiver
            st[c] = awardPurpose
            if(awardQuantity == ''): st[d] = awardAmount
            elif(awardQuantity == awardAmount): st[d] = awardAmont
            else: st[d] = awardQuantity + ' x ' + awardAmount
            st[e] = awardDeadline
            st[f] = targetJuniorHigh
            st[g] = targetHighSchool
            st[h] = targetCollege
            st[i] = targetGraduate
            st[j] = targetAdult
            st[k] = awardSAT
            st[l] = awardACT
            st[m] = awardGPA
            st[n] = isNeedBased
            st[o] = isEssay
            st[p] = isTranscript
            st[q] = isStatement

            wb.save('scholarships.xlsx')
            
        except IndexError:
            print('SCHOLARSHIP NOT FOUND EXCEPTION (OR OTHER ERR)')
        print(l)
    wb.save('scholarships.xlsx')
    print('Done!')

if __name__ == '__main__':
       main()
       