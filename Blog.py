#!/usr/bin/python
# -*- coding: utf-8 -*-
from statics import BLOG


class Blog:

    def __init__(self, row):
        if row[0] == BLOG and row[2] != '':
            raise TypeError('Blog entries can not be associated with other blog entries.')
        self.id = int(row[1])
        self.content = row[3]

    def printContent(self):
        print(self.content)
