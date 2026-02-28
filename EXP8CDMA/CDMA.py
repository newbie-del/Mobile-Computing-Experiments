import numpy as np

# Chips/Codes define karna
c1 = [1, 1, 1, 1]
c2 = [1, -1, 1, -1]
c3 = [1, 1, -1, -1]
c4 = [1, -1, -1, 1]
rc = []

print("Enter the data bits (Example: 1 or -1 or 0):")
d1 = int(input("Enter D1 :"))
d2 = int(input("Enter D2 :"))
d3 = int(input("Enter D3 :"))
d4 = int(input("Enter D4 :"))

# Data ko chips se multiply karna
r1 = np.multiply(c1, d1)
r2 = np.multiply(c2, d2)
r3 = np.multiply(c3, d3)
r4 = np.multiply(c4, d4)

# Saare signals ko jod kar resultant channel banana
resultant_channel = r1 + r2 + r3 + r4
print("Resultant Channel", resultant_channel)

# Station select karna
Channel = int(input("Enter the station to listen for (C1=1, C2=2, C3=3, C4=4): "))

# Indentation (Space) yahan sahi ki gayi hai:
if Channel == 1:
    rc = c1
elif Channel == 2:
    rc = c2
elif Channel == 3:
    rc = c3
elif Channel == 4:
    rc = c4

# Decoding process
inner_product = np.multiply(resultant_channel, rc)
print("Inner Product", inner_product)

res1 = sum(inner_product)
data = res1 / len(inner_product)
print("Data bit that was sent:", data)
