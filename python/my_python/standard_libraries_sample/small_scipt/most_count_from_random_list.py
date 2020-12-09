import random

my_list = []
choose_list = []

for i in range(10000):
    choose_list.append(random.choice(my_list))

print("choosen one:", max(my_list, key=choose_list.count))
