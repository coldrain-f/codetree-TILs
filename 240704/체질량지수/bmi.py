h, w = map(int, input().split())
bmi = (10000 * w) // (h * h)

print(bmi)
if bmi >= 25:
    print("Obesity")