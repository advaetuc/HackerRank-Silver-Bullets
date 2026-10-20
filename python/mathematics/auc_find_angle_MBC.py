import math

ab = int(input())
bc = int(input())

ac = math.sqrt(ab**2 + bc**2)

angle_rad = math.asin(ab / ac)

angle_deg = math.degrees(angle_rad)

print(f"{round(angle_deg)}" + chr(176))
