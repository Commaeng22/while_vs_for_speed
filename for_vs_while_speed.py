# While과 For중 어떤 방식이 더 빠르게 실행이 될까에 대한 코드

import time

countlimit=input("max값을 숫자로 입력하세요 : ")
count=0
whilestarttime=time.time()
while count<int(countlimit):
    count=count+1
    print(count)
whilestoptime=time.time()    

whiletime = whilestoptime - whilestarttime

forstarttime=time.time()
for i in range(1,int(countlimit)+1):
     print(i)
forstoptime=time.time()    

fortime = forstoptime - forstarttime

print("while 구문으로 했을때 :", whiletime)
print("for 구문으로 했을때 :", fortime)

forwin = whiletime - fortime
whilewin = fortime - whiletime

if whiletime < fortime:
    print("while이 %f초 만큼 빠름" % float(whilewin)) #실수형으로 소수점아래 6자리까지 표시(%5f)
else:
    print('for가 %f초 만큼 빠름' % float(forwin))