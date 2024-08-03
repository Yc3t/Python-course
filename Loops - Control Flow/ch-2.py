n = int(input())

og = n
count = 0
r= 0
rev = 0
while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 +r

if(og == rev):
    print("its a palindrome")
else:
    print("it's not a palindrome")