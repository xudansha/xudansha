import numpy
from matplotlib.pyplot import plot, xlabel, ylabel, show,legend 
import sys

g = 9.81

try:
    v0_list = sys.argv[1:]
except:
    print "Please enter numbers for initial velocity."
    sys.exit()

def f(t,v0):
    return v0 * t - 0.5 * g * t ** 2

for v0 in v0_list:
    v0 = float(v0)
    tlist = numpy.linspace(0, 2 * v0 / g, 100)
    ylist = f(tlist,v0)
    plot (tlist, ylist, label = 'v0 = %g' %(v0))

xlabel("time (s)")
ylabel("height (m)")
legend()
show()
