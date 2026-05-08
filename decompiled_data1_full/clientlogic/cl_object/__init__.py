# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_object/__init__.pyc
# RelativePath: clientlogic/cl_object/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import Time2Frame, PerSecond2PerFrame
from . import logging
g_AttrConversionFunc = {
    'RHP': PerSecond2PerFrame,
    'TurnSpeed': PerSecond2PerFrame,
    'StruckIgnoreFrame': Time2Frame,
    'ThumpFrame': Time2Frame,
    'KnockBackFrame': Time2Frame }

def AttrUnitConversion(sAttr, iValue):
    if sAttr not in g_AttrConversionFunc:
        return iValue
    return g_AttrConversionFunc[sAttr](iValue)


def NewDay():
    logging.ClearTimeoutAlertRecord()

