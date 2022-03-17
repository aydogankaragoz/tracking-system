#!/usr/bin/python
# -*- coding: utf-8 -*-

from TrackingSystem import TrackingSystem

ts = TrackingSystem()

ts.consumeCSV('entries.csv')

ts.printBlogs()
