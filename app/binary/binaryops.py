from enum import Enum


class Operation(Enum):
    ADD = 'Add'
    SUBTRACT = 'Sub'
    MULTIPLY = 'Multiply'
    DIVIDE = 'Divide'
    GREATER = 'Gt'
    EQUAL = 'Eq'
    LESSER = 'Lt'
    OR = 'Or'


def add(lhs, rhs):
    if type(lhs).__name__ == type(rhs).__name__:
        return lhs + rhs
    return str(lhs) + str(rhs)


def sub(lhs, rhs):
    if type(lhs).__name__ == type(rhs).__name__:
        return lhs - rhs


def eq(lhs, rhs):
    return lhs == rhs


def gt(lhs, rhs):
    return lhs > rhs


def lt(lhs, rhs):
    return lhs < rhs


def bin_or(lhs, rhs):
    return lhs or rhs


def proc_binary(op, lhs, rhs):
    if op == Operation.ADD.value:
        return add(lhs, rhs)
    if op == Operation.EQUAL.value:
        return eq(lhs, rhs)
    if op == Operation.GREATER.value:
        return gt(lhs, rhs)
    if op == Operation.LESSER.value:
        return lt(lhs, rhs)
    if op == Operation.SUBTRACT.value:
        return sub(lhs, rhs)
    if op == Operation.OR.value:
        return bin_or(lhs, rhs)
    else:
        raise ValueError("Unsupported operation: {}".format(op))
