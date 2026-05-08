# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rareitem/i7009.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rareitem/i7009.pyc
# Source Generated with Decompyle++
# File: i7009.pyc (Python 3.6)

import cl_msgcenter
import cl_evact
import cl_evcon
import cl_action
import cl_condition
from . import rareitemdata

def UseAction(oOwner, oLifeCycle):
    cl_action.ItemAddState(oOwner, oLifeCycle, 1644, 2000, { }, 0)


class CItem(rareitemdata.CRareItemData):
    m_SID = 7009
    m_Shape = 5543
    m_Name = '子弹倾泻'
    m_MaxGroup = 0
    m_UseNotify = 9377
    m_UseAction = UseAction

