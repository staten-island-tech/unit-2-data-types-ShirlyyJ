"#1 challenge"
""" sentence = input("input a sentence")
count = sentence.split(' ')
print(len(count)) """

"python mad libs"
verb1 = input("Enter a verb")
verb2 = input("Enter another verb")
noun = input("Enter a noun")
number = input("Enter a number")
celebrity = input("Enter a celebrity name")

madlib = f"One day {celebrity} {verb1} to the park. That was went {celebrity} came across a {noun} in the middle of the path. They called {number} of their friends to help {verb2} over the {noun} to get pass. "
print(madlib)

"#2 challenge"
""" number = int(input("input a number"))
if number % 2 == 0:
    print('even')
else:
    print('not even') """

"#3 challenge"
""" bill = float(input("Enter bill"))
service = input("How was the service? (bad, okay, good, great)")

if service == "bad":
    tip_percentage = 0
elif service == "okay":
    tip_percentage = 15
elif service == "good":
    tip_percentage = 20
elif service == "great":
    tip_percentage = 25

tip = bill * (tip_percentage / 100)
total_amount = bill + tip

total = f"Service was {service}. The tip amount should be ${tip}, making the total ${total_amount}."
print(total) """

"#4 challenge"
""" number = int(input("Enter a number to find it's factors"))
factor = []

for i in range(1, number + 1):
      if number % i == 0:
          factor.append(i)

print(f"The factors of {number} are {factor}") """

"#5 challenge"
""" a = int(input("Enter a integer"))
b = int(input("Enter another integer"))
gcf = 1
for i in range(1, a+1):
            if a % i == 0 and b % i == 0: 
                    gcf = i
print(f"The greatest common factor of {a} and {b} is {gcf}") """