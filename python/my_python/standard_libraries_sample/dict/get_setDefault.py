#Count with a dictionary

d = {}

colors = ['red', 'blue', 'black', 'green', 'red', 'blue', 'red', 'purple']

for color in colors:
    d[color] = d.get(color, 0) + 1

print d


#Groupt word by the length
dic = {}

for color in colors:
    key = len(color)
    if color not in dic.setdefault(key, []):
        dic[key].append(color)

print dic
