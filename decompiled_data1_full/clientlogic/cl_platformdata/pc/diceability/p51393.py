# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51393.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51393.pyc
# Source Generated with Decompyle++
# File: p51393.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_SEASONOUTPUT, DICE_PUTOUT_POLL_THREE, PF_SUBMSG_CAREERPF
from cl_newformula import Func223, Func308, Func805

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONPEOFROM_START, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONPEOFROM_START, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONPEOFROM_START, -1, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONPEOFROM_START, -1, 1, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONPEOFROM_START, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB):
        cl_action.CommonCreateHeroSidePet(oWarrior, oEventCB.GetCBLifeCycle(), 2423, 0, {
            'DiceID': (lambda *a: Func805(*a)),
            'DiceLevel': (lambda *a: Func308(*a)),
            'HPMax': (lambda *a: 100000 + Func223(*a) * 10000) }, 1, 2, {
            33933: 1 })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB):
        cl_action.CommonCreateHeroSidePet(oWarrior, oEventCB.GetCBLifeCycle(), 2423, 0, {
            'DiceID': (lambda *a: Func805(*a)),
            'DiceLevel': (lambda *a: Func308(*a)),
            'HPMax': (lambda *a: 100000 + Func223(*a) * 10000) }, 1, 2, {
            33933: 1 })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB):
        cl_action.CommonCreateHeroSidePet(oWarrior, oEventCB.GetCBLifeCycle(), 2423, 0, {
            'DiceID': (lambda *a: Func805(*a)),
            'DiceLevel': (lambda *a: Func308(*a)),
            'HPMax': (lambda *a: 100000 + Func223(*a) * 10000) }, 2, 3, {
            33933: 1 })


class CPerform(CCustomPerform):
    m_SID = 51393
    m_Name = '硝石勇士'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_SEASONOUTPUT,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_THREE

