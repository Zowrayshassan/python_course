# =============================================================================
# LECTURE 3: COMPLETE GUIDE TO WHILE LOOPS IN PYTHON
# =============================================================================

"""
WHILE LOOPS: A Complete Deep Dive

A while loop executes a block of code repeatedly as long as a condition is True.
It's one of the fundamental control structures in programming.

Basic Syntax:
while condition:
    # code to execute
    # this code repeats while condition is True

Key Components:
1. Condition: A boolean expression that controls the loop
2. Loop Body: The code that executes repeatedly
3. Update Statement: Code that modifies the condition (prevents infinite loops)
"""

print("=== COMPLETE GUIDE TO WHILE LOOPS IN PYTHON ===\n")
print("🔄 Master the art of repetitive execution with while loops!")
print("=" * 60)

# =============================================================================
# 1. BASIC WHILE LOOP
# =============================================================================
print("1. Basic While Loop Example:")
print("-" * 30)

# Simple counting example
count = 1
while count <= 5:
    print("Count:", count)
    count += 1  # This is crucial - increment to avoid infinite loop!

print()

# =============================================================================
# 2. WHILE LOOP WITH USER INPUT
# =============================================================================
print("2. While Loop with User Input:")
print("-" * 30)

# Keep asking for input until user enters 'quit'
print("Enter 'quit' to stop the loop")
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Enter a word: ")
    if user_input.lower() != "quit":
        print(f"You entered: {user_input}")

print()

# =============================================================================
# 3. WHILE LOOP WITH CONDITIONS
# =============================================================================
print("3. While Loop with Different Conditions:")
print("-" * 30)

# Sum numbers until total exceeds 50
total = 0
number = 1
while total < 50:
    total += number
    print(f"Added {number}, Total: {total}")
    number += 1

print()

# =============================================================================
# 4. WHILE LOOP WITH BREAK STATEMENT
# =============================================================================
print("4. While Loop with Break Statement:")
print("-" * 30)

# Find the first number divisible by 7 after 20
num = 21
while True:  # Infinite loop
    if num % 7 == 0:
        print(f"First number divisible by 7 after 20: {num}")
        break  # Exit the loop
    num += 1

print()

# =============================================================================
# 5. WHILE LOOP WITH CONTINUE STATEMENT
# =============================================================================
print("5. While Loop with Continue Statement:")
print("-" * 30)

# Print odd numbers from 1 to 10
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:  # If even number
        continue    # Skip to next iteration
    print(f"Odd number: {i}")

print()

# =============================================================================
# 6. NESTED WHILE LOOPS
# =============================================================================
print("6. Nested While Loops:")
print("-" * 30)

# Create a simple multiplication table
row = 1
while row <= 3:
    col = 1
    while col <= 3:
        result = row * col
        print(f"{row} x {col} = {result}")
        col += 1
    print()  # New line after each row
    row += 1

# =============================================================================
# 7. WHILE LOOP WITH ELSE CLAUSE
# =============================================================================
print("7. While Loop with Else Clause:")
print("-" * 30)

# The else clause executes when the while condition becomes False
# (but NOT when the loop is terminated by break)
search_num = 15
current = 10
while current < search_num:
    print(f"Searching... current: {current}")
    current += 1
else:
    print(f"Found! Number {search_num} reached.")

print()

# =============================================================================
# 8. COMMON WHILE LOOP PATTERNS
# =============================================================================
print("8. Common While Loop Patterns:")
print("-" * 30)

# Pattern 1: Menu-driven program
print("Simple Calculator Menu:")
while True:
    print("\n1. Add")
    print("2. Subtract") 
    print("3. Exit")
    
    choice = input("Enter choice (1/2/3): ")
    
    if choice == '3':
        print("Goodbye!")
        break
    elif choice in ['1', '2']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
            else:
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
        except ValueError:
            print("Please enter valid numbers!")
    else:
        print("Invalid choice!")

print()

# =============================================================================
# 9. WHILE LOOP BEST PRACTICES
# =============================================================================
print("9. While Loop Best Practices:")
print("-" * 30)

print("""
BEST PRACTICES FOR WHILE LOOPS:

1. ALWAYS ensure the loop condition will eventually become False
   - Avoid infinite loops by updating the control variable

2. Initialize variables before the loop:
   counter = 0
   while counter < 10:
       # do something
       counter += 1  # Don't forget this!

3. Use meaningful variable names:
   while is_running:  # Better than: while flag:

4. Consider using 'for' loops when you know the number of iterations

5. Use break and continue judiciously:
   - break: Exit the loop immediately
   - continue: Skip current iteration, go to next

6. Be careful with user input loops:
   while True:
       user_input = input("Enter command: ")
       if user_input == "quit":
           break
""")

