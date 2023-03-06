hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

if h <= 40:
    pay = h * rate
else:
    pay = 40 * r + (h - 40) * r * 1.5

print(pay)