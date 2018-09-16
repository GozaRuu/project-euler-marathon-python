#!/usr/bin/env python


#generle solution out of scope even for HackerRank, tedious to write too
def n2words(n):
    if n==0: return 'Zero'
    units = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    teens = ['','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen', \
             'Seventeen','Eighteen','Nineteen']
    tens = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy', \
            'Eighty','Ninety']
    thousands = ['','Thousand','Million','Billion','Trillion','Quadrillion']
    words = []
    number = map(''.join, zip(*[iter(str(n).zfill(18))]*3))
    for nx, g in enumerate(number, 1):
        if g=='000': continue
        h,t,u = map(int, g)
        if h>0: words+= [units[h], 'Hundred']
        if t==1:
            words+= [teens[u]] if u>0 else [tens[t]]
        else:
            if t>0: words+= [tens[t]]
            if u>0: words+= [units[u]]
        words+= [thousands[6-nx]]
    return ''.join(words)
    #return ' '.join(words) return the space for the HackerRank solution

n = 1000 ; res = 0
for i in xrange(1,n+1):
    res += len(n2words(i))
print res + 3*891 #add the number of times the word 'and' aprears

def HackRank():
    t = int(raw_input().strip())
    for _ in xrange(t):
        n= int(raw_input().strip())
        print n2words(n)
