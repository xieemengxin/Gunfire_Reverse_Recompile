# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p13124.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p13124.pyc
# Source Generated with Decompyle++
# File: p13124.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD
from math import ceil
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'hit', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'hit') >= 2:
        cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'Trajectory', 0, 0)
        cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'Trajectory', (lambda *a: ceil(min(8, Func717(*a, **{
'sArg': 'hit' }) / 2)) * 100), 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'hit', 0)
    else:
        cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'Trajectory', 0, 0)


class CPerform(CCustomPerform):
    m_SID = 13124
    m_Name = '#NT#迭代狂猎专属2'
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
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1315, 1306), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

