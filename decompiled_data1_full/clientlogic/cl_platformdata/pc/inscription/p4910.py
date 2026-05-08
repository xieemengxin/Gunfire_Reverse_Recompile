# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4910.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4910.pyc
# Source Generated with Decompyle++
# File: p4910.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DPSUBMSG_DEFAULT, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_ATTACK
from cl_newformula import Func303, Func309, Func620

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, DPSUBMSG_DEFAULT, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9198, 1, 1) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func309(*a))) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func620(*a))) and cl_evcon.PassiveCBGetTarKeyInPFArgsDict(oWarrior, oEventCB, (lambda *a: Func620(*a)), 'PF4910VID') == 0:
        cl_evact.PassiveCBUpdatePFArgsDict(oWarrior, oEventCB, 'PF4910VID', (lambda *a: Func620(*a)), 1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveCBAddSourceWeaponBagBullet(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'CurBullet' }) * 50 / 100 + 0))
        if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1756, 0, 0, 0, 0):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1756, 0, { }, 1, 1, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9198, 1, 1):
        cl_evact.PassiveCBSetPFArgsDict(oWarrior, oEventCB, 'PF4910VID', { })


class CPerform(CCustomPerform):
    m_SID = 4910
    m_Name = '隐弹魔王'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1107,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

