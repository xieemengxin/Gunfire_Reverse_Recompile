# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rareitem/i7007.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rareitem/i7007.pyc
# Source Generated with Decompyle++
# File: i7007.pyc (Python 3.6)

import cl_msgcenter
import cl_evact
import cl_evcon
import cl_action
import cl_condition
from . import rareitemdata

def UseAction(oOwner, oLifeCycle):
    cl_action.ItemAddState(oOwner, oLifeCycle, 1626, 2000, { }, 0)


class CItem(rareitemdata.CRareItemData):
    m_SID = 7007
    m_Shape = 5543
    m_Name = '水幕护盾'
    m_MaxGroup = 0
    m_UseNotify = 9366
    m_UseAction = UseAction

