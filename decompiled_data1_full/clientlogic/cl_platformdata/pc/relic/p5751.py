# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5751.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5751.pyc
# Source Generated with Decompyle++
# File: p5751.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import PF_TYPE_CAREERPF, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDPERFORMCD, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDPERFORMCD, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, None) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 33):
        cl_evact.EventCBSetCurPerformCD(oWarrior, oEventCB, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, None) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 33):
        if cl_evcon.CheckPerformUnCrtByOwner(oWarrior, oEventCB) == 0 or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1312, -1, -1):
            cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 0, 100)
            cl_action.CommonSubPointPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1310, 0, 100)
            cl_evact.EventCBSetCurPerformCD(oWarrior, oEventCB, 0)


class CPerform(CCustomPerform):
    m_SID = 5751
    m_Name = '魔术怀表'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 120
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

