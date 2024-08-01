""" print("Choose 2 numbers")

n1 = int(input())
n2 = int(input())

# difference between 2 numbers
if(n1-n2 > 0):
    print(n1-n2)
else:
    print(n2-n1)
 """
""" # number is even or odd
print("Choose a number to check parity")
n3 = int(input())

if(n3 % 2 == 0):
    print(n3 ,"is even")

else:

    print(n3 , "is odd")

 """
print("Choose an age to check if its eligible to vote")

number = int(input())

if(number >= 18):
    print("You can vote")
else:
    print("You cannot vote")
