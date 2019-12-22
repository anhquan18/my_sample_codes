import time
import matplotlib.pyplot as plt

class Robot(object):
    def __init__(self):
        self.pose = [(x, y) for x in range(100) for y in range(100)]

r = Robot()

#print sum(i **2 for i in range(10))
start = time.time()
#a = [(x, y) for x in range(50) for y in range(50)]
pose_x = [x[0] for x in r.pose]
pose_y = [x[1] for x in r.pose]

plt.scatter(pose_x, pose_y)
plt.show()
print ("Time:", time.time() - start)
