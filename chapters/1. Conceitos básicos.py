# :tada:
print("Hello World!");

# Examples of main variable types in Python

## 1. NUMBERS (int, float)
age = 25                      # Integer number
height = 1.75                 # Decimal number (float)
temperature = -10             # Negative number

print("=== NUMBERS ===")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Temperature: {temperature}")

## 2. STRING (text)
name = "John Smith"           # String with double quotes
city = 'New York'             # String with single quotes
description = """Text with
multiple lines"""             # Multiline string

print("\n=== STRINGS ===")
print(f"Name: {name}")
print(f"City: {city}")
print(f"Description: {description}")

## 3. BOOLEAN (True/False)
is_raining = True
has_sun = False
is_adult = age >= 18          # Result of a comparison

print("\n=== BOOLEANS ===")
print(f"Is raining: {is_raining}")
print(f"Has sun: {has_sun}")
print(f"Is adult: {is_adult}")

## 4. LIST (mutable, ordered)
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["text", 42, True, 3.14]  # List can have different types

print("\n=== LISTS ===")
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed list: {mixed}")

### List operations
fruits.append("grape")        # Add item
print(f"Fruits after adding grape: {fruits}")
print(f"First fruit: {fruits[0]}")

## 5. TUPLE (immutable, ordered)
coordinates = (10, 20)
rgb_colors = (255, 128, 0)
person_data = ("Mary", 30, "Engineer")

print("\n=== TUPLES ===")
print(f"Coordinates: {coordinates}")
print(f"RGB colors: {rgb_colors}")
print(f"Person data: {person_data}")

### Accessing tuple elements
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")

## 6. DICTIONARY (key-value)
person = {
    "name": "Anna Costa",
    "age": 28,
    "profession": "Developer",
    "active": True
}

settings = {
    "theme": "dark",
    "language": "english",
    "notifications": True,
    "volume": 0.8
}

print("\n=== DICTIONARIES ===")
print(f"Person: {person}")
print(f"Settings: {settings}")

### Accessing dictionary values
print(f"Person name: {person['name']}")
print(f"Theme: {settings.get('theme')}")

### Adding new key
person["email"] = "anna@email.com"
print(f"Person with email: {person}")

# Debugging

## Function wrong
def multiply_wrong(number1, number2):
    result = number1 ** number2 # breakpoint
    return result

result1 = multiply_wrong(5, 3)
print(f"5 × 3 = {result1}")

## Correct function
def multiply(number1, number2):
    result = number1 * number2 # breakpoint
    return result

result1 = multiply(5, 3)
print(f"5 × 3 = {result1}")

## ESCAPE CHARACTERS EXAMPLES

### \n - New line (line break)
print("=== \\n EXAMPLES (New Line) ===")
print("First line\nSecond line\nThird line")

### \t - Tab (horizontal spacing)
print("\n=== \\t EXAMPLES (Tab) ===")
print("Name\tAge\tCity")

### \r - Carriage return (moves cursor to beginning of line)
print("\n=== \\r EXAMPLES (Carriage Return) ===")
print("Loading...\rComplete!")  # "Loading..." gets overwritten

## Exercises

### 1. Christmas tree in CII Art. ASCII
print("           ⭐           ")
print("          🍃🍃          ")
print("         🍃🎀🍃        ")
print("        🍃🍃🍃🍃        ")
print("       🎁🍃🎁🍃🎁       ")
print("      🍃🍃🍃🍃🍃🍃      ")
print("     🍃❄️🍃❄️🍃❄️🍃❄️🍃     ")
print("    🍃🍃🍃🍃🍃🍃🍃🍃    ")
print("   🔔🍃🔔🍃🔔🍃🔔🍃🔔   ")
print("  🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃  ")
print(" 🍃⛄🍃⛄🍃⛄🍃⛄🍃⛄🍃 ")
print("🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃")
 
## 2. BRL to USD

def convert_brl_to_usd(brl_amount, exchange_rate):
    usd_amount = brl_amount / exchange_rate
    return usd_amount

brl_amount = 100
exchange_rate = 5.0
usd_amount = convert_brl_to_usd(brl_amount, exchange_rate)
print(f"{brl_amount} BRL is equal to {usd_amount:.2f} USD")

## 3. String repeat
print("I need study Python 🐍\n" * 10)