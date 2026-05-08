# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4859.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4859.pyc
# Source Generated with Decompyle++
# File: p4859.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_NORMAL, ITEMPERFORM_ENABLE_HOLD, OBJ_SELF, PF_SUBMSG_FILLBULLET

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1148, 300, { }, 1, 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 1, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1148, 1, 0, 0):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, '4859FillBullet', 1, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 3, 1, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_FILLBULLET, 3, 1, 0)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1149, 1, 0, 0) == 0:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1149, 0, { }, 1, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1148, 1, 0, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, '4859FillBullet', 0):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1148, 1)


class CPerform(CCustomPerform):
    m_SID = 4859
    m_Name = '战斗弹夹'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_NORMAL
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((6, 10, 20), (4857, 4852, 4806, 4878), (1416,))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

