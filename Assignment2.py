#1)Even or Odd Function
print("1)Even or Odd Function")
def is_even(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print(is_even(7))


#2)Largest of Two Numbers
print("2)Largest of Two Numbers")
def largest(a, b):
    if a > b:
        return a
    return b

print(largest(10, 20))


#3)Print Numbers
print("3)Print Numbers")
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(10)


#4)Sum of Numbers
print("4)Sum of Numbers")
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_n(10))


#5)Multiplication Table
print("5)Multiplication Table")
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

table(5)


#6)Count Even Numbers
print("6)Count Even Numbers")
def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 6]))


#7)Find Maximum
print("7)Find Maximum")
def find_maximum(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    largest_number = numbers[0]
    for n in numbers:
        if n > largest_number:
            largest_number = n
    return largest_number

print(find_maximum([4, 9, 2, 7, 5]))


#11)FizzBuzz
print("11)FizzBuzz")
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()


#12)Palindrome Checker
print("12)Palindrome Checker")
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("madam"))


#13)Count Vowels
print("13)Count Vowels")
def count_vowels(text):
    count = 0
    for character in text.lower():
        if character in "aeiou":
            count += 1
    return count

print(count_vowels("Hello World"))


#14)Second Largest Number
print("14)Second Largest Number")
def second_largest(numbers):
    largest_number = None
    second_largest_number = None

    for n in numbers:
        if largest_number is None or n > largest_number:
            if n != largest_number:
                second_largest_number = largest_number
                largest_number = n
        elif n != largest_number and (second_largest_number is None or n > second_largest_number):
            second_largest_number = n

    if second_largest_number is None:
        raise ValueError("List must contain at least two distinct numbers")
    return second_largest_number

print(second_largest([10, 5, 8, 20, 15]))


#15)Guessing Game
print("15)Guessing Game")
import random

def guessing_game():
    number = random.randint(1, 10)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == number:
            print("Correct! You guessed the number.")
            break
        elif guess < number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

guessing_game()


#16)Grade Calculator
print("16)Grade Calculator")
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    return "F"

print(grade(85))
