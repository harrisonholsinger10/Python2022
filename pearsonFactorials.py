num = int(input("Enter a nonnegative integer:"))
total = 1

if num == 0:
    print("0")
for i in range(num, 0, -1):
    total = total * i
    
print(total)