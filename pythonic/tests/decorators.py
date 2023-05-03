#!/usr/bin/python

""" Using decorators """

class my_decorator(object):

    def __init__(self, fun):
        print("my_decorator.__init__()")
        fun()

    def __call__(self):
        print("my_decorator.__call__()")

@my_decorator
def testFunction():
    print("inside testFunction()")

print("Finished decorating aFunction()")

testFunction()
