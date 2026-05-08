# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4963.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4963.pyc
# Source Generated with Decompyle++
# File: p4963.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_GEMINI, ITEMPERFORM_ENABLE_HOLD, OBJ_ATTACK, WEAPON_MAIN_PERFORM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonTriggerWeaponPerformBehavior(oWarrior, oLifeCycle, WEAPON_MAIN_PERFORM, 2016, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 10000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 4963
    m_Name = '自动追踪'
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
    m_InscriptionType = INSCRIPTION_TYPE_GEMINI
    m_ElementType = None
    m_LimitList = ((), (1002, 1003, 1004, 1008, 1010, 1101, 1102, 1104, 1105, 1107, 1007, 1103, 1006), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

