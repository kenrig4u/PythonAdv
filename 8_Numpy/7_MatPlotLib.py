# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 22:45:05 2018

@author: SilverDoe
"""

'''

>> graphing and data visualization module.

	
============Formatting characters =============================================

'-'   Solid line style

'--'  Dashed line style

'-.'  Dash-dot line style

':'   Dotted line style

'.'   Point marker

','   Pixel marker

'o'   Circle marker

'v'   Triangle_down marker

'^'   Triangle_up marker

'<'   Triangle_left marker

'>'   Triangle_right marker

'1'   Tri_down marker

'2'   Tri_up marker

'3'   Tri_left marker

'4'   Tri_right marker

's'   Square marker

'p'   Pentagon marker

'*'   Star marker

'h'   Hexagon1 marker

'H'   Hexagon2 marker

'+'   Plus marker

'x'   X marker

'D'   Diamond marker

'd'   Thin_diamond marker

'|'   Vline marker

'_'   Hline marker

====================== color ==================================================

'b' 	Blue

'g' 	Green

'r' 	Red

'c'	   Cyan

'm'	   Magenta

'y'	   Yellow

'k'	   Black

'w'	   White


'''

import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(2010,2019)
y = np.array([9,2,1,1,3,2,3.3,4,5])
plt.title("LifePlot") 
plt.xlabel("Year") 
plt.ylabel("Life") 
plt.plot(x,y)#============
plt.show()


plt.plot(x,y,"og")#==========


t = np.arange(0.,5.,0.2)

# red dashes, blue squares and green triangles
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()

'''======================== Trigonometric functions ==========================='''
import numpy as np 
from matplotlib import pyplot as plt

a = np.arange(0,360)
x =a*np.pi/180 

y = np.sin(x)
plt.title("Wave") 
plt.xlabel("Phase Angle") 
plt.ylabel("Voltage") 
plt.plot(x,y)
plt.show()


'''======= Subplot ============================================================

>> used to plot two or more plots in one figure.
'''


import numpy as np 
import matplotlib.pyplot as plt  
   
a = np.arange(0,360)
x =a*np.pi/180 
 
y_sin = np.sin(x) 
y_cos = np.cos(x)  
   

#Horizontal subplot
plt.subplot(2, 1, 1)
plt.plot(x, y_sin) 
plt.title('Sine')  
   

plt.subplot(2, 1, 2) 
plt.plot(x, y_cos) 
plt.title('Cosine')  

plt.show()


# Vertical subplot
plt.subplot(1,2,1)
plt.plot(x, y_sin) 
plt.title('Sine') 

plt.subplot(1, 2, 2) 
plt.plot(x, y_cos) 
plt.title('Cosine')

plt.show()




# Subplot grid
plt.subplot(2,2,1)
plt.plot(x, y_sin) 
plt.title('Sine') 

plt.subplot(2,2,2) 
plt.plot(x, y_cos) 
plt.title('Cosine') 

plt.subplot(2,2,3)
plt.plot(x, y_sin) 
plt.title('Sine') 

plt.subplot(2,2,4)
plt.plot(x, y_cos) 
plt.title('Cosine') 

plt.show()


# subplot/multiplots and axis
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)

# pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')

plt.subplot(2,1,2)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.show()


'''=================== Bar Graph =============================================='''
import numpy as np
from matplotlib import pyplot as plt 

x = np.arange(2010,2019)
y = np.array([9,2,1,1,3,2,3.3,4,5])

plt.bar(x, y, color = 'b', align = 'center') 
plt.title('Life Bar') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  

plt.show()


'''================= Histogram ================================================'''

# working with text in plot s
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000) 

# the histogram of the data
n, bins, patches = plt.hist(x,100,normed=1,facecolor='g',alpha=0.2)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60,.010,r'$\mu=100,\ \sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()


'''=============== Histogram using Matplotlib ================================='''

import numpy as np 
from matplotlib import pyplot as plt 
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
plt.hist(a, bins = [0,20,40,60,80,100]) 
plt.title("histogram") 
plt.show()

'''============== Numpy Histogram ============================================='''
# A bin is range that represents the width of a single bar of the histogram along the X-axis
import numpy as np 
from matplotlib import pyplot as plt 
   
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
hist,bins = np.histogram(a,bins = [0,20,40,60,80,100]) 
print(hist)
print(bins)

# plotting histogram outputs on a linegraph
fig, ax = plt.subplots()
ax.plot(bins[:-1], hist)
fig.show()



'''============= Plot over an image ===========================================

You need the Python Imaging Library (PIL) but alas! the PIL project seems to have been abandoned.
 In particular, it hasn't been ported to Python 3. So if you want PIL functionality in Python 3,
 you'll do well do use Pillow, which is the semi-official fork of PIL and appears to be actively developed.

# pip install pillow
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
import matplotlib.cbook as cbook

np.random.seed(0)
x = np.random.uniform(0.0,10.0,15)
y = np.random.uniform(0.0,10.0,15)

datafile = cbook.get_sample_data('E:\\Documents\\NetBeansProjects\\CoreJava\\dataforfiles\\Sevlily.png')
img = imread(datafile)
plt.scatter(x,y,zorder=1)
plt.imshow(img, zorder=0, extent=[0.5, 8.0, 1.0, 7.0])
plt.show()

''' Pie Chart ===============================================================
'''
"""
===============
Basic pie chart
===============

Demo of a basic pie chart plus a few additional features.

In addition to the basic pie chart, this demo shows a few optional features:

    * slice labels
    * auto-labeling the percentage
    * offsetting a slice with "explode"
    * drop-shadow
    * custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.
"""
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.5, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

#=============================================================================
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import tkinter as Tk

  
class Window():
    def __init__(self, master):
        self.frame = Tk.Frame(master)
        self.f = Figure( figsize=(10, 9), dpi=80 )
        self.ax0 = self.f.add_axes( (0.05, .05, .50, .50), axisbg=(.75,.75,.75), frameon=False)
        self.ax1 = self.f.add_axes( (0.05, .55, .90, .45), axisbg=(.75,.75,.75), frameon=False)
        self.ax2 = self.f.add_axes( (0.55, .05, .50, .50), axisbg=(.75,.75,.75), frameon=False)
 
     
        self.ax0.set_xlabel( 'Time (s)' )
        self.ax0.set_ylabel( 'Frequency (Hz)' )
        self.ax0.plot(np.max(np.random.rand(100,10)*10,axis=1),"r-")
        self.ax1.plot(np.max(np.random.rand(100,10)*10,axis=1),"g-")
        self.ax2.pie(np.random.randn(10)*100)
 
          
        self.frame = Tk.Frame( root )
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
 
        self.canvas = FigureCanvasTkAgg(self.f, master=self.frame)
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.canvas.show()
     
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.frame )
        self.toolbar.pack()
        self.toolbar.update()
 
 
if __name__ == '__main__':
    root = Tk.Tk()
    app = Window(root)
    root.title( "MatplotLib with Tkinter" )
    root.update()
    root.deiconify()
    root.mainloop()

