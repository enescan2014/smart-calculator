"""
Smart Calculator - A menu-driven calculator with history
Run with: python calculator.py
Works in VS Code terminal or Jupyter: %run calculator.py
"""

import math
import os

history = []  # Stores last 10 calculations


def add_history(expression, result):
    history.append(f"{expression} = {result}")
    if len(history) > 10:
        history.pop(0)


def show_history():
    if not history:
        print("  No calculations yet.")
    else:
        print("\n  --- Last Calculations ---")
        for i, entry in enumerate(history, 1):
            print(f"  {i}. {entry}")


def basic_calc():
    print("\n  --- Basic Calculator ---")
    try:
        a = float(input("  First number: "))
        op = input("  Operation (+  -  *  /): ").strip()
        b = float(input("  Second number: "))

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                print("  Error: Cannot divide by zero!")
                return
            result = a / b
        else:
            print("  Unknown operation!")
            return

        # Round to avoid floating-point weirdness like 0.1 + 0.2 = 0.30000000000000004
        result = round(result, 10)
        print(f"\n  Result: {a} {op} {b} = {result}")
        add_history(f"{a} {op} {b}", result)

    except ValueError:
        print("  Please enter valid numbers!")


def scientific_calc():
    print("\n  --- Scientific Calculator ---")
    print("  Available: sqrt  power  log  log2  sin  cos  tan  factorial")
    op = input("  Operation: ").strip().lower()

    try:
        if op in ("sqrt", "log", "log2", "sin", "cos", "tan"):
            n = float(input("  Number: "))

            if op == "sqrt":
                if n < 0:
                    print("  Error: Square root of a negative number is imaginary!")
                    return
                result = math.sqrt(n)
                expr = f"sqrt({n})"

            elif op == "log":
                if n <= 0:
                    print("  Error: Log only works on positive numbers!")
                    return
                result = math.log10(n)
                expr = f"log10({n})"

            elif op == "log2":
                if n <= 0:
                    print("  Error: Log only works on positive numbers!")
                    return
                result = math.log2(n)
                expr = f"log2({n})"

            elif op == "sin":
                result = math.sin(math.radians(n))
                expr = f"sin({n}°)"

            elif op == "cos":
                result = math.cos(math.radians(n))
                expr = f"cos({n}°)"

            elif op == "tan":
                if n % 180 == 90:
                    print("  Error: tan(90°) is undefined!")
                    return
                result = math.tan(math.radians(n))
                expr = f"tan({n}°)"

        elif op == "power":
            base = float(input("  Base: "))
            exp = float(input("  Exponent: "))
            result = base ** exp
            expr = f"{base}^{exp}"

        elif op == "factorial":
            n = int(input("  Number (must be a whole number >= 0): "))
            if n < 0:
                print("  Error: Factorial is only defined for non-negative whole numbers!")
                return
            result = math.factorial(n)
            expr = f"{n}!"

        else:
            print("  Unknown operation!")
            return

        print(f"\n  Result: {expr} = {round(result, 8)}")
        add_history(expr, round(result, 8))

    except ValueError:
        print("  Please enter a valid number!")


def unit_converter():
    print("\n  --- Unit Converter ---")
    print("  1) km  → miles       2) miles → km")
    print("  3) kg  → pounds      4) pounds → kg")
    print("  5) °C  → °F          6) °F → °C")
    print("  7) m   → feet        8) feet  → m")

    conversions = {
        "1": (0.621371,     "km",     "miles"),
        "2": (1 / 0.621371, "miles",  "km"),
        "3": (2.20462,      "kg",     "pounds"),
        "4": (1 / 2.20462,  "pounds", "kg"),
        "7": (3.28084,      "m",      "feet"),
        "8": (1 / 3.28084,  "feet",   "m"),
    }

    try:
        choice = input("  Choose (1-8): ").strip()
        value = float(input("  Enter value: "))

        if choice in conversions:
            factor, from_unit, to_unit = conversions[choice]
            result = value * factor
            print(f"\n  Result: {value} {from_unit} = {result:.4f} {to_unit}")
            add_history(f"{value} {from_unit} to {to_unit}", f"{result:.4f}")

        elif choice == "5":
            result = (value * 9 / 5) + 32
            print(f"\n  Result: {value}°C = {result:.2f}°F")
            add_history(f"{value}°C to °F", f"{result:.2f}")

        elif choice == "6":
            result = (value - 32) * 5 / 9
            print(f"\n  Result: {value}°F = {result:.2f}°C")
            add_history(f"{value}°F to °C", f"{result:.2f}")

        else:
            print("  Invalid choice!")

    except ValueError:
        print("  Please enter a valid number!")


def main():
    print("=" * 48)
    print("         SMART CALCULATOR v1.0")
    print("=" * 48)

    running = True
    while running:
        print("\n  --- Main Menu ---")
        print("  1) Basic Calculator  (+, -, *, /)")
        print("  2) Scientific Calculator (sqrt, trig, etc.)")
        print("  3) Unit Converter")
        print("  4) View Calculation History")
        print("  5) Clear Screen")
        print("  6) Exit")

        choice = input("\n  Choose (1-6): ").strip()

        if choice == "1":
            basic_calc()
        elif choice == "2":
            scientific_calc()
        elif choice == "3":
            unit_converter()
        elif choice == "4":
            show_history()
        elif choice == "5":
            os.system("cls" if os.name == "nt" else "clear")
        elif choice == "6":
            print("  Thanks for using Smart Calculator! Goodbye.")
            running = False
        else:
            print("  Please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()
