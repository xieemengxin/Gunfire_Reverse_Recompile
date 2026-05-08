# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4925.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4925.pyc
# Source Generated with Decompyle++
# File: p4925.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveSetPosToCartoon(oWarrior, oEventCB)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9407, 1, 0) and cl_evcon.CheckVictimEPFPosDist(oWarrior, oEventCB, 1):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_WEAPON, '')


class CPerform(CCustomPerform):
    m_SID = 4925
    m_Name = '狱裂骨龙'
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
    m_LimitList = ((), (1407,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

