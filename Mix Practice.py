

import math
import os
import random
import string
import tempfile
from datetime import date


# 1. Find the data type of every value in a mixed list.
print("1. Find the data type of every value in a mixed list.")

mixed_list = [42, 3.14, "hello", True, [1, 2], (3, 4), {"a": 1}, None]
types = [(val, type(val).__name__) for val in mixed_list]
print("Result:", types)


# 2. Convert a nested list into a tuple of tuples.
print("\n2. Convert a nested list into a tuple of tuples.")

nested_list = [[1, 2], [3, 4], [5, 6]]
tuple_of_tuples = tuple(tuple(sub) for sub in nested_list)
print("Result:", tuple_of_tuples)


# 3. Remove all duplicate values from a mixed list while preserving the original order.
print("\n3. Remove all duplicate values from a mixed list while preserving the original order.")

def remove_duplicates_preserve_order(items):
    unique = []
    for item in items:
        # Check both value and exact type so True (bool) and 1 (int) stay distinct
        if not any(item == u and type(item) is type(u) for u in unique):
            unique.append(item)
    return unique

print("Result:", remove_duplicates_preserve_order([1, "a", 1, True, [2, 3], "a", [2, 3], 2]))



# 4. Check whether a number is a power of 2 using operators.
print("\n4. Check whether a number is a power of 2 using operators.")

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print("16 ->", is_power_of_two(16), "| 18 ->", is_power_of_two(18))


# 5. Swap two numbers using bitwise XOR.
print("\n5. Swap two numbers using bitwise XOR.")

a, b = 15, 27
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After swap: a={a}, b={b}")


# 6. Find whether a number is divisible by both 4 and 6 using logical operators.
print("\n6. Find whether a number is divisible by both 4 and 6 using logical operators.")

num = 24
is_divisible = (num % 4 == 0) and (num % 6 == 0)
print(f"{num} divisible by both 4 and 6:", is_divisible)


# 7. Calculate the total electricity bill using different unit rates.
print("\n7. Calculate the total electricity bill using different unit rates.")

def calculate_electricity_bill(units):
    # Example slab rates: 0-100 @ 5/unit, 101-200 @ 7/unit, >200 @ 10/unit
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7
    else:
        return 100 * 5 + 100 * 7 + (units - 200) * 10

print("Bill for 250 units:", calculate_electricity_bill(250))


# 8. Check whether three sides can form a triangle.
print("\n8. Check whether three sides can form a triangle.")

def can_form_triangle(x, y, z):
    return x > 0 and y > 0 and z > 0 and (x + y > z) and (x + z > y) and (y + z > x)

print("Sides (3, 4, 5):", can_form_triangle(3, 4, 5))


# 9. Determine the type of triangle (Equilateral, Isosceles, Scalene).
print("\n9. Determine the type of triangle (Equilateral, Isosceles, Scalene).")

def triangle_type(x, y, z):
    if not can_form_triangle(x, y, z):
        return "Not a valid triangle"
    if x == y == z:
        return "Equilateral"
    elif x == y or y == z or x == z:
        return "Isosceles"
    else:
        return "Scalene"

print("(5, 5, 8):", triangle_type(5, 5, 8))


# 10. Create a simple ATM menu (Withdraw, Deposit, Balance).
print("\n10. Create a simple ATM menu (Withdraw, Deposit, Balance).")

def atm_operation(balance, choice, amount=0):
    if choice == "1":  # Balance
        return balance, f"Current Balance: {balance}"
    elif choice == "2":  # Deposit
        if amount > 0:
            balance += amount
            return balance, f"Deposited {amount}. New Balance: {balance}"
        return balance, "Invalid deposit amount."
    elif choice == "3":  # Withdraw
        if 0 < amount <= balance:
            balance -= amount
            return balance, f"Withdrew {amount}. New Balance: {balance}"
        return balance, "Insufficient funds or invalid amount."
    else:
        return balance, "Invalid menu choice."

bal = 1000
bal, msg = atm_operation(bal, "2", 500)
print(msg)
bal, msg = atm_operation(bal, "3", 300)
print(msg)
bal, msg = atm_operation(bal, "1")
print(msg)


# 11. Calculate income tax based on different tax slabs.
print("\n11. Calculate income tax based on different tax slabs.")

