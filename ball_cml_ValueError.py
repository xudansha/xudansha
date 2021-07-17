#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:28:29 2019

@author: xudansha
"""

import sys
g = 9.81

try:
    t = float(sys.argv[1])
    v0 = float(sys.argv[2])
except IndexError:
    print 'Please enter t and v0 on the command line.'
    t = float(raw_input('t = ?\n'))
    v0 = float(raw_input('v0 = ?\n'))

if t<0 or t>2*v0*g:
    raise ValueError('t is not between 0 and 2v0/g. Calculation is aborted.')
    sys.exit(1)

y = v0*t - 0.5*g*t**2
print y