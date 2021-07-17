#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:12:40 2019

@author: xudansha
"""
import sys
t = float(sys.argv[1])
v0 = float(sys.argv[2])
g = 9.81
y = v0*t - 0.5*g*t**2
print y