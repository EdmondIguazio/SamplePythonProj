import sys
sys.path.append("/opt/nuclio/subdir/")
import newcode

def handler(context, event):
    val = newcode.newfunc()
    return "Hi from Edmond " + str(val)
