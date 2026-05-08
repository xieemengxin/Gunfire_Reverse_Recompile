# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rareitem/i7005.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rareitem/i7005.pyc
# Source Generated with Decompyle++
# File: i7005.pyc (Python 3.6)

import cl_msgcenter
import cl_evact
import cl_evcon
import cl_action
import cl_condition
from cl_platformdata.custom.rareitem.customaction import CustomAction7005 as CustomAction
from . import rareitemdata

def UseAction(oOwner, oLifeCycle):
    CustomAction(oOwner, oLifeCycle, { })
    cl_action.CommonTriggerClientBehavior(oOwner, oLifeCycle, 113, 0, None, None)
    cl_action.CommonTriggerClientBehavior(oOwner, oLifeCycle, 1641, 0, None, None)


class CItem(rareitemdata.CRareItemData):
    m_SID = 7005
    m_Shape = 5543
    m_Name = '湮灭响指'
    m_MaxGroup = 0
    m_UseNotify = 9374
    m_UseAction = UseAction

