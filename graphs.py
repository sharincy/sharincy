import matplotlib.pyplot as mpl
x = [0,10,20,30,40]
y = [0,20,11,34,37]
mpl.xlabel('Hours spent on gaming',color='pink')
mpl.ylabel('My ability',color='green')
mpl.title('Trend',color='lightblue')
mpl.plot(x,y)
mpl.show()

