# Task 6: Organise the Logic into Functions

# Named constants (demonstration values)
BASE_RATE = 30.0
FAT_RATE = 0.40
SNF_RATE = 0.30
TOTAL_DAYS = 10


def rate_per_litre(fat, snf):
    """Calculate and return the milk rate per litre."""
    rate = BASE_RATE + (FAT_RATE * fat) + (SNF_RATE * snf)
    return rate


def payout(litres, rate):
    """Calculate and return the payment for the given litres."""
    amount = litres * rate
    return amount


def ten_day_total(entries):
    """Calculate and return the total payment for all entries."""
    total = 0.0

    for entry in entries:
        litres, fat, snf = entry
        rate = rate_per_litre(fat, snf)
        total += payout(litres, rate)

    return total


def main():
    """Read ten days of entries and display payment details."""
    farmer_id = input("Enter Farmer ID: ").strip()
    entries = []

    for day in range(1, TOTAL_DAYS + 1):
        print("\nDay", day)

        litres = float(input("Enter litres: "))
        fat = float(input("Enter fat percentage: "))
        snf = float(input("Enter SNF percentage: "))

        entries.append((litres, fat, snf))

        rate = rate_per_litre(fat, snf)
        amount = payout(litres, rate)

        print(f"Rate per litre: Rs.{rate:.2f}")
        print(f"Payment amount: Rs.{amount:.2f}")

    total = ten_day_total(entries)

    print("\n------ TEN-DAY PAYMENT SUMMARY ------")
    print("Farmer ID:", farmer_id)
    print(f"Ten-day total: Rs.{total:.2f}")


main()

def payout(litres, rate):
    """Return the payment amount."""
    return litres * rate

amount = payout(10, 34.35)
print(amount)

