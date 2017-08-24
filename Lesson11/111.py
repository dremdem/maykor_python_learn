#!/usr/bin/env python
# -*- coding: utf-8 -*-


class A:

    def __init__(self):
        self.b = None
        self.c = None

    def __repr__(self):
        return "Here is 'Peace of cake'"

    def __add__(self, other):
        return self.b + other.b



a1 = A()
a1.b = 10

a2 = A()
a2.b = 4

print(a1+a2)