from numpy import *
from matplotlib.pyplot import *
import sys

try:
    """slicing does not give an IndexError,
    but simply returns an empty list if the list
    is too short."""
    v0_list = sys.argv[1:]
    if v0_list == []:
        raise IndexError
    
except IndexError:
    print "You must provide a value for v0 as a command line argument"
    sys.exit(1)

g = 9.81

max_t = 0
max_y = 0

for v0 in v0_list:
    v0 = float(v0)
    t = linspace(0, 2*v0/g, 100)
    if max(t) > max_t:
        max_t = max(t)
    y = v0*t -0.5*g*t**2
    if max(y) > max_y:
        max_y = max(y)
    plot(t,y,label='v0=%g' %v0)
    
xlabel('time (s)')
ylabel('height (m)')
legend()
axis([0, max_t, 0, 1.1*max_y])

show()
print "Maximum of t is %.1f seconds. Maximum of height is %.1f meter." %(max_t, max_y)