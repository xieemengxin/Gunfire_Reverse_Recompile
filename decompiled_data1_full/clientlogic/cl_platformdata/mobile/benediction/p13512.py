# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13512.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13512.pyc
# Source Generated with Decompyle++
# File: p13512.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 0, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1412, 'DamInterval', 0, 3)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1413, 'DamInterval', 0, 3)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1412, 'Radius', 10000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1413, 'Radius', 10000, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1412, 'Att', (cl_action.CommonGetPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1412, 'DamInterval') - 1) * 15000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1413, 'Att', (cl_action.CommonGetPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1413, 'DamInterval') - 1) * 15000, 0)


class CPerform(CCustomPerform):
    m_SID = 13512
    m_Name = '高能电弧'
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
    m_Career = 104

