# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/bossrelic/p51006.pyc
# RelativePath: clientlogic/cl_platformdata/pc/bossrelic/p51006.pyc
# Source Generated with Decompyle++
# File: p51006.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bossrelic import CBossRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, USEPERFORM_POSTYPE_CARTOONEND

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 1, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1957)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1958)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf51006', 0) and cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'Attack'):
        cl_evact.PassiveCBUsePerformAtMsgSkillPos(oWarrior, oEventCB, 1957, { }, USEPERFORM_POSTYPE_CARTOONEND)
        cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'pf51006', 0, -10000)
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf51006', 0) and cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'Relic'):
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1958, 1, { })
        cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'pf51006', 0, -10000)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        39012: 1,
        39013: 1,
        39015: 1,
        39156: 1,
        39054: 1,
        39016: 1,
        39011: 1,
        39055: 1 }, 1, 0) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 300)
        cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'pf51006', 1, 0)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            39056: 1,
            39057: 1 }, 1, 0):
            cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1958, 'OffsetY', 25, None)
            cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1958, 'OffsetZ', -35, None)
            cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1958, 'OffsetX', -1, None)
        if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            39095: 1,
            39091: 1,
            39094: 1,
            39096: 1,
            39092: 1 }, 1, 0):
            cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1958, 'OffsetY', 25, None)
            cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1958, 'OffsetZ', -15, None)
            cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1958, 'OffsetX', 0, None)
        if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            39095: 1,
            39091: 1,
            39096: 1,
            39094: 1,
            39056: 1,
            39057: 1,
            39241: 1,
            39025: 1,
            39024: 1,
            39023: 1,
            39026: 1,
            39029: 1,
            39242: 1,
            39243: 1,
            39247: 1,
            39043: 1,
            39244: 1,
            39152: 1,
            39092: 1 }, 1, 0) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 300)
            cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'pf51006', 1, 0)


class CPerform(CCustomPerform):
    m_SID = 51006
    m_Name = '鱼龙击地试炼'
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
    m_BaseArgData = { }
    m_DieDisable = 1
    m_HeroRelic = 0
    m_LimitMonster = { }
    m_ExcludeMonster = {
        3903: 1,
        3920: 1,
        3901: 1,
        3915: 1,
        3905: 1,
        3906: 1,
        3913: 1,
        3914: 1,
        3921: 1 }

