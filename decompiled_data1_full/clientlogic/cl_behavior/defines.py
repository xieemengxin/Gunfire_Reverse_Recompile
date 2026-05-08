# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/defines.pyc
# RelativePath: clientlogic/cl_behavior/defines.pyc
# Source Generated with Decompyle++
# File: defines.pyc (Python 3.6)

from __future__ import absolute_import
import sys
if sys.version_info.major == 3:
    import typing
    status = typing.TypeVar('status')
else:
    status = 'status'
BT_INVALID = 0
BT_SUCCESS = 1
BT_FAILURE = 2
BT_RUNNING = 3
TM_Transfer = 0
TM_Return = 1
E_SUCCESS = 1
E_FAILURE = 2
E_BOTH = 3
E_ENTER = 1
E_UPDATE = 2
ETP_ALWAYS = 1
ETP_SUCCESS = 2
ETP_FAILURE = 3
ETP_EXIT = 4
E_INVALID = 0
E_ASSIGN = 1
E_ADD = 2
E_SUB = 3
E_MUL = 4
E_DIV = 5
E_EQUAL = 6
E_NOTEQUAL = 7
E_GREATER = 8
E_LESS = 9
E_GREATEREQUAL = 10
E_LESSEQUAL = 11
FAIL_ON_ONE = 0
FAIL_ON_ALL = 1
SUCCEED_ON_ONE = 0
SUCCEED_ON_ALL = 1
EXIT_NONE = 0
EXIT_ABORT_RUNNINGSIBLINGS = 1
CHILDFINISH_ONCE = 0
CHILDFINISH_LOOP = 1

class EActionType:
    EAT_enter = 1
    EAT_exit = 2
    EAT_all = EAT_enter | EAT_exit


class EActionResult:
    EAR_none = 0
    EAR_success = 1
    EAR_failure = 2
    EAR_running = 3
    EAR_all = EAR_success | EAR_failure

