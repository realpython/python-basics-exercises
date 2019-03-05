# 6.5 - Challenge: Track Your Investments
# Solution to challenge


# Calculate compound interest to track the growth of an investment


def invest(amount, rate, time):
    print(f"principal amount: ${amount}")
    print("annual rate of return:", rate)
    for t in range(1, time + 1):
        amount = amount * (1 + rate)
        print(f"year {t}: ${amount:,.2f}")
    print()


invest(100, 0.05, 8)
invest(2000, 0.025, 5)
