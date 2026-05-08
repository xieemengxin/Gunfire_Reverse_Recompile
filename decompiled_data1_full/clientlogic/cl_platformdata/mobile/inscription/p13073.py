# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13073.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13073.pyc
# Source Generated with Decompyle++
# File: p13073.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import EQUIP_TYPE_FUNDAMENTALWEAPON, INSCRIPTION_TYPE_GEMINI, ITEMPERFORM_ENABLE_BOTH

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetLinkAttr(oWarrior, oLifeCycle, 'MaxBullet', None)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1867, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckSwitchWeaponType(oWarrior, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_action.PassiveCloseLinkPerform(oWarrior, oEventCB.GetCBLifeCycle())


class CPerform(CCustomPerform):
    m_SID = 13073
    m_Name = '弹夹连结（独立计数）'
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
    m_LimitList = ((), (), ())
    m_ExcludeList = ((10,), (4878,), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_BOTH

