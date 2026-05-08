# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50218.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50218.pyc
# Source Generated with Decompyle++
# File: p50218.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_HERO, OBJ_VICTIM, PF_TYPE_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf50218', 0) == 1:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBAddTargetToxicStateCount(oWarrior, oEventCB, {
                'AddCount': 1 })
        elif cl_condition.GetDeviceEnergyRatio(oWarrior, oEventCB.GetCBLifeCycle()) >= 50:
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf50218', 1, 0)
            cl_evact.EventChangeDeviceEnergy(oWarrior, oEventCB, -500, 0)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBAddTargetToxicStateCount(oWarrior, oEventCB, {
                'AddCount': 1 })


class CPerform(CCustomPerform):
    m_SID = 50218
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
    m_ExclusiveDevice = (1001,)
    m_ExclusiveHero = (214,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

