# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13068.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13068.pyc
# Source Generated with Decompyle++
# File: p13068.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1841, 500, { }, 0)


class CPerform(CCustomPerform):
    m_SID = 13068
    m_Name = '瞳（测试2）'
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
    m_LimitList = ((), (1804,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

