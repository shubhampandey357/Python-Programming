# To find whether the given input is palimdrome or not.
def palindrome(n):
  a=n
  rev=0
  while(a>0):
    lv=a%10
    rev=(rev*10)+lv
    a=a//10
  if(n==rev):
    print("palindrome")
  else:
    print("not palindrome")
n=int(input("enter the value"))
palindrome(n)