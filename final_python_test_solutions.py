# 1) Reverse a number without converting it into a string
print("1) Reverse a number without converting it into a string")
num = 12345
sign = -1 if num < 0 else 1
n = abs(num)
rev = 0
while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10
rev *= sign
print(f"Original: {num}, Reversed: {rev}\n")


# 2) Check whether a number is a palindrome
print("2) Check whether a number is a palindrome")
num = 12321
if num < 0:
    is_palindrome = False
else:
    original = num
    rev = 0
    while num > 0:
        rev = rev * 10 + (num % 10)
        num //= 10
    is_palindrome = (original == rev)
print(f"Is {12321} a palindrome? {is_palindrome}\n")


# 3) Check whether a number is an Armstrong number
print("3) Check whether a number is an Armstrong number")
num = 153
digits = str(num)
power = len(digits)
armstrong_sum = sum(int(d) ** power for d in digits)
print(f"Is {num} an Armstrong number? {num == armstrong_sum}\n")


# 4) Find the factorial of a number using a loop
print("4) Find the factorial of a number using a loop")
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num}: {fact}\n")


# 5) Generate the Fibonacci series up to N terms
print("5) Generate the Fibonacci series up to N terms")
n_terms = 10
a, b = 0, 1
fib_series = []
for _ in range(n_terms):
    fib_series.append(a)
    a, b = b, a + b
print(f"Fibonacci series ({n_terms} terms): {fib_series}\n")


# 6) Check whether a number is prime
print("6) Check whether a number is prime")
num = 29
is_prime = num > 1
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
print(f"Is {num} prime? {is_prime}\n")


# 7) Print all prime numbers between 1 and 100
print("7) Print all prime numbers between 1 and 100")
primes = []
for num in range(2, 101):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        primes.append(num)
print("Primes between 1 and 100:", primes, "\n")


# 8) Find the GCD and LCM of two numbers
print("8) Find the GCD and LCM of two numbers")
a, b = 12, 18
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x
lcm = abs(a * b) // gcd if gcd != 0 else 0
print(f"Numbers: {a}, {b} -> GCD: {gcd}, LCM: {lcm}\n")


# 9) Reverse a string without using slicing
print("9) Reverse a string without using slicing")
text = "Python"
reversed_text = ""
for ch in text:
    reversed_text = ch + reversed_text
print(f"Original: '{text}', Reversed: '{reversed_text}'\n")


