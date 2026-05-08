# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/bossrelic/p51008.pyc
# RelativePath: clientlogic/cl_platformdata/pc/bossrelic/p51008.pyc
# Source Generated with Decompyle++
# File: p51008.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bossrelic import CBossRelic as CCustomPerform
from cl_newformula import Func326, Func589
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1967)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'TotalDam', (lambda *a: Func326(*a)))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'TotalDam') >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func589(*a) * 0.15)):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'TotalDam', 0)
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1967, 0, { })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
        3905: 1,
        3902: 1,
        3904: 1,
        3909: 1 }):
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1967, 'OffsetY', 50, None)
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1967, 'OffsetZ', -10, None)
    if cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
        3901: 1 }):
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1967, 'OffsetY', 15, None)
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1967, 'SizeX', 10, None)
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1967, 'SizeY', 16, None)
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1967, 'SizeZ', 6, None)


class CPerform(CCustomPerform):
    m_SID = 51008
    m_Name = '鱼龙毒球试炼'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = {
        'TotalDam': 0 }
    m_DieDisable = 1
    m_HeroRelic = 15801
    m_LimitMonster = { }
    m_ExcludeMonster = {
        3909: 1,
        3903: 1,
        3913: 1,
        3914: 1 }

