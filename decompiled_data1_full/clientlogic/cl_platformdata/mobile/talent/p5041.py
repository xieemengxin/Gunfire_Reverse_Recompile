# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5041.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5041.pyc
# Source Generated with Decompyle++
# File: p5041.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK
from cl_newformula import Func824

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformForceAttr(oWarrior, oLifeCycle, 1434, 'AddStateTime', 200)
    cl_action.CommonSetPerformForceAttr(oWarrior, oLifeCycle, 1439, 'AddStateTime', 200)
    cl_action.CommonSetPerformForceAttr(oWarrior, oLifeCycle, 1439, 'KeepTime', 200)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1434: 1,
        1439: 1,
        1979: 1 }, 0, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: max(0, int((Func824(*a, **{
'sAttr': 'AddStateTime' }) - 200) * 50))), 0, '')


class CPerform(CCustomPerform):
    m_SID = 5041
    m_Name = '昙华天诀'
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
    m_MaxUpgradeTimes = 0
    m_TalentType = 1
    m_IsRareTalent = 1
    m_Career = 118

