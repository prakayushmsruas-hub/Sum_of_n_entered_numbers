print("SUM OF N NUMBERS")
sum=0
n=int(input("Enter How many numbers do you want to add:"))
for i in range(1,n+1):
     num=int(input(f"enter the number {i}:"))
     sum+=num
print("sum of",n,"numbers is",sum)        