# 10) Check whether a string is a palindrome
print("10) Check whether a string is a palindrome")
text = "madam"
cleaned = text.lower()
is_pal = True
for i in range(len(cleaned) // 2):
    if cleaned[i] != cleaned[len(cleaned) - 1 - i]:
        is_pal = False
        break
print(f"Is '{text}' a palindrome? {is_pal}\n")


# 11) Count vowels, consonants, digits and special characters in a string
print("11) Count vowels, consonants, digits and special characters in a string")
text = "Hello World! 123@"
vowels = consonants = digits = special = 0
for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif not ch.isspace():
        special += 1
print(f"Text: '{text}'")
print(f"Vowels: {vowels}, Consonants: {consonants}, Digits: {digits}, Special: {special}\n")


# 12) Find the frequency of each character in a string
print("12) Find the frequency of each character in a string")
text = "programming"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(f"Character frequency in '{text}': {freq}\n")


# 13) Find the first non-repeating character in a string
print("13) Find the first non-repeating character in a string")
text = "swiss"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
first_non_repeat = None
for ch in text:
    if counts[ch] == 1:
        first_non_repeat = ch
        break
print(f"First non-repeating character in '{text}': {first_non_repeat}\n")


# 14) Remove duplicate characters from a string
print("14) Remove duplicate characters from a string")
text = "programming"
seen = set()
result = ""
for ch in text:
    if ch not in seen:
        seen.add(ch)
        result += ch
print(f"Original: '{text}', Without duplicates: '{result}'\n")


# 15) Check whether two strings are anagrams
print("15) Check whether two strings are anagrams")
s1, s2 = "listen", "silent"
c1 = s1.replace(" ", "").lower()
c2 = s2.replace(" ", "").lower()
is_anagram = sorted(c1) == sorted(c2)
print(f"Are '{s1}' and '{s2}' anagrams? {is_anagram}\n")


# 16) Find the longest word in a sentence
print("16) Find the longest word in a sentence")
sentence = "Python programming is powerful and versatile"
words = sentence.split()
longest_word = ""
for w in words:
    if len(w) > len(longest_word):
        longest_word = w
print(f"Sentence: '{sentence}' -> Longest word: '{longest_word}'\n")


# 17) Find the second-largest element in a list without using sort()
print("17) Find the second-largest element in a list without using sort()")
nums = [12, 35, 1, 10, 34, 1, 35]
largest = second_largest = float("-inf")
for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif largest > n > second_largest:
        second_largest = n
print(f"List: {nums} -> Second largest: {second_largest}\n")


# 18) Remove duplicate elements from a list without using set()
print("18) Remove duplicate elements from a list without using set()")
nums = [1, 2, 2, 3, 4, 3, 5, 1]
unique_list = []
for n in nums:
    if n not in unique_list:
        unique_list.append(n)
print(f"Original: {nums} -> Unique: {unique_list}\n")


# 19) Find the common elements between two lists
print("19) Find the common elements between two lists")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []
for item in list1:
    if item in list2 and item not in common:
        common.append(item)
print(f"Common elements between {list1} and {list2}: {common}\n")


# 20) Move all zeros to the end of a list without changing the order of other elements
print("20) Move all zeros to the end of a list without changing the order of other elements")
nums = [0, 1, 0, 3, 12, 0, 5]
non_zeros = [x for x in nums if x != 0]
zeros = [0] * (len(nums) - len(non_zeros))
result = non_zeros + zeros
print(f"Original: {nums} -> Zeros moved to end: {result}\n")


# 21) Find the missing number in a list containing numbers from 1 to N
print("21) Find the missing number in a list containing numbers from 1 to N")
nums = [1, 2, 4, 5, 6]
n = len(nums) + 1
expected_sum = n * (n + 1) // 2
missing = expected_sum - sum(nums)
print(f"List: {nums} -> Missing number: {missing}\n")


# 22) Find the maximum difference between two elements where the larger element appears after the smaller element
print("22) Find the maximum difference between two elements where the larger element appears after the smaller element")
nums = [2, 3, 10, 6, 4, 8, 1]
min_val = nums[0]
max_diff = nums[1] - nums[0]
for x in nums[1:]:
    if x - min_val > max_diff:
        max_diff = x - min_val
    if x < min_val:
        min_val = x
print(f"List: {nums} -> Maximum difference: {max_diff}\n")


# 23) Rotate a list to the right by K positions
print("23) Rotate a list to the right by K positions")
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
k = k % len(nums) if nums else 0
rotated = nums[-k:] + nums[:-k] if k else nums[:]
print(f"Original: {nums}, K={k} -> Rotated: {rotated}\n")


# 24) Find all pairs in a list whose sum equals a given target
print("24) Find all pairs in a list whose sum equals a given target")
nums = [2, 4, 3, 5, 7, 8, 1]
target = 9
pairs = []
seen = set()
for n in nums:
    complement = target - n
    if complement in seen:
        pairs.append((complement, n))
    seen.add(n)
print(f"List: {nums}, Target: {target} -> Pairs: {pairs}\n")


# 25) Count the frequency of each word in a paragraph
print("25) Count the frequency of each word in a paragraph")
paragraph = "Python is easy to learn. Python is also powerful and easy to use."
cleaned_words = [w.strip(".,!?;:\"'()").lower() for w in paragraph.split()]
word_freq = {}
for w in cleaned_words:
    if w:
        word_freq[w] = word_freq.get(w, 0) + 1
print(f"Word frequencies: {word_freq}\n")


# 26) Merge two dictionaries; if a key exists in both, add their values
print("26) Merge two dictionaries; if a key exists in both, add their values")
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 5, "c": 15, "d": 40}
merged = d1.copy()
for k, v in d2.items():
    merged[k] = merged.get(k, 0) + v