# =============================================================================
# 10. PRACTICE EXERCISES
# =============================================================================
print("\n10. Practice Exercises:")
print("-" * 30)

print("""
TRY THESE EXERCISES:

1. Write a while loop to find the factorial of a number
2. Create a guessing game where user guesses a random number
3. Write a loop that reverses a string using while loop
4. Create a password validator that keeps asking until valid password
5. Write a loop that finds all prime numbers up to 50
""")

print("\n=== END OF WHILE LOOPS LESSON ===")

# =============================================================================
# PRACTICE QUESTIONS WITH SOLUTIONS
# =============================================================================

print("\n" + "=" * 60)
print("🎯 PRACTICE QUESTIONS WITH STEP-BY-STEP SOLUTIONS")
print("=" * 60)

# =============================================================================
# PRACTICE QUESTION 1: PASSWORD VALIDATOR
# =============================================================================
print("\n📝 PRACTICE 1: Password Validator")
print("-" * 40)
print("Create a password validator that keeps asking until requirements are met")
print("Requirements: At least 8 characters, contains both letters and numbers")

# =============================================================================
# PRACTICE QUESTIONS WITH SOLUTIONS (NO FUNCTIONS - SIMPLE CODE)
# =============================================================================

print("\n" + "=" * 60)
print("🎯 PRACTICE QUESTIONS WITH SIMPLE SOLUTIONS")
print("=" * 60)

# =============================================================================
# PRACTICE QUESTION 1: PASSWORD VALIDATOR
# =============================================================================
print("\n📝 PRACTICE 1: Password Validator")
print("-" * 40)
print("Create a password validator that keeps asking until requirements are met")
print("Requirements: At least 8 characters, contains both letters and numbers")

print("\nSOLUTION:")
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter a password (min 8 chars, letters + numbers): ")
    attempts = attempts + 1
    
    # Check length
    if len(password) < 8:
        print("❌ Password too short! Need at least 8 characters.")
    else:
        # Check for letters and numbers
        has_letter = False
        has_number = False
        
        # Check each character in password
        i = 0
        while i < len(password):
            if password[i].isalpha():
                has_letter = True
            if password[i].isdigit():
                has_number = True
            i = i + 1
        
        if has_letter and has_number:
            print("✅ Password accepted! Strong and secure.")
            break
        else:
            print("❌ Password must contain both letters and numbers.")
    
    if attempts == max_attempts:
        print("❌ Maximum attempts reached. Access denied.")

print()

# =============================================================================
# PRACTICE QUESTION 2: NUMBER GUESSING GAME
# =============================================================================
print("\n📝 PRACTICE 2: Number Guessing Game")
print("-" * 40)
print("Create a guessing game where computer picks random number 1-100")

print("\nSOLUTION:")
import random
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print(f"🎯 I'm thinking of a number between 1 and 100!")
print(f"You have {max_attempts} attempts to guess it.")

while attempts < max_attempts:
    guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
    attempts = attempts + 1
    
    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("📈 Too low! Try a higher number.")
    else:
        print("📉 Too high! Try a lower number.")
        
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"💡 {remaining} attempts remaining.")

if attempts == max_attempts and guess != secret_number:
    print(f"💀 Game Over! The number was {secret_number}")

print()

# =============================================================================
# PRACTICE QUESTION 3: FACTORIAL CALCULATOR
# =============================================================================
print("\n📝 PRACTICE 3: Factorial Calculator")
print("-" * 40)
print("Calculate factorial using while loop (e.g., 5! = 5×4×3×2×1 = 120)")

print("\nSOLUTION:")
num = int(input("Enter a positive number: "))

if num < 0:
    print("❌ Please enter a positive number!")
else:
    # Calculate factorial
    factorial = 1
    original_num = num
    calculation_steps = ""
    
    while num > 0:
        if calculation_steps == "":
            calculation_steps = str(num)
        else:
            calculation_steps = calculation_steps + " × " + str(num)
        factorial = factorial * num
        num = num - 1
    
    print(f"✅ {original_num}! = {calculation_steps} = {factorial}")

print()

# =============================================================================
# PRACTICE QUESTION 4: REVERSE STRING
# =============================================================================
print("\n📝 PRACTICE 4: String Reverser")
print("-" * 40)
print("Reverse a string using while loop character by character")

print("\nSOLUTION:")
text = input("Enter text to reverse: ")

if text == "":
    print("❌ Please enter some text!")
else:
    # Reverse using while loop
    reversed_text = ""
    index = len(text) - 1
    
    print(f"🔄 Reversing '{text}' step by step:")
    step = 1
    while index >= 0:
        reversed_text = reversed_text + text[index]
        print(f"   Step {step}: Added '{text[index]}' → '{reversed_text}'")
        index = index - 1
        step = step + 1
        
    print(f"✅ Final result: '{reversed_text}'")

