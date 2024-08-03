""" # check if mark is withn range 0-100
print("Enter mark")

mark = int(input())

if (mark >= 0 and mark <= 100):
    print("The mark is within range")
else:
    print("The mark is not within range")
 """
""" # check if a person is a male or female

gender = input().lower()

if (gender == "m"): 
    print("male")
elif (gender == "f"):
    print("female")
else:
    print("error")
 """
# check if person is eligible to work

age = int(input())
if (age >= 18 and age <= 60):
        print("valid")
else:
        print("invalid")    