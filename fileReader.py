#Used to initialize the list of scholarship codes from a text file.
f = open('TheUltimateScholarshipBook2019.txt','r')
g = open('ScholarshipCodes.txt','w') 

while True:
    x = f.readline()

    if not x: break
    if x.startswith("Exclusive:"):
        print >> g, x
        print("Printed" + x)
