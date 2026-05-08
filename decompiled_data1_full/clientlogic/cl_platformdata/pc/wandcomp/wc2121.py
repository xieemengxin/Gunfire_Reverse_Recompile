# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2121.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2121.pyc
# Source Generated with Decompyle++
# File: wc2121.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION, WAND_SUBMSG_EXTACTIONSLOT
from cl_newformula import Func651, Func772, Func776

def Action2(oWarrior, oLifeCycle):
    cl_action.WandActCompSetWandCustomLimit(oWarrior, oLifeCycle, 'ColdTime', 10, 10000000)
    cl_action.WandActCompSealRightSide(oWarrior, oLifeCycle)
    cl_action.WandActCompChangeWandAttr(oWarrior, oLifeCycle, 'ColdTime', (lambda *a: -Func772(*a) * 40), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_EXTACTIONSLOT, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func776(*a))) == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Wand' }))):
        cl_action.WandActCompSealRightSide(oWarrior, oEventCB.GetCBLifeCycle())
        cl_action.WandActCompChangeWandAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ColdTime', (lambda *a: -Func772(*a) * 40), 0)


def PresetAction(iPos, dComp, iMaxNum, lstNewComp):
    cl_action.SealRightSide(iPos, dComp, iMaxNum, lstNewComp)


class CWandComp(CBaseComp):
    m_SID = 2121
    m_Name = '封锁秘法'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        2: (Action2, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_PresetAction = PresetAction
    m_TriggerType = WAND_ACTCOMP_INSTANT

