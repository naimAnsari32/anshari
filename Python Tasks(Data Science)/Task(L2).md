# Task : `if` statement:

1. **Basic Condition Check**
  - Write an `if` statement that checks if a given number `num` is positive. If it is, print `"The number is positive"`.
Ans: 
num=input("Enter a number")
num=int(num)
if num>0:
   print("The number is positive")
else:
   print("The number is negative")

2. **Even or Odd Check**
   - Write a Python program that checks if a number `n` is even or odd. Use an `if` statement to print `"Even"` if the number is even and `"Odd"` if it is odd.
Ans: n=input("Enter a number")
n=int(n)
if n%2==0:
   print("The number is even")
else:
   print("The number is odd")

3. **Pass or Fail**
   - Create a program that checks a student's score and prints `"Pass"` if the score is 40 or above. If the score is below 40, print `"Fail"`.
Ans: p=input("Enter a number out of 100=")
     p=int(p)
     c=input("Enter a number out of 100=")
     c=int(c)
     m=input("Enter a number out of 100=")
     m=int(m)
     e=input("Enter a number out of 100=")
     e=int(e)
     h=input("Enter a number out of 100=")
     h=int(h)
     score=(((p+c+m+e+h)/500)*100)
if score>=40:
   print("The student is pass")
else:
   print("The student is fail")
4. **Temperature Check**
   - Write a program to check if the temperature `temp` is above 30 degrees. If it is, print `"It's a hot day!"`. Otherwise, print `"It's a cool day"`.
Ans: temp = float(input("Enter the temperature in Celsius: "))
if temp > 30:
    print("It's a hot day!")
else:
    print("It's a cool day")

5. **Adult Verification**
   - Using an `if` statement, write a program that checks if a person is an adult. If `age` is 18 or older, print `"You are an adult"`. Otherwise, print `"You are not an adult"`.
Ans: age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")

6. **Multiple of 5**
   - Write a program that checks if a given number `x` is a multiple of 5. If it is, print `"This number is a multiple of 5"`.
Ans: x = int(input("Enter a number: "))
if x % 5 == 0:
    print("This number is a multiple of 5")

7. **Check Vowel**
   - Write a Python program that checks if a given character `ch` is a vowel (`a, e, i, o, u`). Print `"It is a vowel"` if true.
Ans: ch = input("Enter a character: ")
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
   ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print("It is a vowel")
else:
      print("It is consonent")

8. **Password Verification**
   - Create a simple program to check if the entered password is `"secure123"`. If the password matches, print `"Access Granted"`. Otherwise, print `"Access Denied"`.
Ans: password = input("Enter password: ")
if password == "secure123":
    print("Access Granted")
else:
    print("Access Denied")

9. **Positive, Negative, or Zero**
   - Write a program that takes a number `num` and prints `"Positive"` if it is greater than zero, `"Negative"` if it is less than zero, and `"Zero"` if it is exactly zero.
Ans: num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    
10. **Weather Suggestion**
    - Write a Python program that checks if the `weather` variable is `"rainy"`. If it is, print `"Take an umbrella"`. Otherwise, print `"No umbrella needed"`.
ANS: weather = input("Enter the weather condition (e.g., rainy, sunny): ")
if weather == "rainy":
    print("Take an umbrella")
else:
    print("No umbrella needed")