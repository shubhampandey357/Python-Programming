# To find whether a number is perfect square or not.
def perfect_square(n):
  c=int((n**0.5))
  if(c**2==n):
    print("perfect square")
  else:
    print("not perfect square")
n=int(input("enter the value"))
perfect_square(n)