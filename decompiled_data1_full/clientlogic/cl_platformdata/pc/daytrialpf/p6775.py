# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p6775.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p6775.pyc
# Source Generated with Decompyle++
# File: p6775.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, HP_TYPE_ARMOR, HP_TYPE_NORMAL, HP_TYPE_SHIELD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeElementDam(oWarrior, oLifeCycle, DAM_TYPE_FIRE, {
        HP_TYPE_SHIELD: -3333,
        HP_TYPE_ARMOR: -3333 })
    cl_action.CommonChangeElementDam(oWarrior, oLifeCycle, DAM_TYPE_CORRISION, {
        HP_TYPE_NORMAL: -3333,
        HP_TYPE_SHIELD: -3333 })
    cl_action.CommonChangeElementDam(oWarrior, oLifeCycle, DAM_TYPE_THUNDER, {
        HP_TYPE_NORMAL: -3333,
        HP_TYPE_ARMOR: -3333 })


class CPerform(CCustomPerform):
    m_SID = 6775
    m_Name = '增加被元素克制减伤'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

