from math import pi

dec = int(input("Enter the amount of decimal places of pi to be represented as a fraction: "))
newpi = float("3.0" if dec == 0 else str(pi)[:dec+2])
num = 1
den = 1

while True:
    frac = num/den
    if str(newpi) in str(frac):
        break
    if frac > newpi:
        den += 1
    else:
        num += 1

print(f"Fraction: {num}/{den} ({num/den})")
print(f"Selected digits of pi: {newpi}")