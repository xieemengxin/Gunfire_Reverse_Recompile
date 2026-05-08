# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/monsteraf/__init__.pyc
# RelativePath: clientlogic/cl_perform/monsteraf/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import PF_TYPE_MONSTERAF
from cl_only import DeepCopy
import cllib.lib_flag
g_MonsterAfAdjust = { }
g_MobileMonsterAfAdjust = { }
from cl_commondefines import WARRIOR_ELIHEVFAR, WARRIOR_NORBADGER, WARRIOR_NORFLY, WARRIOR_NORHEVNEAR, WARRIOR_NORMAGIC, WARRIOR_NORMEDFAR, WARRIOR_NORSMAFAR, WARRIOR_NORSMANEAR, WARRIOR_NORSNIPE, WARRIOR_NORTHROW
g_MonsterAfAdjust = {
    (3, 10, 5): {
        WARRIOR_NORMAGIC: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORTHROW: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORMEDFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMAFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_ELIHEVFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORHEVNEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMANEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSNIPE: {
            6102: -10,
            6103: -10,
            6105: -3,
            6111: -5 },
        WARRIOR_NORFLY: {
            6101: -10,
            6102: -15,
            6103: -15,
            6105: -3,
            6111: -5 },
        WARRIOR_NORBADGER: {
            6101: -5,
            6102: -15,
            6103: -15 } },
    (3, 9, 5): {
        WARRIOR_NORMAGIC: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORTHROW: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORMEDFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMAFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_ELIHEVFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORHEVNEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMANEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSNIPE: {
            6102: -10,
            6103: -10,
            6105: -3,
            6111: -5 },
        WARRIOR_NORFLY: {
            6101: -10,
            6102: -15,
            6103: -15,
            6105: -3,
            6111: -5 },
        WARRIOR_NORBADGER: {
            6101: -5,
            6102: -15,
            6103: -15 } },
    (3, 8, 5): {
        WARRIOR_NORMAGIC: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORTHROW: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORMEDFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMAFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_ELIHEVFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORHEVNEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMANEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSNIPE: {
            6102: -10,
            6103: -10,
            6105: -3,
            6111: -3 },
        WARRIOR_NORFLY: {
            6101: -10,
            6102: -15,
            6103: -15,
            6105: -3,
            6111: -3 },
        WARRIOR_NORBADGER: {
            6101: -5,
            6102: -15,
            6103: -15 } },
    (3, 7, 5): {
        WARRIOR_NORMAGIC: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORTHROW: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORMEDFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMAFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_ELIHEVFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORHEVNEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMANEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSNIPE: {
            6102: -10,
            6103: -10,
            6105: -3,
            6111: -3 },
        WARRIOR_NORFLY: {
            6101: -10,
            6102: -15,
            6103: -15,
            6105: -3,
            6111: -3 },
        WARRIOR_NORBADGER: {
            6101: -5,
            6102: -15,
            6103: -15 } },
    (3, 6, 5): {
        WARRIOR_NORMAGIC: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORTHROW: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORMEDFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMAFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_ELIHEVFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORHEVNEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMANEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSNIPE: {
            6102: -10,
            6103: -10,
            6105: -3,
            6111: -3 },
        WARRIOR_NORFLY: {
            6101: -10,
            6102: -15,
            6103: -15,
            6105: -3,
            6111: -3 },
        WARRIOR_NORBADGER: {
            6101: -5,
            6102: -15,
            6103: -15 } },
    (3, 5, 5): {
        WARRIOR_NORMAGIC: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORTHROW: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORMEDFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMAFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_ELIHEVFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORHEVNEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMANEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSNIPE: {
            6102: -10,
            6103: -10,
            6105: -3,
            6111: -3 },
        WARRIOR_NORFLY: {
            6101: -10,
            6102: -15,
            6103: -15,
            6105: -3,
            6111: -3 },
        WARRIOR_NORBADGER: {
            6101: -5,
            6102: -15,
            6103: -15 } },
    (3, 4, 5): {
        WARRIOR_NORMAGIC: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORTHROW: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORMEDFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMAFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_ELIHEVFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORHEVNEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMANEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSNIPE: {
            6102: -10,
            6103: -10,
            6105: -3,
            6111: -3 },
        WARRIOR_NORFLY: {
            6101: -10,
            6102: -15,
            6103: -15,
            6105: -3,
            6111: -3 },
        WARRIOR_NORBADGER: {
            6101: -5,
            6102: -15,
            6103: -15 } },
    (3, 3, 5): {
        WARRIOR_NORMAGIC: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORTHROW: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORMEDFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMAFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_ELIHEVFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORHEVNEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMANEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSNIPE: {
            6102: -10,
            6103: -10,
            6105: -3,
            6111: -3 },
        WARRIOR_NORFLY: {
            6101: -10,
            6102: -15,
            6103: -15,
            6105: -3,
            6111: -3 },
        WARRIOR_NORBADGER: {
            6101: -5,
            6102: -15,
            6103: -15 } },
    (3, 2, 5): {
        WARRIOR_NORMAGIC: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORTHROW: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORMEDFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMAFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_ELIHEVFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORHEVNEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMANEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSNIPE: {
            6102: -10,
            6103: -10,
            6105: -3,
            6111: -3 },
        WARRIOR_NORFLY: {
            6101: -10,
            6102: -15,
            6103: -15,
            6105: -3,
            6111: -3 },
        WARRIOR_NORBADGER: {
            6101: -5,
            6102: -15,
            6103: -15 } },
    (3, 1, 5): {
        WARRIOR_NORMAGIC: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORTHROW: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORMEDFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMAFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_ELIHEVFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORHEVNEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMANEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSNIPE: {
            6102: -10,
            6103: -10,
            6105: -3,
            6111: -3 },
        WARRIOR_NORFLY: {
            6101: -10,
            6102: -15,
            6103: -15,
            6105: -3,
            6111: -3 },
        WARRIOR_NORBADGER: {
            6101: -5,
            6102: -15,
            6103: -15 } },
    (3, 0, 5): {
        WARRIOR_NORMAGIC: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORTHROW: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORMEDFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMAFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_ELIHEVFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORHEVNEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMANEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSNIPE: {
            6102: -10,
            6103: -10,
            6105: -15,
            6111: -5 },
        WARRIOR_NORFLY: {
            6101: -10,
            6102: -15,
            6103: -15,
            6105: -15,
            6111: -5 },
        WARRIOR_NORBADGER: {
            6101: -5,
            6102: -15,
            6103: -15 } },
    (2, 0, 5): {
        WARRIOR_NORMAGIC: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORTHROW: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORMEDFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMAFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_ELIHEVFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORHEVNEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMANEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSNIPE: {
            6102: -10,
            6103: -10,
            6105: -15,
            6111: -5 },
        WARRIOR_NORFLY: {
            6101: -10,
            6102: -15,
            6103: -15,
            6105: -15,
            6111: -5 },
        WARRIOR_NORBADGER: {
            6101: -5,
            6102: -15,
            6103: -15 } },
    (1, 0, 5): {
        WARRIOR_NORMAGIC: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORTHROW: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORMEDFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMAFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_ELIHEVFAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORHEVNEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSMANEAR: {
            6105: 5,
            6111: 5 },
        WARRIOR_NORSNIPE: {
            6102: -10,
            6103: -10,
            6105: -15,
            6111: -5 },
        WARRIOR_NORFLY: {
            6101: -10,
            6102: -15,
            6103: -15,
            6105: -15,
            6111: -5 },
        WARRIOR_NORBADGER: {
            6101: -5,
            6102: -15,
            6103: -15 } } }
g_MobileMonsterAfAdjust = { }
if cllib.lib_flag.g_IsMobileRun:
    
    def GetMonsterAfAdjust(iRound, iCycle, iSeason):
        tKey = (iRound, iCycle, iSeason)
        if tKey not in g_MobileMonsterAfAdjust:
            return { }
        return DeepCopy(g_MobileMonsterAfAdjust[tKey])

else:
    
    def GetMonsterAfAdjust(iRound, iCycle, iSeason):
        tKey = (iRound, iCycle, iSeason)
        if tKey not in g_MonsterAfAdjust:
            return { }
        return DeepCopy(g_MonsterAfAdjust[tKey])


class CPerform(CCustomPerform):
    m_PFType = PF_TYPE_MONSTERAF

