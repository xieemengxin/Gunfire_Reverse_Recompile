# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13722.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13722.pyc
# Source Generated with Decompyle++
# File: p13722.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK
from cl_newformula import Func555

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1668, 0, { }, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func555(*a, **{
'sAttr': 'CrazyEff' }) * 0.5), 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 13722
    m_Name = '战斗法师'
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
    m_Career = None

