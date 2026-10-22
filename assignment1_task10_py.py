from decimal import Decimal
from time import perf_counter


def total_float(payments):
    total = 0.0

    for payment in payments:
        total += float(payment)

    return total


def total_decimal(payments):
    total = Decimal("0.00")

    for payment in payments:
        total += Decimal(payment)

    return total


for n in (300, 6000, 150000):
    payments = ["33.40"] * n

    start = perf_counter()
    f_total = total_float(payments)
    f_time = perf_counter() - start

    start = perf_counter()
    d_total = total_decimal(payments)
    d_time = perf_counter() - start

    print("Payments:", n)
    print("Float total:", f_total)
    print("Float time:", f_time)

    print("Decimal total:", d_total)
    print("Decimal time:", d_time)
    print("--------------------")
