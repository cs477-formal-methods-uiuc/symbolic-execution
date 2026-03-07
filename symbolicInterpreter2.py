from z3 import *
import copy

from expression import *
from command import *

from symbolicInterpreter import evaluateExpr

def checkSat(formula):
    s = Solver()
    s.add(formula)
    if s.check() == sat:
        return True 
    else:
        return False 

def executeCommandWithPaths(paths, command):
    """
    Paths is a list of (pathCondition, store) pairs.
    command is a Command object.
    This function should return a list of (pathCondition, store) pairs that result from executing the command on 
    each of the input paths.
    """
    raise NotImplementedError('executeCommandWithPaths is not implemented yet')