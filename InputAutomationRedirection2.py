import sys
from io import StringIO


##sys.stdin
##sys.stdin.__class__.__base__
##StringIO.__base__


###Hardcoded
##with StringIO('asdf') as f:
##    stdin = sys.stdin
##    sys.stdin = f
##    print("'" + input() + "' wasn't actually typed at the command line")
##    sys.stdin = stdin



def dummy_fn():
    name = input()
    return('Hello, '+name)

with StringIO('Mati') as f:
    stdin = sys.stdin
    sys.stdin = f
    print(dummy_fn())
    sys.stdin = stdin

