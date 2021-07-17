#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:35:13 2019

@author: xudansha
"""

import sys, calendar
year = eval(sys.argv[1])
month = eval(sys.argv[2])
day = eval(sys.argv[3])

print "The date %d %d %d is a %s." % (year, month, day, calendar.day_name[calendar.weekday(year, month, day)])