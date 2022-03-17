#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
from Blog import Blog
from Comment import Comment
from statics import BLOG, COMMENT


class TrackingSystem:

    def __init__(self):
        self.blog_set = set()
        self.comment_set = set()
        self.parents = {}

    def consumeCSV(self, file_name):
        file = open(file_name)
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            if row[0] == BLOG:
                try:
                    blog = Blog(row)
                    self.blog_set.add(blog)
                except TypeError as e:
                    print('TypeError: ' + str(row) + '\n\t' + str(e) + '\n')
            elif row[0] == COMMENT:
                try:
                    comment = Comment(row)
                    self.comment_set.add(comment)
                    if comment.parent_id not in self.parents:
                        self.parents[comment.parent_id] = []
                    self.parents[comment.parent_id].append(comment)
                except TypeError as e:
                    print('TypeError: ' + str(row) + '\n\t' + str(e) + '\n')
        file.close()

    def printChildren(self, parent_id, prefix):
        if parent_id in self.parents:
            for child in self.parents[parent_id]:
                print(prefix + ' ' + child.content)
                self.printChildren(child.id, prefix + '\t')

    def printBlogs(self):
        for blog in self.blog_set:
            blog.printContent()
            self.printChildren(blog.id, '\t')
