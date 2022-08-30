#Most repeated letter in string
s='ENGINEERING'
d={i:s.count(i) for i in s}
m=max(d.values())
for j in d:
    if d[j]==m:
        print(j)

#Most repeated word in given sentance
s='''Literature written in the English language includes many countries such as the United Kingdom and its crown dependencies, Republic of Ireland, the United States, and the countries of the former British Empire. The English language has developed over the course of more than 1,400 years.[1] The earliest forms of English, a set of Anglo-Frisian dialects brought to Great Britain by Anglo-Saxon invaders in the fifth century, are called Old English. Beowulf is the most famous work in Old English, and has achieved national epic status in England, despite being set in Scandinavia. However, following the Norman conquest of England in 1066, the written form of the Anglo-Saxon language became less common. Under the influence of the new aristocracy, French became the standard language of courts, parliament, and polite society.[2] The English spoken after the Normans came is known as Middle English. This form of English lasted until the 1470s, when the Chancery Standard (late Middle English), a London-based form of English, became widespread. Geoffrey Chaucer (1343 – 1400), author of The Canterbury Tales, was a significant figure in the development of the legitimacy of vernacular Middle English at a time when the dominant literary languages in England were still French and Latin'''
s=s.split()
d={i:s.count(i) for i in s}
m=max(d.values())
for j in d:
    if d[j]==m:
        print(j)


#lenthiest word in given sentance
s='''Literature written in the English language includes many countries such as the United Kingdom and its crown dependencies, Republic of Ireland, the United States, and the countries of the former British Empire. The English language has developed over the course of more than 1,400 years.[1] The earliest forms of English, a set of Anglo-Frisian dialects brought to Great Britain by Anglo-Saxon invaders in the fifth century, are called Old English. Beowulf is the most famous work in Old English, and has achieved national epic status in England, despite being set in Scandinavia. However, following the Norman conquest of England in 1066, the written form of the Anglo-Saxon language became less common. Under the influence of the new aristocracy, French became the standard language of courts, parliament, and polite society.[2] The English spoken after the Normans came is known as Middle English. This form of English lasted until the 1470s, when the Chancery Standard (late Middle English), a London-based form of English, became widespread. Geoffrey Chaucer (1343 – 1400), author of The Canterbury Tales, was a significant figure in the development of the legitimacy of vernacular Middle English at a time when the dominant literary languages in England were still French and Latin'''
s=s.split()
d={i:len(i) for i in s}
m=max(d.values())
for j in d:
    if d[j]==m:
        print(j)
