n=5
k = 2*n - 2

for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")

print()



m=5
num = 65
for i in range(0, m):
    for j in range(0, i+1):
        ch = chr(num)
        print(ch, end=" ")
        num = num +1
    print("\r")


