# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4369.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4369.pyc
# Source Generated with Decompyle++
# File: p4369.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, HP_TYPE_ARMOR, HP_TYPE_NORMAL, HP_TYPE_SHIELD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeElementDam(oWarrior, oLifeCycle, DAM_TYPE_FIRE, {
        HP_TYPE_SHIELD: -2500,
        HP_TYPE_ARMOR: -2500 })
    cl_action.CommonChangeElementDam(oWarrior, oLifeCycle, DAM_TYPE_CORRISION, {
        HP_TYPE_SHIELD: -2500,
        HP_TYPE_NORMAL: -2500 })
    cl_action.CommonChangeElementDam(oWarrior, oLifeCycle, DAM_TYPE_THUNDER, {
        HP_TYPE_NORMAL: -2500,
        HP_TYPE_ARMOR: -2500 })


class CPerform(CCustomPerform):
    m_SID = 4369
    m_Name = '元素湍流'
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

