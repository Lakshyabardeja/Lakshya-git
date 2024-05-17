
last_digit = 0
number = int(input("type number"))
last_digit = number % 10
if  (last_digit % 3 == 0) :
  print(f"the last digit of {number} which is {last_digit} is divisible by 3")
else:
  print(f"the last digit of {number} which is {last_digit} is not divisible by 3")
