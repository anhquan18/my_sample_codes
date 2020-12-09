import sys

num = int(sys.argv[1])
prime_nums = []

for num1 in range(2, num+1):
    for num2 in range(2, (num1/2)+1):
        if num1%num2 == 0:
            break
    else:
        prime_nums.append(num1)