print()

# =============================================================================
# PRACTICE QUESTION 5: PRIME NUMBER FINDER
# =============================================================================
print("\n📝 PRACTICE 5: Prime Number Finder")
print("-" * 40)
print("Find all prime numbers up to a given number using while loops")

print("\nSOLUTION:")
limit = int(input("Find all prime numbers up to: "))

if limit < 2:
    print("❌ Please enter a number >= 2")
else:
    print(f"\n🔍 Finding prime numbers up to {limit}:")
    primes_found = []
    current = 2
    
    while current <= limit:
        # Check if current number is prime
        is_prime = True
        divisor = 2
        
        # Only need to check up to square root
        while divisor * divisor <= current:
            if current % divisor == 0:
                is_prime = False
                break
            divisor = divisor + 1
            
        if is_prime:
            primes_found.append(current)
            print(f"✅ {current} is prime")
        
        current = current + 1
        
    print(f"\n🎯 Found {len(primes_found)} prime numbers: {primes_found}")

print()

# =============================================================================
# PRACTICE QUESTION 6: FIBONACCI SEQUENCE
# =============================================================================
print("\n📝 PRACTICE 6: Fibonacci Sequence Generator")
print("-" * 40)
print("Generate Fibonacci sequence up to n terms using while loop")

print("\nSOLUTION:")
n = int(input("How many Fibonacci numbers to generate? "))

if n <= 0:
    print("❌ Please enter a positive number!")
else:
    print(f"\n🌀 Generating first {n} Fibonacci numbers:")
    
    # Initialize
    a = 0
    b = 1
    count = 0
    fibonacci_sequence = []
    
    while count < n:
        if count == 0:
            fibonacci_sequence.append(a)
            print(f"F({count}) = {a}")
        elif count == 1:
            fibonacci_sequence.append(b)
            print(f"F({count}) = {b}")
        else:
            next_fib = a + b
            fibonacci_sequence.append(next_fib)
            print(f"F({count}) = {a} + {b} = {next_fib}")
            a = b
            b = next_fib
            
        count = count + 1
        
    print(f"\n✅ Fibonacci sequence: {fibonacci_sequence}")

print()

# =============================================================================
# PRACTICE QUESTION 7: DIGITAL ROOT CALCULATOR
# =============================================================================
print("\n📝 PRACTICE 7: Digital Root Calculator")
print("-" * 40)
print("Calculate digital root (keep adding digits until single digit)")

print("\nSOLUTION:")
num = int(input("Enter a number: "))

if num < 0:
    print("❌ Please enter a positive number!")
else:
    original_num = num
    step = 1
    
    print(f"\n🧮 Calculating digital root of {original_num}:")
    
    while num >= 10:
        digit_sum = 0
        temp = num
        digits = []
        
        # Extract and sum all digits
        while temp > 0:
            digit = temp % 10
            digits.insert(0, str(digit))  # Insert at beginning to maintain order
            digit_sum = digit_sum + digit
            temp = temp // 10
            
        digit_string = " + ".join(digits)
        print(f"Step {step}: {digit_string} = {digit_sum}")
        num = digit_sum
        step = step + 1
        
    print(f"✅ Digital root of {original_num} is: {num}")

print()

# =============================================================================
# PRACTICE QUESTION 8: PATTERN GENERATOR
# =============================================================================
print("\n📝 PRACTICE 8: Pattern Generator")
print("-" * 40)
print("Generate various patterns using nested while loops")

print("\nSOLUTION - Right Triangle Pattern:")
size = int(input("Enter pattern size: "))

if size <= 0:
    print("❌ Size must be positive!")
else:
    print("\nRight Triangle Pattern:")
    row = 1
    while row <= size:
        col = 1
        while col <= row:
            print("* ", end="")
            col = col + 1
        print()  # New line after each row
        row = row + 1

print()

print("Number Triangle Pattern:")
row = 1
while row <= size:
    col = 1
    while col <= row:
        print(f"{col} ", end="")
        col = col + 1
    print()  # New line after each row
    row = row + 1

print()

# =============================================================================
# SIMPLE COUNTING EXERCISES
# =============================================================================
print("\n📝 SIMPLE COUNTING EXERCISES")
print("-" * 40)

print("\n1. Count from 10 to 1 (countdown):")
countdown = 10
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown = countdown - 1
print("🚀 Blast off!")

print()

print("\n2. Count even numbers from 2 to 20:")
even_num = 2
while even_num <= 20:
    print(f"Even number: {even_num}")
    even_num = even_num + 2

