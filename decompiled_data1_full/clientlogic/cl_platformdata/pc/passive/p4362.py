# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4362.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4362.pyc
# Source Generated with Decompyle++
# File: p4362.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7142: 1,
        7141: 1,
        7143: 1 }, 1, 0) and cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'HadHit') == 0:
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'HadHit', 1)
        cl_evact.PassiveSubPerformCD(oWarrior, oEventCB, 7150, 100)


class CPerform(CCustomPerform):
    m_SID = 4362
    m_Name = '究极进化'
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

