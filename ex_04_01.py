def computepay(h, r):
    if h > 40:
        pay = 40 * r + (h - 40) * r * 1.5
        return pay
    else:
        pay = h * r
        return pay


hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter Rate:")
r = float(rph)

p = computepay(h ,r)
print("Pay:",p)
