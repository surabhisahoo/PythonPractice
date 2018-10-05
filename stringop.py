str = 'X-DSPAM-Confidence: 0.8475'
p = str.find(':')
print(p)
p1 = str.find('5')
print(p1)
print(str[p:p1])