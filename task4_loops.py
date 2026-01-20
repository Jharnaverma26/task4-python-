# 1. Use for loop to print numbers 1–100
for i in range(1, 101):
    print(i)

# 2. Use while loop for countdown timer
count = 5
while count > 0:
    print(count)
    count -= 1

# 3. Implement break and continue
for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)

# 4. Iterate over string characters
text = "Python"
for ch in text:
    print(ch)

# 5. Generate multiplication table
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 6. Use range with steps
for i in range(0, 21, 2):
    print(i)

# 7. Combine loop with conditions
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 8. Real-world example
students = ["Amit", "Riya", "Neha"]
for s in students:
    print(s, "is present")






