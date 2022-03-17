#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from Blog import Blog
from Comment import Comment


class TestStringMethods(unittest.TestCase):

    def test_blog(self):
        row = ['BLOG', '1', '', 'My first blog!']
        blog = Blog(row)
        self.assertEqual(blog.id, 1)
        self.assertEqual(blog.content, 'My first blog!')

    def test_blog_with_association(self):
        row = ['BLOG', '6', '5', 'How does this thing work?']
        with self.assertRaises(TypeError):
            Blog(row)

    def test_comment(self):
        row = ['COMMENT', '2', '1', 'Nice work']
        comment = Comment(row)
        self.assertEqual(comment.id, 2)
        self.assertEqual(comment.parent_id, 1)
        self.assertEqual(comment.content, 'Nice work')

    def test_comment_without_association(self):
        row = ['COMMENT', '6', '', 'Wow, look at that']
        with self.assertRaises(TypeError):
            Comment(row)


if __name__ == '__main__':
    unittest.main()
