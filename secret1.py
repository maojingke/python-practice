astr= str(input(""))
a1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a2=['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C']
a1str=str.upper(astr)
for c in a1str:
    if c in a1: 
        num=a1.index(c)
        print(str.lower(a2[num]),end="")
    else:
        print(c,end="")
