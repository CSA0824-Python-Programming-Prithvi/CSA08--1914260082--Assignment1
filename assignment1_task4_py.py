
# Task 4: Write Correct Expressions
import math

# Named constants (demonstration assumptions)
BASE_RATE = 30.0
FAT_STEP_RATE = 0.40
SNF_STEP_RATE = 0.30
FAT_BASE = 3.5
SNF_BASE = 8.0
STEP_SIZE = 0.1

# User inputs
litres = float(input("Enter litres of milk: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))

# Calculate fat and SNF steps
fat_steps = round((fat - FAT_BASE) / STEP_SIZE)
snf_steps = round((snf - SNF_BASE) / STEP_SIZE)

# Calculate rate and payment amount
rate = BASE_RATE + fat_steps * FAT_STEP_RATE + snf_steps * SNF_STEP_RATE
amount = litres * rate

print("\n--- Payment Details ---")
print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print(f"Rate per litre: Rs.{rate:.2f}")
print(f"Amount: Rs.{amount:.2f}")

# Demonstrate floating-point surprises
print("\n--- Floating-point surprises ---")
print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
print("(3.1 - 3.5) / 0.1 =", (3.1 - 3.5) / 0.1)
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)

# Compare round(), int(), and math.floor()
for fat_value in (4.2, 3.1):
    steps = (fat_value - FAT_BASE) / STEP_SIZE
    print("\nFat:", fat_value, "Raw steps:", steps)
    print("round():", round(steps))
    print("int():", int(steps))
    print("math.floor():", math.floor(steps))

(4.2 - 3.5) / 0.1
0.1 + 0.2
-7 // 2
import math

for fat_value in (4.2, 3.1):
    steps = (fat_value - 3.5) / 0.1
    print(fat_value, round(steps), int(steps), math.floor(steps))
2.0 <= fat <= 7.0
fat >= 2.0 and fat <= 7.0
