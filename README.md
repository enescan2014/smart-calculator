# smart-calculator
This is a very futuristic and smart calculator that calculates anything you need help with.

A calculator that does way more than just add and subtract. It has a main menu that loops until you choose to exit, so you can do calculation after calculation without restarting the program. I built this because our school calculator can't do unit conversions and I kept having to look them up online.

What Does It Do?

- Basic maths: addition, subtraction, multiplication, division (with divide-by-zero protection)
- Advanced maths: square root, powers, log base 10, log base 2, sin/cos/tan (in degrees), factoria,l etc
- Unit converter: km ↔ miles, kg ↔ pounds, °C ↔ °F, metres ↔ feet
- History log: remembers your last 10 calculations so you can refer back


Example

  --- Main Menu ---
  1) Basic Calculator
  2) Scientific Calculator
  3) Unit Converter
  4) View Calculation History
  5) Clear Screen
  6) Exit

  Choose (1-6):(eg:2)
  Operation: sqrt
  Number: 144
  Result: sqrt(144) = 12.0

 Python Concepts Used

- While loop with a flag: Instead of "while True: break", I use "running = True" and set "running = False" to exit. 
- Try/except: If someone types "hello" where a number is expected, "float("hello")" raises a "ValueError". The "except ValueError" block catches it and prints a friendly message instead of crashing.
- Python's built-in maths library. "math.sqrt()", "math.factorial()", "math.sin()" etc. I use Python's "math.sin()" .
- Dictionaries for lookup tables: The unit converter stores all 6 conversion factors in one dictionary. 
  
What I Learned
I learned about floating-point precision — I was confused why 0.1 + 0.2 != 0.3 until I read about how computers store decimal numbers in binary. The round() fix was the solution. 

For example, "round(result, 10)" Floating point numbers in computers aren't perfectly precise. 0.1 + 0.2 gives 0.30000000000000004 in Python. Sooo, rounding to 10 decimal places fixes these display issues.
