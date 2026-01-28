### Finding the reverse of a given number
n=int(input("Enter a number:"))

def Rev(n):
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
res=Rev(n)
print(f"Reverse is: {res}")

def ispalindrome(n):
    return n==Rev(n)
print(ispalindrome(n))
