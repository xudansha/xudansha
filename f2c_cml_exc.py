#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:16:24 2019

@author: xudansha
"""

import sys
try:
    F = float(sys.argv[1]) 
    C = 5.0/9*(F-32)
    print "Celsius is %.1f degree." %(C)
except IndexError:
    print "Enter a value for F."


