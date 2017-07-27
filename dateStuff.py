#from time import gmtime, strftime
#strftime("%Y-%m-%d %H:%M:%S", gmtime())


#from datetime import datetime
import datetime
import matplotlib.pyplot as plt

a=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(a)

time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

x=['2017-07-27 11:38:53', '2017-07-27 11:39:00','2017-07-27 11:39:08', '2017-07-27 11:40:02']
x=['2017-07-27 11:38:53', '2017-07-27 11:39:00','2017-07-27 11:39:08', '2017-07-27 11:40:02']
y=[0, 1, 1, 0]
x2 = [datetime.strptime(elem, '%Y-%m-%d %H:%M:%S') for elem in x]
dates=matplotlib.dates.date2num(x2)

plt.plot_date(dates, y)

(fig, ax) = plt.subplots(1, 1)
ax.plot(x, y)
fig.show()

