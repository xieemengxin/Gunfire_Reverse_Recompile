# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13091.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13091.pyc
# Source Generated with Decompyle++
# File: p13091.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, INSCRIPTION_TYPE_RARE, ITEMPERFORM_ENABLE_HOLD, OBJ_ATTACK, OBJ_ENEMY

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByTargetType(oWarrior, oEventCB, 8, OBJ_ENEMY, 0)
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, min(int(cl_evact.EventGetTargetNum(oWarrior, oEventCB) * 2500), 10000), DAM_TYPE_WEAPON, '')


class CPerform(CCustomPerform):
    m_SID = 13091
    m_Name = '近战法师'
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
    m_LimitList = ((23,), (), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

