from decimal import Decimal, ROUND_HALF_UP

STEP_SIZE = Decimal("0.1")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")

RATE_CARDS = {
    "regular": {
        "base": Decimal("30.00"),
        "fat": Decimal("0.40"),
        "snf": Decimal("0.30")
    },
    "april_june": {
        "base": Decimal("32.00"),
        "fat": Decimal("0.45"),
        "snf": Decimal("0.30")
    }
}

BONUS_RATE = Decimal("0.50")
BONUS_LIMIT = Decimal("500")


def rate_per_litre(fat, snf, season="regular"):
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    if season not in RATE_CARDS:
        raise ValueError("Invalid season")

    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("Invalid fat")

    if snf < 0:
        raise ValueError("Invalid SNF")

    fat_steps = ((fat - STANDARD_FAT) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )

    snf_steps = ((snf - STANDARD_SNF) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )

    card = RATE_CARDS[season]

    rate = card["base"] + fat_steps * card["fat"]
    rate += snf_steps * card["snf"]

    return rate.quantize(Decimal("0.01"))


def payout(litres, fat, snf, season="regular"):
    litres = Decimal(str(litres))

    if litres < 0:
        raise ValueError("Invalid litres")

    rate = rate_per_litre(fat, snf, season)

    return (litres * rate).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )


def ten_day_payment(entries, season="regular"):
    total_litres = sum(
        (Decimal(str(e[0])) for e in entries), Decimal("0")
    )

    base_total = sum(
        (payout(litres, fat, snf, season) for litres, fat, snf in entries),
        Decimal("0.00")
    )

    bonus = Decimal("0.00")

    if total_litres > BONUS_LIMIT:
        bonus = (total_litres * BONUS_RATE).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

    final_total = base_total + bonus

    return base_total, bonus, final_total


entries = [
    ("250.00", "4.25", "8.65"),
    ("260.50", "3.55", "8.50")
]

base, bonus, final = ten_day_payment(
    entries, "april_june"
)

print("Base payment:", base)
print("Bonus:", bonus)
print("Final payment:", final)