def calculate_income_tax(income):
    # Example slabs: 0-2.5L: 0%, 2.5L-5L: 5%, 5L-10L: 20%, >10L: 30%
    tax = 0.0
    if income <= 250000:
        tax = 0.0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = 250000 * 0.05 + (income - 500000) * 0.20
    else:
        tax = 250000 * 0.05 + 500000 * 0.20 + (income - 1000000) * 0.30
    return tax

print("Tax on 1,200,000:", calculate_income_tax(1200000))


# 12. Create a menu-driven calculator using if-elif.
print("\n12. Create a menu-driven calculator using if-elif.")

def calculator(op, x, y):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y if y != 0 else "Division by zero error"
    else:
        return "Invalid operator"

print("10 * 5 =", calculator("*", 10, 5))


# 13. Print all prime numbers between 1 and n.
print("\n13. Print all prime numbers between 1 and n.")

def primes_up_to(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print("Primes up to 30:", primes_up_to(30))


# 14. Find the factorial of a number using a loop.
print("\n14. Find the factorial of a number using a loop.")

def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("5! =", factorial_loop(5))


# 15. Print the Fibonacci series up to n terms.
print("\n15. Print the Fibonacci series up to n terms.")

def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print("First 8 Fibonacci terms:", fibonacci_series(8))


# 16. Check whether a number is an Armstrong number.
print("\n16. Check whether a number is an Armstrong number.")

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == n

print("153 ->", is_armstrong(153), "| 123 ->", is_armstrong(123))


# 17. Reverse a number and check if it is a palindrome.
print("\n17. Reverse a number and check if it is a palindrome.")

def reverse_and_check_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev, rev == original

print("12321 ->", reverse_and_check_palindrome(12321))


# 18. Find the Greatest Common Divisor (GCD) of two numbers.
print("\n18. Find the Greatest Common Divisor (GCD) of two numbers.")

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

print("GCD(48, 18):", find_gcd(48, 18))



# 19. Write a function to check if a string is a palindrome.
print("\n19. Write a function to check if a string is a palindrome.")

def is_string_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

print("'Madam' ->", is_string_palindrome("Madam"))


# 20. Write a function to count vowels and consonants in a string.
print("\n20. Write a function to count vowels and consonants in a string.")

def count_vowels_consonants(s):
    vowels = set("aeiouAEIOU")
    v_count = c_count = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

print("'Hello World' -> (vowels, consonants):", count_vowels_consonants("Hello World"))


# 21. Create a function to calculate simple and compound interest.
print("\n21. Create a function to calculate simple and compound interest.")

def calculate_interest(principal, rate, time, compounds_per_year=1):
    si = (principal * rate * time) / 100
    ci = principal * ((1 + (rate / 100) / compounds_per_year) ** (compounds_per_year * time)) - principal
    return round(si, 2), round(ci, 2)

print("SI & CI (P=10000, R=5%, T=2yrs):", calculate_interest(10000, 5, 2))


# 22. Write a function to return all factors of a number.
print("\n22. Write a function to return all factors of a number.")

def get_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

print("Factors of 28:", get_factors(28))


# 23. Write a function to find the second-largest number in a list.
print("\n23. Write a function to find the second-largest number in a list.")

def second_largest_in_list(nums):
    unique = sorted(set(nums))
    return unique[-2] if len(unique) >= 2 else None

print("Result:", second_largest_in_list([10, 20, 4, 45, 99, 99]))


# 24. Merge two lists without duplicates.
print("\n24. Merge two lists without duplicates.")

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
merged_unique = list(dict.fromkeys(list1 + list2))
print("Result:", merged_unique)


# 25. Find the second-largest and second-smallest elements.
print("\n25. Find the second-largest and second-smallest elements.")

def second_largest_and_smallest(nums):
    unique = sorted(set(nums))
    if len(unique) < 2:
        return None, None
    return unique[-2], unique[1]

print("Result (2nd largest, 2nd smallest):", second_largest_and_smallest([12, 45, 2, 41, 31, 10, 8, 6, 4]))


# 26. Rotate a list to the left by k positions.
print("\n26. Rotate a list to the left by k positions.")

def rotate_left(lst, k):
    if not lst:
        return lst
    k %= len(lst)
    return lst[k:] + lst[:k]

print("Result:", rotate_left([1, 2, 3, 4, 5], 2))


# 27. Separate even and odd numbers into two lists.
print("\n27. Separate even and odd numbers into two lists.")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in nums if x % 2 == 0]
odds = [x for x in nums if x % 2 != 0]
print("Evens:", evens, "| Odds:", odds)


