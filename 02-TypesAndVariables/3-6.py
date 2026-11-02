import math
h = float(input("height: "))
d = 3.57 * math.sqrt(h)

print(f"Distance to the horizon: {d:.2f} km")

print("\nFor cases:")
print(f"1. At the beach (~1.7 m): {3.57 * math.sqrt(1.7):.2f} km")
print(f"2. From a hotel window (20 m): {3.57 * math.sqrt(20):.2f} km")
