# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50216.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50216.pyc
# Source Generated with Decompyle++
# File: p50216.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_HERO, OBJ_ATTACK, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 32775, 1, 0)):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 10000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 50216
    m_Name = '英雄核心'
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
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = (213,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 1
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

