def computepay(h, r):
    if h <= 40:
        result = h * r
    else:
        result = h * r + (h - 40) * (r * 0.5)
    return result

hrs = input("Enter Hours:")
rate = input("Enter Rates:")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay", p)