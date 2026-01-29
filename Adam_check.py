n=int(input("Enter any number:"))
def isAdam(n):
  return square(n)==reverse(square(reverse(n)))
print(isAdam(12))
