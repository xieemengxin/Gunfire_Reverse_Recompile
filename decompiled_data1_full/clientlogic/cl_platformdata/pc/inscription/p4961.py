# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4961.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4961.pyc
# Source Generated with Decompyle++
# File: p4961.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import FIGHT_KEY_IGNOREDAMAGE, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, NWARRIOR_DROP_AXE, OBJ_VICTIM, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2002)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, -1, 0, 0, 0)
    cl_action.CommonChangeWeaponPerformArgs(oWarrior, oLifeCycle, 4330, 'ExtraDrop', 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 2002)
    cl_action.CommonChangeWeaponPerformArgs(oWarrior, oLifeCycle, 4330, 'ExtraDrop', -1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPickType(oWarrior, oEventCB, NWARRIOR_DROP_AXE):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) and cl_evcon.EventCBCheckTargetIsLive(oWarrior, oEventCB):
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 2002, 0, { }, 0)
        else:
            cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 30, WARRIOR_MONSTER, 1, 0, 1, 0, 0, { }, 0, FIGHT_KEY_IGNOREDAMAGE, 0, 1, None)
            if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
                cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 2002, 0, { }, 0)


class CPerform(CCustomPerform):
    m_SID = 4961
    m_Name = '飞斧'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1215,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

