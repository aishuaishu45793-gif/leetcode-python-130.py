# 🐍 LeetCode Python Practice (126–130)

## 📌 About This Repository

Welcome to my Python programming practice repository!

This repository contains five beginner-friendly Python programs designed to improve my programming fundamentals, logical thinking, and problem-solving skills.

Each program focuses on a different problem using Python lists, loops, conditional statements, string manipulation, and mathematical operations.

## 🎯 Objectives

* Strengthen Python programming fundamentals.
* Practice solving programming problems.
* Understand lists, loops, and conditional statements.
* Learn to use Python built-in functions.
* Improve logical thinking and analytical skills.
* Build a consistent coding practice portfolio on GitHub.

## 📚 Problems Included

| No. | Problem Name                                     | Main Concepts                     |
| --- | ------------------------------------------------ | --------------------------------- |
| 126 | Count Even and Odd Numbers                       | Lists, loops, modulo operator     |
| 127 | Find the Smallest Number in a List               | Lists, `min()`                    |
| 128 | Reverse a Number                                 | Strings, slicing, type conversion |
| 129 | Check Whether a Number Is a Perfect Number       | Loops, divisors, mathematics      |
| 130 | Remove All Occurrences of an Element from a List | Lists, list comprehensions        |

---

# 1️⃣ LeetCode Python 126 — Count Even and Odd Numbers

## Description

Write a Python program to count the number of even and odd integers in a list.

An even number is divisible by 2, while an odd number is not divisible by 2.

## Python Code

```python
try:
    numbers = list(map(
        int,
        input("Enter numbers separated by spaces: ").split()
    ))

    even_count = 0
    odd_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even numbers count:", even_count)
    print("Odd numbers count:", odd_count)

except ValueError:
    print("Invalid input! Please enter numbers only.")
```

## Example

**Input:**

```text
Enter numbers separated by spaces: 1 2 3 4 5 6
```

**Output:**

```text
Even numbers count: 3
Odd numbers count: 3
```

## Concepts Learned

* Python lists
* Loops
* Conditional statements
* Modulo operator (`%`)
* Exception handling

---

# 2️⃣ LeetCode Python 127 — Find the Smallest Number in a List

## Description

Write a Python program to find the smallest number in a list of integers entered by the user.

## Python Code

```python
try:
    numbers = list(map(
        int,
        input("Enter numbers separated by spaces: ").split()
    ))

    if numbers:
        smallest = min(numbers)
        print("Smallest number:", smallest)
    else:
        print("The list is empty.")

except ValueError:
    print("Invalid input! Please enter integers only.")
```

## Example

**Input:**

```text
Enter numbers separated by spaces: 15 8 22 3 10
```

**Output:**

```text
Smallest number: 3
```

## Concepts Learned

* Lists
* User input
* Type conversion
* `min()` function
* Conditional statements
* Exception handling

---

# 3️⃣ LeetCode Python 128 — Reverse a Number

## Description

Write a Python program to reverse the digits of an integer.

For example, the reverse of `12345` is `54321`.

## Python Code

```python
try:
    number = int(input("Enter an integer: "))

    sign = -1 if number < 0 else 1
    reversed_number = int(str(abs(number))[::-1]) * sign

    print("Reversed number:", reversed_number)

except ValueError:
    print("Invalid input! Please enter an integer.")
```

## Example

**Input:**

```text
Enter an integer: 12345
```

**Output:**

```text
Reversed number: 54321
```

## Negative Number Example

**Input:**

```text
Enter an integer: -987
```

**Output:**

```text
Reversed number: -789
```

## Concepts Learned

* Integers and strings
* String slicing (`[::-1]`)
* Type conversion
* `abs()` function
* Conditional expressions
* Exception handling

---

# 4️⃣ LeetCode Python 129 — Check Whether a Number Is a Perfect Number

## Description

A perfect number is a positive integer equal to the sum of its positive divisors, excluding itself.

For example:

