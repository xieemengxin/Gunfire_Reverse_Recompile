# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51556.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51556.pyc
# Source Generated with Decompyle++
# File: p51556.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import DAM_TYPE_WEAPON
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 2000, DAM_TYPE_WEAPON, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 5000, DAM_TYPE_WEAPON, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 8000, DAM_TYPE_WEAPON, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttSpeed', 2000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, (lambda *a: Func717(*a, **{
'sArg': 'AttSpeed' })), 0, { })


class CPerform(CCustomPerform):
    m_SID = 51556
    m_Name = '#NT#火力升级'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

