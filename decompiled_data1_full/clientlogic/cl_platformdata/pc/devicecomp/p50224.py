# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50224.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50224.pyc
# Source Generated with Decompyle++
# File: p50224.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_HERO, GAMBLER_CHOOSE_EQUITY, GAMBLER_REPLACE_DEFAULT, QUALITY_TYPE_CURSE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DamageNum') >= 2:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DamageNum', 0)
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            1: 8000,
            2: 2000 }, 1)
    else:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'DamageNum', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonAppendMaxProbQuality(oWarrior, oEventCB.GetCBLifeCycle(), GAMBLER_CHOOSE_EQUITY, 1, 1, GAMBLER_REPLACE_DEFAULT)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonAppendQuality(oWarrior, oEventCB.GetCBLifeCycle(), QUALITY_TYPE_CURSE, GAMBLER_CHOOSE_EQUITY, 1, 1, GAMBLER_REPLACE_DEFAULT, None)


class CPerform(CCustomPerform):
    m_SID = 50224
    m_Name = '英雄核心'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = (216,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

