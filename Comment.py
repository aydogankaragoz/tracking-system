#!/usr/bin/python
# -*- coding: utf-8 -*-
from Blog import Blog


class Comment(Blog):

    def __init__(self, row):
        if row[2] == '':
            raise TypeError('All comments must be associated with another object.')
        super().__init__(row)
        self.parent_id = int(row[2])
