# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13010.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13010.pyc
# Source Generated with Decompyle++
# File: p13010.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_RARE, ITEMPERFORM_ENABLE_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'LuckyHit', 50, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'LuckyHit', 0, 0)


class CPerform(CCustomPerform):
    m_SID = 13010
    m_Name = '奖励幸运-近战'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_RARE
    m_ElementType = None
    m_LimitList = ((20,), (), ())
    m_ExcludeList = ((), (), (1606,))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

