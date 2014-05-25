# Any Python source file can be used as a Module
# spam.py example
# load this code as a module by using IMPORT
a = 37
def foo():
    print("I'm foo and a is %s" % a)
def bar():
    print("I'm bar and I'm calling foo")
    foo()
class Spam(object):
    def grok(self):
        print("I'm Spam.grok")