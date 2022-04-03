from matplotlib import colors
import matplotlib.pyplot as wow
lb = ['Gaming','Study','Sleep','Going out','Relax']
time = [20,15,30,15,20]
wow.pie(time,labels=lb,colors=['lightgreen','lightblue','grey','pink','orange'])
wow.show()