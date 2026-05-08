# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50102.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50102.pyc
# Source Generated with Decompyle++
# File: p50102.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_DEVICE, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 205):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50112)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 201):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50111)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 206):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50113)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50114)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 212):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50115)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 213):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50116)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50117)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 215):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50118)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 216):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50119)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50110)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 218):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50266)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 219):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50267)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, -7500, 0, '')


class CPerform(CCustomPerform):
    m_SID = 50102
    m_Name = '昙花'
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
    m_ExclusiveHero = ()
    m_ExcludeComp = (50100, 50101)
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 0

