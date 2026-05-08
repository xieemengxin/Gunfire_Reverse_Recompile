# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25795.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25795.pyc
# Source Generated with Decompyle++
# File: p25795.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_LOW
from cl_newformula import Func304, Func553

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1677, 0, { }, -1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 20026, 0, { }, -1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1714, 0, { }, -1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALCURE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1714, (lambda *a: Func553(*a, **{
'sAttr': 'HP' }) * 100 // Func304(*a, **{
'sAttr': 'HPMax' })), -1)


class CPerform(CCustomPerform):
    m_SID = 25795
    m_Name = '火焰狂热'
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
    m_RelicType = 0
    m_HeroRelic = 5795
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

