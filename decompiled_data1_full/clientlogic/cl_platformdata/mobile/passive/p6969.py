# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p6969.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p6969.pyc
# Source Generated with Decompyle++
# File: p6969.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'HPMax', 5500)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldMax', 4500)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'RShield', 15)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldRecoverTime', 300)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1436, 'ColdTime', 1000)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1436, 'Radius', 4)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_LAYERSTART, -1, 0)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1333, 'AddStateTime', 3)
    CustomAction(oWarrior, oLifeCycle, { })


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBChangeTargetPerformAttr(oWarrior, oEventCB, 1333, 'ColdTime', 0, (lambda *a: 1000 - min(4, Func651(*a, **{
'sKey': 'Layer' })) * 100), 0)


class CPerform(CCustomPerform):
    m_SID = 6969
    m_Name = '呦呦队友AI被动'
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

