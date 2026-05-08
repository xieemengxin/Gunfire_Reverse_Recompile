# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14042.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14042.pyc
# Source Generated with Decompyle++
# File: p14042.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7118: 1,
        22223: 1,
        22233: 1,
        22243: 1 }, 1, 0):
        cl_evact.EventGetTargetByNearestHero(oWarrior, oEventCB)
        cl_evact.EventCBUpdateCustomPosInfo(oWarrior, oEventCB, {
            'vStart': cl_evact.EventCBGetTargetPos(oWarrior, oEventCB),
            'vEnd': cl_evact.EventCBGetCurPos(oWarrior, oEventCB) })


class CPerform(CCustomPerform):
    m_SID = 14042
    m_Name = '轮回9-魔化硝石勇士'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