`6 = 1 + 2 + 3`

Therefore, 6 is a perfect number.

## Python Code

```python
try:
    number = int(input("Enter a positive integer: "))

    if number <= 0:
        print("Please enter a positive integer.")
    else:
        divisor_sum = 0

        for i in range(1, number):
            if number % i == 0:
                divisor_sum += i

        if divisor_sum == number:
            print(number, "is a perfect number.")
        else:
            print(number, "is not a perfect number.")

except ValueError:
    print("Invalid input! Please enter an integer.")
```

## Example

**Input:**

```text
Enter a positive integer: 28
```

**Output:**

```text
28 is a perfect number.
```

## Concepts Learned

* Loops
* Conditional statements
* Divisors
* Modulo operator
* Arithmetic operations
* Accumulating a sum
* Exception handling

---

# 5️⃣ LeetCode Python 130 — Remove All Occurrences of an Element from a List

## Description

Write a Python program to remove all occurrences of a specified number from a list.

The program creates a new list containing only the elements that do not match the target number.

## Python Code

```python
try:
    numbers = list(map(
        int,
        input("Enter numbers separated by spaces: ").split()
    ))

    target = int(input("Enter the number to remove: "))

    result = [number for number in numbers if number != target]

    print("Updated list:", result)

except ValueError:
    print("Invalid input! Please enter integers only.")
```

## Example

**Input:**

```text
Enter numbers separated by spaces: 1 2 3 2 4 2 5
Enter the number to remove: 2
```

**Output:**

```text
Updated list: [1, 3, 4, 5]
```

## Concepts Learned

* Python lists
* List comprehensions
* Filtering elements
* Conditional expressions
* User input
* Type conversion
* Exception handling

---

# 🛠️ Technologies Used

* **Programming Language:** Python 3
* **Code Editor:** Visual Studio Code
* **Version Control:** Git
* **Code Hosting:** GitHub

# 🚀 How to Run the Programs

## Step 1: Install Python

Install Python 3 on your computer.

## Step 2: Open VS Code

Open the folder containing your Python project.

## Step 3: Open the Terminal

Select **Terminal → New Terminal** in Visual Studio Code.

## Step 4: Run a Program

If your Python files are stored in a folder named `python`, use these commands:

**Problem 126:**

```bash
python python/126.py
```

**Problem 127:**

```bash
python python/127.py
```

**Problem 128:**

```bash
python python/128.py
```

**Problem 129:**

```bash
python python/129.py
```

**Problem 130:**

```bash
python python/130.py
```

Enter the requested values and check the output in the terminal.

*Note: Adjust the file paths if your files are stored in a different folder.*

# 📈 Learning Outcomes

By completing these five exercises, I practiced:

* Working with lists and integers.
* Using loops and conditional statements.
* Applying mathematical operations.
* Reversing numbers using string slicing.
* Finding divisors and checking perfect numbers.
* Filtering list elements with list comprehensions.
* Handling invalid user input.
* Running Python programs in Visual Studio Code.

# 👩‍💻 Author

**Aishwarya**

## 🔗 Individual GitHub Repositories

1. [LeetCode Python 126 — Count Even and Odd Numbers](https://github.com/aishuaishu45793-gif/leetcode-python-126.py)
2. [LeetCode Python 127 — Find the Smallest Number](https://github.com/aishuaishu45793-gif/leetcode-python-127.py)
3. [LeetCode Python 128 — Reverse a Number](https://github.com/aishuaishu45793-gif/leetcode-python-128.py)
4. [LeetCode Python 129 — Perfect Number Checker](https://github.com/aishuaishu45793-gif/leetcode-python-129.py)
5. [LeetCode Python 130 — Remove All Occurrences](https://github.com/aishuaishu45793-gif/leetcode-python-130.py)

---

⭐ **Thank you for visiting my Python practice projects!**

I am continuously improving my Python programming skills through regular practice, problem-solving, and building projects on GitHub.
