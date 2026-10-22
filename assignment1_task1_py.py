def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total

from decimal import Decimal
import sys

# 1,000 payments of Rs 33.40 and three small adjustments of Rs 0.10
payments = ["33.40"] * 1000 + ["0.10"] * 3


def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total


def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total


print("float  :", total_float(payments))
print("Decimal:", total_decimal(payments))
print(0.1 + 0.2 == 0.3,
      Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

# Change Decimal(amount) to Decimal(float(amount))
def total_decimal_from_float(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(float(amount))
    return total

print("Decimal from float:", total_decimal_from_float(payments))

# Alternative: store money as integer paise
total_paise = sum(int(Decimal(amount) * 100) for amount in payments)
print("Integer paise: Rs.", total_paise // 100, "and", total_paise % 100, "paise")

# Compare memory sizes
print("Size of float:", sys.getsizeof(0.0), "bytes")
print("Size of Decimal:", sys.getsizeof(Decimal("0.00")), "bytes")
print("Size of int:", sys.getsizeof(0), "bytes")
