astr= str(input(""))
a1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a2=['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C']
for c in astr:
    if 'a'<=c<='z':
        num=a1.index(str.upper(c))
        print(str.lower(a2[num]),end="")
    elif 'A'<=c<='Z':
        num=a1.index(c)
        print(a2[num],end="")
    else:
        print(c,end="")
