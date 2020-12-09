import sys

a = sys.argv
for i in range(10):
    
    if a != []:
        print("There is a list")
        break;
else:
    print("Completed successfully. The list is empty")

# Normally we use a for loop to search an item and we found it we use if and break to get out
#of the loop. In here, we have 2 scenario, the for loop encounter the if and then break with
#the item being found. Or, the for loop run normally and didn't break and end without finding
#anything, that is when the else clause is executed
