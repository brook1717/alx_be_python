number = int(input("Enter the size of the pattern: "))
i=0
while i<number:
    j=1
    for j in range(number):
        print("*", end="")
    i+=1
    print("\n")