print(f"Dict 1: {d1}, Dict 2: {d2} -> Merged: {merged}\n")


# 27) Sort a dictionary based on its values
print("27) Sort a dictionary based on its values")
scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 81}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))
print(f"Original: {scores} -> Sorted by values: {sorted_scores}\n")


# 28) Find the student with the highest marks from a list of student dictionaries
print("28) Find the student with the highest marks from a list of student dictionaries")
students = [
    {"name": "Aarav", "marks": 84},
    {"name": "Priya", "marks": 96},
    {"name": "Rohan", "marks": 91},
]
top_student = max(students, key=lambda s: s["marks"])
print(f"Top student: {top_student}\n")


# 29) Group words from a list based on their first character using a dictionary
print("29) Group words from a list based on their first character using a dictionary")
words = ["apple", "ant", "banana", "ball", "cat", "car"]
grouped = {}
for w in words:
    first_char = w[0].lower()
    grouped.setdefault(first_char, []).append(w)
print(f"Grouped words: {grouped}\n")


# 30) Convert two lists into a dictionary (first list as keys, second as values)
print("30) Convert two lists into a dictionary (first list as keys, second as values)")
keys = ["name", "age", "city"]
values = ["Maya", 22, "Pune"]
result_dict = dict(zip(keys, values))
print(f"Result dictionary: {result_dict}\n")


# 31) Recursive function to calculate the factorial of a number
print("31) Recursive function to calculate the factorial of a number")
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)

print(f"Factorial of 6 (recursive): {factorial_recursive(6)}\n")


# 32) Recursive function to find the sum of digits of a number
print("32) Recursive function to find the sum of digits of a number")
def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(f"Sum of digits of 9875: {sum_of_digits(9875)}\n")


# 33) Implement your own map() function without using Python's built-in map()
print("33) Implement your own map() function without using Python's built-in map()")
def custom_map(func, iterable):
    return [func(item) for item in iterable]

nums = [1, 2, 3, 4, 5]
squared = custom_map(lambda x: x ** 2, nums)
print(f"Original: {nums} -> Custom map (squares): {squared}\n")


# 34) Function that accepts a list and returns a new list containing only even numbers
print("34) Function that accepts a list and returns a new list containing only even numbers")
def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {nums} -> Even numbers: {filter_even_numbers(nums)}\n")


# 35) Write a function to flatten a nested list
print("35) Write a function to flatten a nested list")
def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

nested_data = [1, [2, [3, 4], 5], [6, 7], 8]
print(f"Nested: {nested_data} -> Flattened: {flatten_list(nested_data)}\n")


# 36) Student Management System
print("36) Student Management System")
def student_management_system():
    students_db = {}
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            sid = input("Enter Student ID: ").strip()
            if sid in students_db:
                print("Student ID already exists.")
            else:
                name = input("Enter Name: ").strip()
                age = input("Enter Age: ").strip()
                course = input("Enter Course: ").strip()
                students_db[sid] = {"name": name, "age": age, "course": course}
                print("Student added successfully.")
        elif choice == "2":
            if not students_db:
                print("No students found.")
            else:
                for sid, info in students_db.items():
                    print(f"ID: {sid} | Name: {info['name']} | Age: {info['age']} | Course: {info['course']}")
        elif choice == "3":
            sid = input("Enter Student ID to search: ").strip()
            if sid in students_db:
                info = students_db[sid]
                print(f"Found -> ID: {sid} | Name: {info['name']} | Age: {info['age']} | Course: {info['course']}")
            else:
                print("Student not found.")
        elif choice == "4":
            sid = input("Enter Student ID to update: ").strip()
            if sid in students_db:
                name = input("Enter new Name (leave blank to keep current): ").strip()
                age = input("Enter new Age (leave blank to keep current): ").strip()
                course = input("Enter new Course (leave blank to keep current): ").strip()
                if name:
                    students_db[sid]["name"] = name
                if age:
                    students_db[sid]["age"] = age
                if course:
                    students_db[sid]["course"] = course
                print("Student updated successfully.")
            else:
                print("Student not found.")
        elif choice == "5":
            sid = input("Enter Student ID to delete: ").strip()
            if sid in students_db:
                del students_db[sid]
                print("Student deleted successfully.")
            else:
                print("Student not found.")
        elif choice == "6":
            print("Exiting Student Management System.")
            break
        else:
            print("Invalid choice. Try again.")


