'''
data=[['dhoni',20,40,'2021-04-05','N'],['krishna',30,69,'2021-04-05','N'],
      ['dhoni',56,67,'2021-04-09','O'],['kohli',20,40,'2021-04-09','N'],
      ['krishna',37,65,'2021-04-09','N'],['dhoni',72,94,'2021-04-15','N'],
      ['krishna',20,61,'2021-04-15','O'],['kohli',56,67,'2021-04-15','O'],
      ['dhoni',20,40,'2021-05-05','O'],['krishna',30,69,'2021-05-05','O'],
      ['dhoni',56,67,'2021-05-09','N'],['kohli',20,40,'2021-05-09','O'],
      ['krishna',37,65,'2021-05-09','O'],['dhoni',72,94,'2021-05-15','N'],
      ['krishna',20,61,'2021-05-15','O'],['kohli',56,67,'2021-05-15','O']]
        total runs of each player / No.of times OUT

'''

data=[['dhoni',20,40,'2021-04-05','N'],['krishna',30,69,'2021-04-05','N'],
      ['dhoni',56,67,'2021-04-09','N'],['kohli',20,40,'2021-04-09','N'],
      ['krishna',37,65,'2021-04-09','N'],['dhoni',72,94,'2021-04-15','N'],
      ['krishna',20,61,'2021-04-15','N'],['kohli',56,67,'2021-04-15','N'],
      ['dhoni',20,40,'2021-05-05','N'],['krishna',30,69,'2021-05-05','N'],
      ['dhoni',56,67,'2021-05-09','N'],['kohli',20,40,'2021-05-09','N'],
      ['krishna',37,65,'2021-05-09','N'],['dhoni',72,94,'2021-05-15','N'],
      ['krishna',20,61,'2021-05-15','N'],['kohli',56,67,'2021-05-15','N']]
d1={}#score
d2={}#balls
d3={}#our ot not
for i in data:
    if i[0] not in d1:
        d1[i[0]]=i[2]
    else:
        d1[i[0]]+=i[2]
for i in data:
    if i[0] not in d2:
        d2[i[0]]=i[1]
    else:
        d2[i[0]]+=i[1]
for i in data:
    if i[0] not in d3:
        d3[i[0]]=0
    if i[4]=='O':
        d3[i[0]]+=1

for i in d1:
    score=d1[i]
    no_out=d3[i]
    balls=d2[i]
    try:
        avg1=score/no_out
    except Exception as x:
        avg1=x
    avg2=score/balls
    print([i,avg1,avg2])