print()

print("\n3. Add numbers from 1 to 10:")
total = 0
current = 1
while current <= 10:
    total = total + current
    print(f"Added {current}, Total so far: {total}")
    current = current + 1
print(f"Final sum: {total}")

print()

print("\n4. Multiplication table of 5:")
multiplier = 1
while multiplier <= 10:
    result = 5 * multiplier
    print(f"5 × {multiplier} = {result}")
    multiplier = multiplier + 1

print()

# =============================================================================
# SIMPLE INPUT VALIDATION EXAMPLES
# =============================================================================
print("\n📝 INPUT VALIDATION EXAMPLES")
print("-" * 40)

print("\n1. Keep asking for positive number:")
number = -1
while number <= 0:
    number = int(input("Enter a positive number: "))
    if number <= 0:
        print("❌ That's not positive! Try again.")
print(f"✅ Great! You entered: {number}")

print()

print("\n2. Keep asking until user says 'yes':")
answer = ""
while answer.lower() != "yes":
    answer = input("Do you want to continue? (yes/no): ")
    if answer.lower() != "yes":
        print("Please answer 'yes' to continue.")
print("✅ Thank you! Continuing...")

print()

print("\n3. Count how many times user enters 'hello':")
hello_count = 0
user_word = ""
while hello_count < 3:
    user_word = input("Say 'hello' (or 'stop' to quit): ")
    if user_word.lower() == "hello":
        hello_count = hello_count + 1
        print(f"Hello count: {hello_count}")
    elif user_word.lower() == "stop":
        break
    else:
        print("That's not 'hello'!")

print(f"You said hello {hello_count} times!")

print()

# =============================================================================
# SIMPLE GAME EXAMPLES
# =============================================================================
print("\n📝 SIMPLE GAME EXAMPLES")
print("-" * 40)

print("\n1. Simple Addition Game:")
score = 0
questions = 0
max_questions = 5

while questions < max_questions:
    # Generate random numbers
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 + num2
    
    user_answer = int(input(f"Question {questions + 1}: What is {num1} + {num2}? "))
    
    if user_answer == correct_answer:
        print("✅ Correct!")
        score = score + 1
    else:
        print(f"❌ Wrong! The answer was {correct_answer}")
    
    questions = questions + 1

print(f"\nGame Over! Your score: {score}/{max_questions}")

print()

print("\n2. Simple Rock Paper Scissors:")
player_wins = 0
computer_wins = 0
rounds = 0
max_rounds = 3

while rounds < max_rounds:
    print(f"\nRound {rounds + 1}")
    player_choice = input("Choose (rock/paper/scissors): ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("🏆 You win this round!")
        player_wins = player_wins + 1
    else:
        print("🤖 Computer wins this round!")
        computer_wins = computer_wins + 1
    
    rounds = rounds + 1

print(f"\nFinal Score:")
print(f"Player: {player_wins}")
print(f"Computer: {computer_wins}")

if player_wins > computer_wins:
    print("🎉 You are the champion!")
elif computer_wins > player_wins:
    print("🤖 Computer wins the game!")
else:
    print("🤝 It's a draw!")

print()

# =============================================================================
# SIMPLE WHILE LOOP CHALLENGES FOR BEGINNERS
# =============================================================================

print("\n" + "=" * 60)
print("🏆 BEGINNER CHALLENGES - Try These Yourself!")
print("=" * 60)

print("""
🎯 CHALLENGE 1: Count to 100 by 5s
Write a while loop that counts: 5, 10, 15, 20... up to 100

🎯 CHALLENGE 2: Sum of Even Numbers
Find the sum of all even numbers from 2 to 20

🎯 CHALLENGE 3: Multiplication Table
Create a multiplication table for any number (user input)

🎯 CHALLENGE 4: Password Checker
Keep asking for a password until user enters "secret123"

🎯 CHALLENGE 5: Letter Counter
Count how many times the letter 'a' appears in a word

🎯 CHALLENGE 6: Simple Calculator
Create a calculator that keeps working until user types "quit"

🎯 CHALLENGE 7: Number Pyramid
Create a number pyramid:
1
1 2
1 2 3
1 2 3 4

🎯 CHALLENGE 8: Reverse Counter
Count backwards from any number to 0

🎯 CHALLENGE 9: Find the Largest
Keep asking for numbers until user enters 0, then show the largest

🎯 CHALLENGE 10: Simple ATM
Create an ATM simulator with balance checking and withdrawals
""")

print("\n" + "=" * 60)
print("🎉 CONGRATULATIONS! You've learned While Loops!")
print("💡 Practice these challenges to become a Python pro!")
print("🚀 Next up: Learn about For Loops!")
print("=" * 60)



