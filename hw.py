__author__ = 'Alexey'
# -*- coding: utf-8 -*-

def sum(n1, n2):
    return n1 + n2

print sum(2, 3)
print (lambda x, y: x * y )(3, 4)

class Fruit:
    'Fruit class'
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name


fruits = [Fruit("Apple"), Fruit("Orange")]
for fruit in fruits:
    print fruit,
try:
    print "Try block"
    raise Exception("123")
except Exception, (e):
    print "Catch exception " + e.message
else:
    print "Else block"
print "Outside"
