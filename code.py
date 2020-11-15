import sys
from subdir import newcode

def handler(context, event):
    val = newcode.newfunc()
    return "Hi from Edmond " + str(val)

