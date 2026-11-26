numList = []
total = 0

for i in range(20):    
    number = int(input("Enter number {} of 20: ".format(i+1)))
    numList.append(number)
    total += number
    i += 1
    
low = min(numList)
high = max(numList)
avg = format(float(total / i), '.2f')

print("Low: ", low)
print("High: ", high)
print("Total: ", total)
print("Average: ", avg) 

input("press enter")
