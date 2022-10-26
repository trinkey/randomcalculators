ans = 0
yn = 1
m = 0
go_ = 1
import math
while go_ == 1:
  try:
    # asks what operation to do
    action = input("""What action do you wanna do?
1: Additon
2: Subtraction
3: Multiplication
4: Division
5: Division with Remainder
6: Exponent (Power of)
7: Round
8: Square root
Type the number of the action here:""").lower()
    print("")
    
    # if addition
    if action == "1" or action == "+" or action == "addition" or action == "a" or action == "add":
      m = 1
      
      # asks the numbers
      num1 = input("""What is the first number you would like to add?
Input here:""").lower()
      num2 = input("""What is the second number you would like to add?
Input here:""").lower()
      print("")
      
      # logic that tells if there is an "ans"
      if num1 == "ans":
        if num2 == "ans":
          ans = ans + ans
        else:
          ans = ans + float(num2)
      else:
        if num2 == "ans":
          ans = float(num1) + ans
        else:
          ans = float(num1) + float(num2)
    
    # if subtraction
    elif action == "2" or action == "-" or action == "subtraction" or action == "s" or action == "subtract":
      m = 1
      
      # asks the numbers
      num1 = input("""What is the number that you would like to subtract from?
Input here:""")
      num2 = input("""What is the number that you would like to subtract from the first number?
Input here:""")
      print("")
      
      # logic that tells if there is an "ans"
      if num1 == "ans":
        if num2 == "ans":
          ans = ans - ans
        else:
          ans = ans - float(num2)
      else:
        if num2 == "ans":
          ans = float(num1) - ans
        else:
          ans = float(num1) - float(num2)
    
    # if multiplication
    elif action == "3" or action == "*" or action == "m" or action == "multiplication" or action == "multiply":
      m = 1
      
      # asks the numbers
      num1 = input("""What is the first number that you would like to multiply?
Input here:""")
      num2 = input("""What is the second number that you would like to multiply?
Input here:""")
      print("")
      
      # logic that tells if there is an "ans"
      if num1 == "ans":
        if num2 == "ans":
          ans = ans * ans
        else:
          ans = ans * float(num2)
      else:
        if num2 == "ans":
          ans = float(num1) * ans
        else:
          ans = float(num1) * float(num2)
    
    # if division
    elif action == "4" or action == "d" or action == "division" or action == "divide" or action == "/":
      m = 1
      
      # asks the numbers
      num1 = input("""What is the number you want to divide from?
Input here:""")
      num2 = input("""What is the number you want to divide?
Input here:""")
      print("")
      
      # logic that tells if there is an "ans"
      if num1 == "ans":
        if num2 == "ans":
          ans = ans / ans
        else:
          ans = ans / float(num2)
      else:
        if num2 == "ans":
          ans = float(num1) / ans
        else:
          ans = float(num1) / float(num2)
    
    # if division with remainder
    elif action == "5" or action == "division with remainder" or action == "dwr" or action == "dr":
      m = 1
      
      # asks the numbers
      num1 = input("""What is the number you want to divide from?
Input here:""")
      num2 = input("""What is the number you want to divide?
Input here:""")
      print("")
      
      # logic that tells if there is an "ans"
      if num1 == "ans":
        if num2 == "ans":
          r = float(ans) % float(ans)
          d = math.floor(float(ans) / float(ans))
          ans = str(int(d)) + " Remainder " + str(int(r))
        else:
          r = float(ans) % float(num2)
          d = math.floor(float(ans) / float(num2))
          ans = str(int(d)) + " Remainder " + str(int(r))
      else:
        if num2 == "ans":
          r = float(num1) % float(ans)
          d = math.floor(float(num1) / float(ans))
          ans = str(int(d)) + " Remainder " + str(int(r))
        else:
          r = float(num1) % float(num2)
          d = math.floor(float(num1) / float(num2))
          ans = str(int(d)) + " Remainder " + str(int(r))
    
    # if exponent
    elif action == "6" or action == "e" or action == "exponent" or action == "**" or action == "^":
      m = 1
      
      # asks the numbers
      num1 = input("""What is the first number?
Input here:""")
      num2 = input("""What is the number you want to put to the power of?
Input here:""")
      print("")
      
      # logic that tells if there is an "ans"
      if num1 == "ans":
        if num2 == "ans":
          ans = ans ** ans
        else:
          ans = ans ** float(num2)
      else:
        if num2 == "ans":
          ans = float(num1) ** ans
        else:
          ans = float(num1) ** float(num2)
    
    # if round
    elif action == "7" or action == "round" or action == "r":
      m = 1
      
      # asks the number
      num1 = input("""what is the number you want to round?
Input here:""")
      print("")
      
      # logic that tells if there is an "ans"
      if num1 == "ans":
        ans = round(ans)
      else:
        ans = round(float(num1))
    
    # if square root
    elif action == "8" or action == "sqrt" or action == "square root" or action == "-/" or action == "sr":
      m = 1
      
      # asks the number
      num1 = input("""what is the number you want to get the square root of?
Input here:""")
      print("")
      
      # logic that tells if there is an "ans"
      if num1 == "ans":
        ans = math.sqrt(ans)
      else:
        ans = math.sqrt(float(num1))
    
    # if hi
    elif action == "hi":
      print("")
      print("""==========
| HELLO! |
==========""")
      print("")
    
    # if invalid input
    else:
      print("")
      print("Your input is invalid, please try again.")
      print("")
      yn = 0
    
    # prints the answer
    if yn == 1:
      print(ans)
    
    # asks if you want to do another calculation
    if m == 1:
      m = 0
      a = input("""Would you like to do another calculation?
If so, type anything. If not, then type \"n\"
Input here:""").lower()
      
      # message if not going again
      if a == "n" or a == "no" or a == "stop" or a == "done":
        go_ = 0
        print("")
        print("Thanks for using this epic calculator!")
    
    print("")
  
  #reset variable
    yn = 1
  except:
    for i in range(50):
      print("")
    print("epic error moment")
    print("")
# nice you found the easter egg good job you're epic