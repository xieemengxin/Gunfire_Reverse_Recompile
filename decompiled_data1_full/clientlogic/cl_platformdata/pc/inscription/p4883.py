# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4883.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4883.pyc
# Source Generated with Decompyle++
# File: p4883.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) and cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 80):
        cl_evact.PassiveCBHitWeaknessUsePerform(oWarrior, oEventCB, 1640, 1000)
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 40)


class CPerform(CCustomPerform):
    m_SID = 4883
    m_Name = '额外奖励-火球'
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
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (), (16, 17))
    m_ExcludeList = ((23,), (), (1303,))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

