list = [[1,2,3],
        [5,6,7],
       [8,9,10]]

G = (sum(row) for row in list)

# next() run the generator
for i in range(3):
    print i+1
    i = next(G)
    print i
