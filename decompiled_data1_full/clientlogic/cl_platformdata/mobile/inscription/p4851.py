# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4851.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4851.pyc
# Source Generated with Decompyle++
# File: p4851.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_RARE, ITEMPERFORM_ENABLE_HOLD
from cl_newformula import Func505

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        if cl_evcon.GetEventWeaponBulletCnt(oWarrior, oEventCB) > cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func505(*a) * 50 / 100 + 0)):
            cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, 4000)
            cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'Trajectory', 0, 2000)
        else:
            cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, 0)
            cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'Trajectory', 0, 0)


class CPerform(CCustomPerform):
    m_SID = 4851
    m_Name = '前倾弹夹'
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
    m_LimitList = ((), (), ())
    m_ExcludeList = ((9, 10, 12, 14, 15, 17, 18, 19, 20), (4878,), (1704,))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

