# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p15710.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p15710.pyc
# Source Generated with Decompyle++
# File: p15710.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import MG_TALENT, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL, VIRTUAL_ITEM_TALENT

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPGRADEREWARD_CREATE, -1, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPGRADEREWARD_CREATE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckLoading(oWarrior, oEventCB) == 0:
        cl_action.PassiveSetSurvivorChooseAllCnt(oWarrior, oEventCB.GetCBLifeCycle(), VIRTUAL_ITEM_TALENT, 3)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckLoading(oWarrior, oEventCB) == 0:
        cl_action.PassiveSetSurvivorChooseAllCnt(oWarrior, oEventCB.GetCBLifeCycle(), VIRTUAL_ITEM_TALENT, 5)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_TALENT):
        cl_evact.EventCBSetMiniGameChooseCnt(oWarrior, oEventCB, 2)


class CPerform(CCustomPerform):
    m_SID = 15710
    m_Name = '塞翁失马'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 0
    m_BasePrice = 120
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

