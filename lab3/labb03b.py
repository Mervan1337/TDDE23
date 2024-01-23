
def choose(n,k):
    if (k == n or k == 0):
        return 1
    elif (k > (n-k)):
        return perm(n,k)//factorial(n-k)
    else:
        return perm(n,n-k)//factorial(k)
def factorial(n):
    if (n == 1):
        return (n)
    else: 
        return (n * factorial(n-1))
def perm(n,k):
    if (n == k):
        return (1)
    else: 
        return (n * perm(n-1,k))

#print(choose(1000,4))
print(choose(1000,800))
#print(choose(1000,999))