# 37) Bank Account Management
print("37) Bank Account Management")
def bank_account_management():
    accounts = {}
    while True:
        print("\n--- Bank Account Management ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display Account Details")
        print("6. Exit")
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            acc_no = input("Enter Account Number: ").strip()
            if acc_no in accounts:
                print("Account already exists.")
            else:
                holder = input("Enter Account Holder Name: ").strip()
                balance = float(input("Enter Initial Deposit: "))
                accounts[acc_no] = {"holder": holder, "balance": balance}
                print("Account created successfully.")
        elif choice == "2":
            acc_no = input("Enter Account Number: ").strip()
            if acc_no in accounts:
                amount = float(input("Enter Deposit Amount: "))
                if amount > 0:
                    accounts[acc_no]["balance"] += amount
                    print(f"Deposited {amount:.2f}. New Balance: {accounts[acc_no]['balance']:.2f}")
                else:
                    print("Deposit amount must be positive.")
            else:
                print("Account not found.")
        elif choice == "3":
            acc_no = input("Enter Account Number: ").strip()
            if acc_no in accounts:
                amount = float(input("Enter Withdrawal Amount: "))
                if 0 < amount <= accounts[acc_no]["balance"]:
                    accounts[acc_no]["balance"] -= amount
                    print(f"Withdrew {amount:.2f}. New Balance: {accounts[acc_no]['balance']:.2f}")
                else:
                    print("Invalid amount or insufficient balance.")
            else:
                print("Account not found.")
        elif choice == "4":
            acc_no = input("Enter Account Number: ").strip()
            if acc_no in accounts:
                print(f"Current Balance: {accounts[acc_no]['balance']:.2f}")
            else:
                print("Account not found.")
        elif choice == "5":
            acc_no = input("Enter Account Number: ").strip()
            if acc_no in accounts:
                acc = accounts[acc_no]
                print(f"Account No: {acc_no} | Holder: {acc['holder']} | Balance: {acc['balance']:.2f}")
            else:
                print("Account not found.")
        elif choice == "6":
            print("Exiting Bank Account Management.")
            break
        else:
            print("Invalid choice. Try again.")


# 38) Employee Salary Management
print("38) Employee Salary Management")
def employee_salary_management():
    employees = {}

    def calculate_gross(basic, hra, da):
        return basic + hra + da

    def calculate_deductions(gross, tax_rate=0.10, pf_rate=0.05):
        return gross * tax_rate + gross * pf_rate

    def calculate_net(gross, deductions):
        return gross - deductions

    while True:
        print("\n--- Employee Salary Management ---")
        print("1. Add Employee Details")
        print("2. Display Employee Salary Details")
        print("3. Exit")
        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            emp_id = input("Enter Employee ID: ").strip()
            name = input("Enter Employee Name: ").strip()
            basic = float(input("Enter Basic Salary: "))
            hra = float(input("Enter HRA: "))
            da = float(input("Enter DA: "))
            gross = calculate_gross(basic, hra, da)
            deductions = calculate_deductions(gross)
            net = calculate_net(gross, deductions)
            employees[emp_id] = {
                "name": name,
                "basic": basic,
                "hra": hra,
                "da": da,
                "gross": gross,
                "deductions": deductions,
                "net": net,
            }
            print("Employee added and salary calculated.")
        elif choice == "2":
            if not employees:
                print("No employee records found.")
            else:
                for emp_id, e in employees.items():
                    print(
                        f"ID: {emp_id} | Name: {e['name']} | Gross: {e['gross']:.2f} | "
                        f"Deductions: {e['deductions']:.2f} | Net Salary: {e['net']:.2f}"
                    )
        elif choice == "3":
            print("Exiting Employee Salary Management.")
            break
        else:
            print("Invalid choice. Try again.")


