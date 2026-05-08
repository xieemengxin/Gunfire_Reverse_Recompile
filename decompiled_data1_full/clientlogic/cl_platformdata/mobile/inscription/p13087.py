# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13087.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13087.pyc
# Source Generated with Decompyle++
# File: p13087.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_RARE, ITEMPERFORM_ENABLE_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33281, 0, { }, 1, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 13087
    m_Name = '能量基伤'
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
    m_InscriptionType = INSCRIPTION_TYPE_RARE
    m_ElementType = None
    m_LimitList = ((23, 24), (), ())
    m_ExcludeList = ((), (), (1704, 1709))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

