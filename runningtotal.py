numbers=[10,20,30,40]
total=0
for num in numbers:
    total=total+num
    print("Running Total:",total)
    

n=int(input("how many numbers? "))
total=0
for i in range(n):
    num=int(input("Enter number: "))
    total += num
    print("Running Total:",total)



numbers=[10,20,30,40]
total=0
for num in numbers:
    total += num
    print("Final Total:",total)
