def f(n):
             if n==1 or n==2:
                          return 1
             else:
                          return f(n-1)+f(n-2)
a=int(input("求斐波那契数列的第几项："))
print("斐波那契数列的第{}项为{}".format(a,f(a)))
