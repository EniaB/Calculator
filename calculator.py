#This Repo is for my calculator project in fulfilment of Week 8 of The Skills Network Level 3 Software development Skills Bootcamp.

print("Select a function to perform:")

while True:

  print("Enter 1 for Addition")
  print("Enter 2 for Subtraction")
  print("Enter 3 for Multiplication")
  print("Enter 4 for Division")
  print("")

  function = input()

  if function == "1":
    print("Addition")
  elif function == "2":
    print("Subtration")
  elif function == "3":
    print("Multiplication")
  elif function == "4":
    print("Division")
  else:
    print("Invalid entry")
    print("\nSelect a function to perform within the 4 options available:")
    continue

  num1 = input("\nEnter first number: ")
  num2 = input("Enter second number: ")

  if function == "1":
    print("\nThe sum is " + str(int(num1) + int(num2)))
  elif function == "2":
    print("\nThe difference is " + str(int(num1) - int(num2)))
  elif function == "3":
    print("\nThe product is " + str(int(num1) * int(num2)))
  elif function == "4":
    print("\nThe quotient is " + str(int(num1) / int(num2)))
  else:
    print("\nInvalid entry")

  print("\nDo you want to continue? Yes/No")
  n = str(input())
  print("\n")
  if n == "Yes".lower():
    continue #Function call to use calculator again
  if n == "No".lower():
    break  #Function call to to end programme
