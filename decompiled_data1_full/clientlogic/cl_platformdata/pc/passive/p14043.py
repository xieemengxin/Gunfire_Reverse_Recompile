# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14043.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14043.pyc
# Source Generated with Decompyle++
# File: p14043.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERSISTENCE, OBJ_VICTIM, WARRIOR_HERO
from cl_newformula import Func410, Func412

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERSISTENCE):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7138, 500, { }, 0, 1, None)
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func412(*a, **{
'iState': 7138 }))) < 5:
                cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 7138, 1, 0)
                cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1003, 0, 14043, None)
                cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 1003, 7138, {
                    'MoveSpeedMul': (lambda *a: Func410(*a, **{
'sid': 7138 }) * -1000) }, 0, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 14043
    m_Name = '轮回9-大漠幼豚'
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

