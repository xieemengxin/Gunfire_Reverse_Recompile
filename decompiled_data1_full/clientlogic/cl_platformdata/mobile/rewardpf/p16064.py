# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16064.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16064.pyc
# Source Generated with Decompyle++
# File: p16064.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_ATTACK, PF_SUBMSG_THROW
from cl_newformula import Func305

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1419, -1, -1):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.EventChangeShield(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'ShieldMax' }) * 15 / 100 + 0))
        cl_evact.EventChangeArmor(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'ArmorMax' }) * 15 / 100 + 0))


class CPerform(CCustomPerform):
    m_SID = 16064
    m_Name = '花开花谢'
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

