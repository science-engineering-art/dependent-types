from .matrix import Matrix
from dependent_types import Attr, _

N = Attr()
M = Attr()

def test_1():
    try:
        Matrix[N, 4| (M > 9)]
    except:
        return True
    # raise Exception() 
    