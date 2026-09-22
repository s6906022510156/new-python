import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.plot(x,y, marker='o',linestyle='-',color='b')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('simple line plot')

plt.show()