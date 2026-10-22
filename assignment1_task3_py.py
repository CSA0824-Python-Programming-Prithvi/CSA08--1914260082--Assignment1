# Named constants
BASE_RATE = 30.0
FAT_RATE = 0.40
SNF_RATE = 0.30
MIN_FAT = 2.0
MAX_FAT = 7.0
TOTAL_DAYS = 10

# Get input from the user
farmer_id = input("Enter Farmer ID: ")
litres = float(input("Enter litres of milk: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))

# Calculate rate using named constants
rate = BASE_RATE + (FAT_RATE * fat) + (SNF_RATE * snf)
amount = litres * rate

print("\n--- Payment Details ---")
print("Farmer ID:", farmer_id)
print(f"Rate per litre: Rs.{rate:.2f}")
print(f"Payment amount: Rs.{amount:.2f}")

# Demonstrate dynamic typing
value = 100
print("\nInteger value:", value, type(value))

value = "Python"
print("String value:", value, type(value))

# Demonstrate multiple assignment
a, b = 10, 20
print("\nBefore swapping:", a, b)

# Swap the values
a, b = b, a
print("After swapping:", a, b)

# Alternative: dictionary rate card
RATE_CARD = {
    "base": 30.0,
    "fat": 0.40,
    "snf": 0.30
}
print("\nRate card:", RATE_CARD)

value = 100
print(type(value))

value = "Python"
print(type(value))

a, b = 10, 20
a, b = b, a
