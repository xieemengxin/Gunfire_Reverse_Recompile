# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/operation.pyc
# RelativePath: clientlogic/cl_behavior/operation.pyc
# Source Generated with Decompyle++
# File: operation.pyc (Python 3.6)

from __future__ import absolute_import
from . import defines
OPRATION_DATA = {
    'Invalid': defines.E_INVALID,
    'Assign': defines.E_ASSIGN,
    'Add': defines.E_ADD,
    'Sub': defines.E_SUB,
    'Mul': defines.E_MUL,
    'Div': defines.E_DIV,
    'Equal': defines.E_EQUAL,
    'NotEqual': defines.E_NOTEQUAL,
    'Greater': defines.E_GREATER,
    'Less': defines.E_LESS,
    'GreaterEqual': defines.E_GREATEREQUAL,
    'LessEqual': defines.E_LESSEQUAL }

class COprationUtils(object):
    
    def ParseOperatorType(operatorType):
        return OPRATION_DATA[operatorType]

    ParseOperatorType = staticmethod(ParseOperatorType)
    
    def CompareValue(leftValue, rightValue, oprator):
        if oprator == defines.E_EQUAL:
            return leftValue == rightValue
        if oprator == defines.E_NOTEQUAL:
            return leftValue != rightValue
        if oprator == defines.E_GREATER:
            return leftValue > rightValue
        if oprator == defines.E_LESS:
            return leftValue < rightValue
        if oprator == defines.E_GREATEREQUAL:
            return leftValue >= rightValue
        if oprator == defines.E_LESSEQUAL:
            return leftValue <= rightValue

    CompareValue = staticmethod(CompareValue)

