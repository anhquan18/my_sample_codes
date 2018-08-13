#Zip unite two or n different list into a list of tuple

chara_list = ['a','b','hel','no','yes']
num_list = range(1,20,4)
another_num = range(-1, -20, -4)

for name, num in zip(chara_list, num_list):
    print name, num

print zip(chara_list, num_list, another_num)
