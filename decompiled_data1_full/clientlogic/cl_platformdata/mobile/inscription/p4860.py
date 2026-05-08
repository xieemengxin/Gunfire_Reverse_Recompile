# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4860.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4860.pyc
# Source Generated with Decompyle++
# File: p4860.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_NORMAL, ITEMPERFORM_ENABLE_HOLD, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        if cl_evcon.CheckShootStatus(oWarrior, oEventCB):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1155, 0, { }, 1, None, None)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1155, None, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1155, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4860
    m_Name = '开镜瞄准'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_NORMAL
    m_ElementType = None
    m_LimitList = ((11,), (), ())
    m_ExcludeList = ((17, 1), (4869,), (1016,))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

