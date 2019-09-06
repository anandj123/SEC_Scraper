import requests
import operator
import bleach

class FileLine:
    def __init__(self, CIK, Company_Name, Form_Type, Date_Filed, Filename):
        self.CIK = CIK
        self.Company_Name = Company_Name
        self.Form_Type = Form_Type
        self.Date_Filed = Date_Filed
        self.Filename = Filename


def printform(filename, count):
    url = "https://www.sec.gov/Archives/" + filename
    r = requests.get(url, allow_redirects=True)
    n = "to" + str(count) + ".html"
    #x = bleach.clean(r.content, tags=[], attributes={}, styles=[], strip=True)
    open(n, 'wb').write(r.content)
    f = open(n, 'r')
    if f.read().__contains__("odd lot"):
        return True

#Step 1: Find master.idx

url="https://www.sec.gov/Archives/edgar/full-index/"
year="2019"
qtr="2"

fullUrl = url + year + "/QTR" + qtr + "/master.idx"

r = requests.get(fullUrl, allow_redirects=True)

open('sec.txt', 'wb').write(r.content)

print("full URL: " + fullUrl + "\n")

#Step 2: find individual lines

f = open("sec.txt", "r")
flag = False
formTypes = {}
line = ""
count = 1;
while True:
    line = f.readline()
    if flag:
        info = line.split("|")
        #print info
        #fileLine = FileLine(info[0], info[1], info[2], info[3], info[4])
        if len(info) != 5:
            break
        form = info[2]
        if form in formTypes:
            formTypes[form] += 1
        else:
            formTypes[form] = 1
        if form.__contains__("SC TO") :
            filename = info[4]
            foundOdd = printform(filename, count)
            if foundOdd:
                print(count)
                count += 1

    if line[0:10] == "----------":
        flag = True

sorted_formTypes = sorted(formTypes.items(), key=operator.itemgetter(1))
print(sorted_formTypes)
