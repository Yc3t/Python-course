print("numbers")
n = int(input())
sum1 = 0
sum2 = 0 
while n>0:
    n1 = int(input())
    n -=1
    if n1 > 0:
        sum1 += n1
    else: 
        sum2 += n1

print(sum1)
print(sum2)

