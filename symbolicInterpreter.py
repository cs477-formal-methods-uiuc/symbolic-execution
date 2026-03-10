from z3 import *
import copy

from expression import *
from command import *

"""PLEASE ONLY MODIFY THE TODO SECTIONS"""

def evaluateConst(pathCondition, store, c):
    return c.const

def evaluateVar(pathCondition, store, var):
    return store[var.name]

def evaluateUnaryOp(pathCondition, store, lhs, op):
    # TODO
    raise NotImplementedError('evaluateUnaryOp is not implemented yet')
    
def evaluateBinaryArithOp(pathCondition, store, lhs, rhs, op):
    # TODO
    raise NotImplementedError('evaluateBinaryArithOp is not implemented yet')

def evaluateBinaryComparisonOp(pathCondition, store, lhs, rhs, op):
    # TODO
    raise NotImplementedError('evaluateBinaryComparisonOp is not implemented yet')

def evaluateBinaryLogicalOp(pathCondition, store, lhs, rhs, op):
    # TODO
    raise NotImplementedError('evaluateBinaryLogicalOp is not implemented yet')


def evaluateExpr(pathCondition, store, expr):

    if isinstance(expr, Const):
        return evaluateConst(pathCondition, store, expr)
    
    elif isinstance(expr, Var):
        return evaluateVar(pathCondition, store, expr)
    
    elif isinstance(expr, BinaryArithOp):
        return evaluateBinaryArithOp(pathCondition, store, expr.lhs, expr.rhs, expr.op)
    
    elif isinstance(expr, BinaryComparisonOp):
        return evaluateBinaryComparisonOp(pathCondition, store, expr.lhs, expr.rhs, expr.op)
    
    elif isinstance(expr, BinaryLogicalOp):
        return evaluateBinaryLogicalOp(pathCondition, store, expr.lhs, expr.rhs, expr.op)
    
    elif isinstance(expr, UnaryOp):
        return evaluateUnaryOp(pathCondition, store, expr.lhs, expr.op)
    else:
        print('ERROR')
        return None



def executeSkip(pathCondition, store, command):
    return pathCondition, store


def executeAssignment(pathCondition, store, command):
    # TODO
    raise NotImplementedError("executeAssignment is not implemented yet")

def executeSequence(pathCondition, store, command):
    # TODO
    raise NotImplementedError("executeSequence is not implemented yet")

def executeAssert(pathCondition, store, command):
    e = evaluateExpr(pathCondition, store, command.expr)
    s = Solver()
    s.add(Not(Implies(pathCondition, e)))
    c = s.check()
    if c == unsat:
        print('ASSERT PASSED')
    else:
        print('ASSERT FAILED')
    return pathCondition, store 


def executeCommand(pathCondition, store, command):
    if isinstance(command, Skip):
        return executeSkip(pathCondition, store, command)
    elif isinstance(command, Assignment):
        return executeAssignment(pathCondition, store, command)
    elif isinstance(command, Sequence):
        return executeSequence(pathCondition, store, command)
    elif isinstance(command, Assert):
        return executeAssert(pathCondition, store, command)
    elif isinstance(command, Ite):
        print('NOT IMPLEMENTED')
        return None
    else:
        print('ERROR')
        return None