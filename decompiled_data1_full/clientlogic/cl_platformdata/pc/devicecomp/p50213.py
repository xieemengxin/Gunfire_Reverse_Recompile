# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50213.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50213.pyc
# Source Generated with Decompyle++
# File: p50213.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.devicecomp.customaction import CustomAction50213 as CustomAction
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 50):
        CustomAction(oWarrior, oEventCB, {
            'PerformId': 8503,
            'MulAtt': 1,
            'CostBullet': 2 })


class CPerform(CCustomPerform):
    m_SID = 50213
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
    m_ExclusiveHero = (212,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 1
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