# 28. Find the common elements between two lists.
print("\n28. Find the common elements between two lists.")

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
common = list(set(l1) & set(l2))
print("Result:", common)


# 29. Count the frequency of each element in a tuple.
print("\n29. Count the frequency of each element in a tuple.")

tup = (1, 2, 2, 3, 3, 3, 4)
freq = {}
for item in tup:
    freq[item] = freq.get(item, 0) + 1
print("Result:", freq)


# 30. Find the union, intersection, and difference of two sets.
print("\n30. Find the union, intersection, and difference of two sets.")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a | set_b, "| Intersection:", set_a & set_b, "| Difference (A-B):", set_a - set_b)


# 31. Check whether one set is a subset of another.
print("\n31. Check whether one set is a subset of another.")

s1 = {1, 2}
s2 = {1, 2, 3, 4}
print("Is s1 subset of s2?", s1.issubset(s2))

# 32. Count the frequency of words in a sentence.
print("\n32. Count the frequency of words in a sentence.")

sentence = "python is easy and python is powerful"
word_freq = {}
for word in sentence.lower().split():
    word_freq[word] = word_freq.get(word, 0) + 1
print("Result:", word_freq)


# 33. Create a dictionary from two lists (keys and values).
print("\n33. Create a dictionary from two lists (keys and values).")

keys = ["name", "age", "city"]
values = ["Alice", 25, "Pune"]
combined_dict = dict(zip(keys, values))
print("Result:", combined_dict)


# 34. Sort a dictionary by its values.
print("\n34. Sort a dictionary by its values.")

scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 81}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))
print("Result:", sorted_scores)


# 35. Read a text file and count the number of lines, words, and characters.
print("\n35. Read a text file and count the number of lines, words, and characters.")

with tempfile.TemporaryDirectory() as tmpdir:
    sample_path = os.path.join(tmpdir, "sample.txt")
    with open(sample_path, "w", encoding="utf-8") as f:
        f.write("Line one text\nLine two text\nLine three text\nLine four text\n")

    with open(sample_path, "r", encoding="utf-8") as f:
        content = f.read()
        lines = content.splitlines()
        words = content.split()
        chars = len(content)
    print(f"Lines: {len(lines)}, Words: {len(words)}, Characters: {chars}")


# 36. Copy only the even-numbered lines from one file to another.
print("\n36. Copy only the even-numbered lines from one file to another.")

with tempfile.TemporaryDirectory() as tmpdir:
    src_path = os.path.join(tmpdir, "source.txt")
    dst_path = os.path.join(tmpdir, "even_lines.txt")
    with open(src_path, "w", encoding="utf-8") as f:
        f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\n")

    with open(src_path, "r", encoding="utf-8") as src, open(dst_path, "w", encoding="utf-8") as dst:
        for line_num, line in enumerate(src, start=1):
            if line_num % 2 == 0:
                dst.write(line)

    with open(dst_path, "r", encoding="utf-8") as dst:
        print("Copied even lines:", dst.read().splitlines())


# 37. Handle invalid integer input using try-except.
print("\n37. Handle invalid integer input using try-except.")

def parse_integer(user_input):
    try:
        value = int(user_input)
        return f"Valid integer: {value}"
    except ValueError:
        return f"Invalid integer input: '{user_input}'"

print(parse_integer("42"), "|", parse_integer("abc"))


# 38. Handle file-not-found errors while reading a file.
print("\n38. Handle file-not-found errors while reading a file.")

def read_file_safely(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."

print(read_file_safely("non_existent_file_12345.txt"))



# 39. Create a random password generator using the random and string modules.
print("\n39. Create a random password generator using the random and string modules.")

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

print("Generated password:", generate_password(12))


# 40. Use the datetime module to calculate the number of days between two dates.
print("\n40. Use the datetime module to calculate the number of days between two dates.")

date1 = date(2026, 1, 1)
date2 = date(2026, 11, 26)
days_between = abs((date2 - date1).days)
print(f"Days between {date1} and {date2}: {days_between}")