# 39) Library Management System
print("39) Library Management System")
def library_management_system():
    books = {}
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Display Available Books")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. Search Books by Title")
        print("6. Exit")
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            book_id = input("Enter Book ID: ").strip()
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author: ").strip()
            copies = int(input("Enter Number of Copies: "))
            books[book_id] = {"title": title, "author": author, "copies": copies}
            print("Book added successfully.")
        elif choice == "2":
            available = [
                (bid, b) for bid, b in books.items() if b["copies"] > 0
            ]
            if not available:
                print("No books currently available.")
            else:
                for bid, b in available:
                    print(f"ID: {bid} | Title: {b['title']} | Author: {b['author']} | Copies: {b['copies']}")
        elif choice == "3":
            book_id = input("Enter Book ID to issue: ").strip()
            if book_id in books and books[book_id]["copies"] > 0:
                books[book_id]["copies"] -= 1
                print(f"Issued '{books[book_id]['title']}'. Remaining copies: {books[book_id]['copies']}")
            else:
                print("Book not available or does not exist.")
        elif choice == "4":
            book_id = input("Enter Book ID to return: ").strip()
            if book_id in books:
                books[book_id]["copies"] += 1
                print(f"Returned '{books[book_id]['title']}'. Available copies: {books[book_id]['copies']}")
            else:
                print("Book ID not found in library records.")
        elif choice == "5":
            query = input("Enter title keyword to search: ").strip().lower()
            matches = [
                (bid, b) for bid, b in books.items() if query in b["title"].lower()
            ]
            if not matches:
                print("No matching books found.")
            else:
                for bid, b in matches:
                    print(f"ID: {bid} | Title: {b['title']} | Author: {b['author']} | Copies: {b['copies']}")
        elif choice == "6":
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Try again.")


# 40) Task Management Application
print("40) Task Management Application")
def task_management_application():
    tasks = {}
    next_id = 1
    while True:
        print("\n--- Task Management Application ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Filter Completed and Pending Tasks")
        print("7. Exit")
        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            title = input("Enter Task Description: ").strip()
            tasks[next_id] = {"title": title, "completed": False}
            print(f"Task added with ID {next_id}.")
            next_id += 1
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
            else:
                for tid, t in tasks.items():
                    status = "Completed" if t["completed"] else "Pending"
                    print(f"ID: {tid} | {t['title']} [{status}]")
        elif choice == "3":
            tid = int(input("Enter Task ID to update: "))
            if tid in tasks:
                new_title = input("Enter new Task Description: ").strip()
                tasks[tid]["title"] = new_title
                print("Task updated.")
            else:
                print("Task not found.")
        elif choice == "4":
            tid = int(input("Enter Task ID to delete: "))
            if tid in tasks:
                del tasks[tid]
                print("Task deleted.")
            else:
                print("Task not found.")
        elif choice == "5":
            tid = int(input("Enter Task ID to mark completed: "))
            if tid in tasks:
                tasks[tid]["completed"] = True
                print("Task marked as completed.")
            else:
                print("Task not found.")
        elif choice == "6":
            filter_type = input("Show (c)ompleted or (p)ending tasks? ").strip().lower()
            want_completed = filter_type == "c"
            filtered = [
                (tid, t) for tid, t in tasks.items() if t["completed"] == want_completed
            ]
            label = "Completed" if want_completed else "Pending"
            if not filtered:
                print(f"No {label.lower()} tasks found.")
            else:
                print(f"--- {label} Tasks ---")
                for tid, t in filtered:
                    print(f"ID: {tid} | {t['title']}")
        elif choice == "7":
            print("Exiting Task Management Application.")
            break
        else:
            print("Invalid choice. Try again.")


# Uncomment any console application below to run it interactively:
if __name__ == "__main__":
    # student_management_system()
    # bank_account_management()
    # employee_salary_management()
    # library_management_system()
    # task_management_application()
    pass
