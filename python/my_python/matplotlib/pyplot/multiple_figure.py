import time 
import matplotlib.pyplot as plt

plt.figure(1)   # Call out figure 1 and make it current
axes1_1 = plt.subplot(211)# Call out plot 1 and make it current
plt.plot(range(4))

axes1_2 = plt.subplot(212)# Call out plot 2 and make it current
plt.plot(range(4,8))

plt.figure(2)   # Call out figure 2 and make it current
plt.plot(range(10), range(10))

plt.figure(1)   # Make figure 1 current, subplot 212 still current 
plt.subplot(211)# Make subplot 1 current call this out the second time will return an error since you
# are overwritting the axes
plt.title('Easy as 1 2 3')
plt.show()

print 'sleep now'
time.sleep(3)
print 'clf now'
# plt.clf()   clear figure
# plt.cla()   clear axes

plt.show()
