# SUBSTRING EXAMPLES

## Basic strings for examples
text = "Hello World Python Programming"
sentence = "Python is awesome for programming"

### 1. Basic substring using slicing [start:end]
print("\n=== BASIC SUBSTRING ===")
substring1 = text[0:5]      # From index 0 to 4 (5 not included)
print(f"text[0:5] = '{substring1}'")

### 2. Substring from start [start:]
print("\n=== FROM START ===")
from_start1 = text[6:]      # From index 6 to end
print(f"text[6:] = '{from_start1}'")

### 3. Substring to end [:end]
print("\n=== TO END ===")
to_end1 = text[:5]          # From start to index 4
print(f"text[:5] = '{to_end1}'")

### 4. Negative indexing
print("\n=== NEGATIVE INDEXING ===")
last_chars = text[-11:]     # Last 11 characters
print(f"text[-11:] = '{last_chars}'")

### 5. Step/stride in substring [start:end:step]
print("\n=== WITH STEP ===")
partial_reverse = text[5:15:2]  # Every second char from index 5 to 14
print(f"text[5:15:2] = '{partial_reverse}'")

### 6. Using substring methods
print("\n=== SUBSTRING METHODS ===")

### Check if substring exists
print(f"'Python' in sentence: {'Python' in sentence}")
print(f"'Java' in sentence: {'Java' in sentence}")

### Find substring position
python_pos = sentence.find('Python')
print(f"Position of 'Python': {python_pos}")

### Count occurrences
test_string = "banana"
count_a = test_string.count('a')
print(f"Count of 'a' in 'banana': {count_a}")

### Replace substring
original = "I love Java programming"
replaced = original.replace('Java', 'Python')
print(f"Original: '{original}'")
print(f"Replaced: '{replaced}'")