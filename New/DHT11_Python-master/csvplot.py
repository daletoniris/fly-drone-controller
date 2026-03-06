import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def graph():
    Archi1 = raw_input("input archive name ex: test.csv: ")
    time, value,  = np.loadtxt(Archi1, delimiter=',', unpack=True, converters = {0: mdates.strpdate2num("%H:%M:%S")})

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1, axisbg='white')
    plt.plot_date(x=time, y=value, fmt='-')
    plt.title('temp y hum plot')
    plt.ylabel('value')	
    plt.xlabel('date')
    plt.show()
graph()    
