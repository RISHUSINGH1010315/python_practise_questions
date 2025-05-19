mark1 = int(input("Enter the number 1: "))
mark2 = int(input("Enter the number 2: "))
mark3 = int(input("Enter the number 3: "))

total_percentage = (100*(mark1 + mark2 + mark3))/300
if(total_percentage >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33):
    print("pass")
else:
    print("Fail try next time")    