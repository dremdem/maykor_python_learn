#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Bad(Exception):
    pass

a = '12345'

try:
    a = int(a) + 5
    print(a)
    raise Bad
except Bad:
    # print(u'Данное значение: (%s) не является числом.' % a)
    print(u'Очень плохое исключение Ж(')
finally:
    print(111)    

# a = int(a) + 5

try:
    assert 'money' == '1000000'
except AssertionError:
    print('Надо больше работать!')


print('Конец!')



